import unittest

from sitemap_search import sitemap_search


class SitemapTest(unittest.TestCase):
    def test_sitemap_search_correct_url(self):
        entry_url = [
            "https://www.halifax.co.uk/",
            "https://www.nationwide.co.uk/",
            "https://blog.moneysavingexpert.com/",
            "https://www.bbc.com/",
            "http://feeds.copyblogger.com/",
            "https://contently.com/",
            "https://www.salesforce.com/",
        ]
        for look in entry_url:
            sitemap_links = sitemap_search(look)
            new_sitemap_links = f"{look}sitemap.xml"
            new_sitemap_links_exception = None
            if sitemap_links:
                self.assertEqual(new_sitemap_links, sitemap_links)
            else:
                self.assertEqual(new_sitemap_links_exception, sitemap_links)

    def test_sitemap_search_wrong_url(self):
        entry_url = [
            "https://www.halifax.co.uk/money-explained/",
            "https://www.nationwide.co.uk/guides/news/all-news",
            "http://feeds.copyblogger.com/copyblogger",
            "https://emea.epsilon.com/blog/",
            "http://feeds.copyblogger.com/copyblogger",
            "https://contently.com/strategist/",
            "https://www.salesforce.com/blog/",
        ]
        for look in entry_url:
            sitemap_links = sitemap_search(look)
            new_sitemap_links = f"{look}sitemap.xml"
            new_sitemap_links_exception = None
            if sitemap_links:
                self.assertEqual(new_sitemap_links, sitemap_links)
            else:
                self.assertEqual(new_sitemap_links_exception, sitemap_links)

    def test_sitemap_search_no_url(self):
        entry_url = ["123", "abc", "", "@#45", ""]
        for look in entry_url:

            sitemap_links = sitemap_search(look)
            new_sitemap_links = f"{look}sitemap.xml"
            new_sitemap_links_exception = None
            if sitemap_links:
                self.assertEqual(new_sitemap_links, sitemap_links)
            else:
                self.assertEqual(new_sitemap_links_exception, sitemap_links)


if __name__ == "__main__":
    unittest.main()
