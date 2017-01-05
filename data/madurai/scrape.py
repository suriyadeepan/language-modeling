BASE_URL = 'http://www.projectmadurai.org/pmworks.html'
ROOT = 'http://www.projectmadurai.org'
FORMAT = '/pm_etexts/utf8/'


from bs4 import BeautifulSoup
import requests


def get_soup(url):
    return BeautifulSoup(requests.get(url).content, 'lxml')

def get_text(url):
    tables = get_soup(url).findAll('table')
    if len(tables):
        return [ tag.text for tag in tables ]
    dds = get_soup(url).findAll('dd')
    if len(dds):
        return [ tag.text for tag in dds ]
    body = get_soup(url).findAll('body')
    return [tag.text for tag in body ]

def clean_text(text):
    return ' '.join([ item for item in text.strip().split(' ') if item ])

def grab_links(base_url, url_format, root):
    links = []
    for a in get_soup(base_url).findAll('a'):
        if 'href' in a.attrs:
            href = a.get('href')
            if url_format in href:
                links.append(root + href)
    return links

def scrape():
    corpus = ''
    # grab links
    links = grab_links(BASE_URL, FORMAT, ROOT)
    print('>> Grabbed {} links'.format(len(links)))
    # get text from each link
    for i,link in enumerate(links):
        texts = get_text(link)
        num_chars = len([ch in text_ for text_ in texts for ch in text_])
        print('Grabbed {} characters from {} sections from [{}] {}'.format(num_chars, len(texts), i, link))
        for text in texts:
            corpus += clean_text(text)

    return corpus


if __name__ == '__main__':
    raw_data = scrape()
    print('>> Scraping complete')
    # write to file
    with open('madurai.txt', 'w') as f:
        f.write(raw_data)
