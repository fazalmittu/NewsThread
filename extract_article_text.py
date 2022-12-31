import requests
from bs4 import BeautifulSoup
from draft_thread import generate_thread


# url = "https://www.wsj.com/articles/apple-production-in-china-begins-to-catch-up-despite-covid-19-woes-11672315005?mod=tech_lead_pos1"
url = "https://www.bbc.com/future/article/20220804-the-lost-nuclear-bombs-that-no-one-can-find"
res = requests.get(url)
html_page = res.content

soup = BeautifulSoup(html_page, 'html.parser')

text = soup.find_all(text=True)

print(set([t.parent.name for t in text])) # shows all the html tags

output = ''
blacklist = [
    '[document]',
    'noscript',
    'header',
    'html',
    'meta',
    'head', 
    'input',
    'script',
    'style',
    'button'
] # elements that we don't want

for t in text:
    if t.parent.name not in blacklist:
        output += '{} '.format(t)

print(output)

# print(generate_thread(output))