from ..items import NewsArticleItem, NewsArticleItemLoader
from .base import DailySitemapSpider


class IndianExpressSpider(DailySitemapSpider):
    name = "indianexpress"

    sitemap_frequency = "1D"
    sitemap_patterns = [
        "https://indianexpress.com/sitemap.xml?yyyy={year}&mm={month}&dd={day}"
    ]

    sitemap_rules = [(r"/article/business/", "parse_article")]

    def parse_article(self, response):
        """
        sample article: https://indianexpress.com/article/business/market/indian-shares-record-high-after-sensex-breaches-80000-mark-9431868/
        """

        article = NewsArticleItemLoader(item=NewsArticleItem(), response=response)

        # content
        article.add_css("title", "h1::text")
        article.add_css("description", "h2.synopsis::text")
        article.add_css("author", "div.editor a::text")
        article.add_css("article_html", "div.story-details")

        # dates
        article.add_css(
            "date_published",
            'meta[itemprop="datePublished"]::attr(content)',
        )
        article.add_css(
            "date_modified",
            'meta[itemprop="dateModified"]::attr(content)',
        )

        yield article.load_item()
