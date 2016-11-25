import re
import urlparse

from bs4 import BeautifulSoup

class HtmlParser(object):
    def _get_new_urls(self, url, soup):
        new_urls = set()
        # /view/123.htm
        links = soup.find_all('a', href = re.compile(r"/view/\d+\.htm"))
        for link in links:
            new_url = urlparse.urljoin(url, link['href'])
            new_urls.add(new_url)
        return new_urls

    def _get_new_data(self, url, soup):
        data = {}

        # url
        data['url'] = url

        # <dd class="lemmaWgt-lemmaTitle-title"> <h1>Python</h1>
        title = soup.find('dd', class_ = "lemmaWgt-lemmaTitle-title").find('h1')
        data['title'] = title.get_text()

        # <div class="lemma-summary" label-module="lemmaSummary">
        summary = soup.find('div', class_ = "lemma-summary")
        data['summary'] = summary.get_text()

        return data

    def parse(self, url, html_cont):
        if url is None or html_cont is None:
            return
        soup = BeautifulSoup(html_cont, 'html.parser', from_encoding = 'utf-8')
        new_urls = self._get_new_urls(url, soup)
        new_data = self._get_new_data(url, soup)
        return new_urls, new_data