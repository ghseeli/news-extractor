from bs4 import BeautifulSoup
import requests

def get_articles_from_page_data(page, depth = 1):
    base_url = page.url.replace("http://","").replace("www.","")
    print(base_url)
    soup = BeautifulSoup(page.content(), 'html.parser')
    url_strings = [link.get('href') for link in soup.find_all('a')]
    internal_url_strings = [link for link in url_strings if possible_article_link(link,base_url)]
    return internal_url_strings

def possible_article_link(url, base_url):
    is_part_of_site = base_url in url or './' in url
    ends_as_webpage = ".htm" in url
    not_an_index_page = "index.html" not in url
    return is_part_of_site and ends_as_webpage and not_an_index_page
