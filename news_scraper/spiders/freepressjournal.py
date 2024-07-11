from ..items import NewsArticleItem, NewsArticleItemLoader
from .base import DailySitemapSpider


class FreePressJournalSpider(DailySitemapSpider):
    name = "freepressjournal"

    sitemap_frequency = "1D"
    sitemap_patterns = [
        "https://www.freepressjournal.in/sitemap/sitemap-daily-{year}-{month}-{day}.xml",
    ]

    sitemap_rules = [(r"/business/", "parse_article")]

    def parse_article(self, response):
        """
        sample article: https://www.freepressjournal.in/business/sbi-raises-10000-cr-via-sixth-infrastructure-bond-issuance-at-736-coupon-rate-oversubscribed-36-times
        """

        article = NewsArticleItemLoader(item=NewsArticleItem(), response=response)

        # content
        article.add_css("title", "h1::text")
        article.add_css("description", "h2#heading-2::text")
        article.add_css("author", "a.author-name::text")
        article.add_css("article_html", "div.article-lhs")

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
