

import re

from usp.tree import sitemap_tree_for_homepage

tree = sitemap_tree_for_homepage("https://www.halifax.co.uk/money-explained/")
check_url = [str(i) for i in tree.all_pages()]

out=[]
def Find(string):
    regex = r"(?i)\b((?:https?://|www\d{0,3}[.]|[a-z0-9.\-]+[.][a-z]{2,4}/)(?:[^\s()<>]+|\(([^\s()<>]+|(\([^\s()<>]+\)))*\))+(?:\(([^\s()<>]+|(\([^\s()<>]+\)))*\)|[^\s`!()\[\]{};:'\".,<>?«»“”‘’]))"
    url = re.findall(regex, string)
    return [x[0] for x in url]

def reemovNestings(l):

    for i in l:
        if type(i) == list:
            reemovNestings(i)
        else:
            out.append(i)


if bool(check_url):
    links = [Find(j) for j in check_url]
    reemovNestings(links)
    print("Process url")

else:
    print('manually')

print(out)