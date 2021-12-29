from trafilatura import sitemaps
import logging

LOGGER = logging.getLogger(__name__)


def sitemap_search(entry_url):
    check_sitemap_link = sitemaps.sitemap_search(entry_url)

    sitemap_link = []
    if check_sitemap_link:
        for find_sitemap in check_sitemap_link:
            if "sitemap." in str(find_sitemap):
                try:
                    sitemap_link.append(find_sitemap.replace(".html", ".xml"))

                except (IndexError, KeyError):
                    sitemap_link.append(find_sitemap)

            else:
                pass

    try:
        return sitemap_link[0]
    except (IndexError, KeyError):
        LOGGER.info("No sitemap found Do it manually")
