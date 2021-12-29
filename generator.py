import json
import base64
import os
import cloudscraper
import logging
from db import get_db
from helpers import (
    collect_links_from_xml,
    collect_links_from_txt,
    get_difference_links,
    publish_to_before_scraper,
    _update_crawling,
    Find_re,
    reemovNestings,
    out,
)
from gcs_helpers import upload_file_to_gcs, get_file_from_gcs
from constants import GCS_BUCKET_NAME
from trafilatura import sitemaps

from usp.tree import sitemap_tree_for_homepage

logging.basicConfig(level=logging.NOTSET)
LOGGER = logging.getLogger(__name__)


def sitemap_main(event, context):
    LOGGER.info(
        f"Running the sitemap generator for Event Id: {context.event_id}  and timestamp: {context.timestamp}"
    )
    if "data" in event:
        #decoded_message = base64.b64decode(event["data"]).decode("utf-8")
        #message = json.loads(decoded_message)

        try:
            brand, source = event["data"]
        except (KeyError, IndexError, RuntimeError, ValueError):
            LOGGER.error("Error in unpacking values. Please check the message passed")
            return {}

        else:
            db = get_db()
            _update_crawling(brand, source, start=1)
            query = {"name": brand, "sources.name": source}
            projection = {"sources.$": 1}
            brand_object = db.brands.find_one(query, projection)
            if not brand_object:
                LOGGER.warning(
                    "Brand and Source not found. Exiting the sitemap generation process"
                )

            try:
                entry_url = brand_object["sources"][0]["entry"][0]
            except (KeyError, IndexError) as exception:
                # Update Crawling field due to fail in crawling with exception message
                _update_crawling(brand, source, finish=1, exception=str(exception))

                LOGGER.error(
                    f"[{brand}, {source}] do not contain a valid sitemap URL to be crawled"
                )
                return {}

            try:
                tree = sitemap_tree_for_homepage(entry_url)
                check_url = [i for i in tree.all_pages()]
                LOGGER.info(f"Running 1")

                if bool(check_url):
                    LOGGER.info(f"Running 2")
                    file_name = f"{brand}-{source}-sitemap.txt"
                    file_name = file_name.lower().replace(" ", "_")
                    LOGGER.info(f"Running 3")
                    sitemap_file1 = get_file_from_gcs(file_name, GCS_BUCKET_NAME)
                    with open(f"/tmp/{file_name}", "a") as f:
                        LOGGER.info(f"Running 4")
                        for link in check_url:
                            f.write(f"{link}\n")
                    f.close()
                    LOGGER.info(f"Running 5")
                    bucket = os.environ.get(GCS_BUCKET_NAME)
                    LOGGER.info(f"Running 6")
                    upload_file_to_gcs(f"/tmp/{file_name}", bucket)
                    LOGGER.info('Processing the URL')
                else:
                    LOGGER.info('Do it manually')
            except:
                LOGGER.error(f"Manually configure the sitemap")

            else:
                headers = {
                    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36"
                }
                scraper = cloudscraper.create_scraper()
                response = scraper.get(entry_url, headers=headers)
                file_name = f"{brand}-{source}-sitemap.txt"
                file_name = file_name.lower().replace(" ", "_")
                sitemap_file = get_file_from_gcs(file_name, GCS_BUCKET_NAME)

                try:
                    scrape_rule = brand_object["sources"][0]["scrape"]["white_list"]
                except (IndexError, KeyError):
                    LOGGER.error(
                        f"Brand/Source : {brand}/{source} does not contain a valid Scrape Rule. "
                        f"Please re-configure the brand/source entry"
                    )
                    return {}
                try:
                    black_scrape_rule = brand_object["sources"][0]["scrape"][
                        "black_list"
                    ]
                except (IndexError, KeyError):
                    black_scrape_rule = []

                if sitemap_file:
                    new_links = collect_links_from_xml(
                        response.text, brand, source, scrape_rule, black_scrape_rule
                    )
                    old_links = collect_links_from_txt(
                        sitemap_file, brand, source, scrape_rule, black_scrape_rule
                    )
                    publish_to_before_scraper(old_links, brand, source)
                    different_links = get_difference_links(new_links, old_links)
                    if different_links:
                        # Updating the sitemap file, using the append mode.
                        # This update file will be then updated to the GCS server
                        links_to_send = different_links
                        with open(sitemap_file, "a") as sitemap:
                            for link in different_links:
                                sitemap.write(f"\n{link}")
                    else:
                        LOGGER.warning(
                            f"No new links found while Scraping the sitemap for [{brand}, {source}]. Exiting, the "
                            f"sitemap generator"
                        )
                        return {}
                else:
                    links_to_send = collect_links_from_xml(
                        response.text, brand, source, scrape_rule, black_scrape_rule
                    )
                    with open(f"/tmp/{file_name}", "a") as f:
                        for link in links_to_send:
                            f.write(f"{link}\n")
                    f.close()
                try:
                    # This method will upload the file at "/tmp/file_name
                    # to Google Cloud Storage. Please check constants.py for
                    # name of the bucket to where the file will be uploaded
                    bucket = os.environ.get(GCS_BUCKET_NAME)
                    upload_file_to_gcs(f"/tmp/{file_name}", bucket)
                    publish_to_before_scraper(links_to_send, brand, source)
                except Exception as e:
                    # Update crawling field with ex ception message
                    _update_crawling(brand, source, finish=1, exception=str(e))
                    # End of update crawling
                    LOGGER.error(f"Error in writing file to GCS. Traceback: {e}")
                    return {}
                else:
                    # All is well, updating the crawling attribute without the exception message
                    _update_crawling(brand, source, finish=1)
                    LOGGER.info(
                        f"Fresh new sitemap for [{brand},{source}] uploaded to GCS Bucket."
                    )
                    return {}
