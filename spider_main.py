import html_downloader
import url_manager
import html_parser
import html_outputer


class SpiderMain(object):
    def __init__(self):
        self.urls = url_manager.UrlManager()
        self.downloader = html_downloader.HtmlDownloader()
        self.parser = html_parser.HtmlParser()
        self.outputer = html_outputer.HtmlOutputer()

    def craw(self, entry_url):
        cnt = 1
        self.urls.add_new_url(entry_url)
        while self.urls.has_new_url():
            try:
                new_url = self.urls.get_new_urls()
                html_cont = self.downloader.download(new_url)
                new_urls, new_data = self.parser.parse(new_url, html_cont)
                self.urls.add_new_urls(new_urls)
                self.outputer.collect_data(new_data)
                print cnt, 'OK.', new_url
                if cnt == 100:
                    break
                cnt = cnt + 1
            except:
                print 'failed'
        self.outputer.output_html()

if __name__ == "__main__":
    # Baidu
    entry_url = "http://baike.baidu.com/view/262.htm"
    obj_spider = SpiderMain()
    obj_spider.craw(entry_url)