import usp
from usp.tree import sitemap_tree_for_homepage

def first_site(url):
    try:
        tree = sitemap_tree_for_homepage(url)
    except:
        print('error')

    links = []
    try:
        for page in tree.all_pages():
            links.append(page)
    except:
        print('error')

    try:
        for i in links:
            print(i)
    except:

        print('error')

first_site('https://igiaviationdelhi.com')