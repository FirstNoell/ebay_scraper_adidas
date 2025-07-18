🛒 eBay Adidas Scraper (Scrapy + Splash)
This project is a simple web scraper built using Scrapy and Splash to extract Adidas product listings from eBay Australia, specifically from the "Athletic Shoes" category.

🔧 Features
Custom User-Agent to mimic real browser behavior.

Uses Splash to handle JavaScript-rendered content.

Extracts key product details:

✅ Product title

✅ Price

✅ Image URL

✅ Product link

Handles pagination to scrape multiple pages.

📄 Spider: adidas
https://www.ebay.com.au/sch/i.html?_from=R40&_trksid=p2380057.m570.l2632&_nkw=adidas&_sacat=93427
Extracted Fields:
title: Name of the product

price: Listed price

image: Product image URL

link: Direct link to the product page

Custom Settings:
custom_settings = {
    'USER_AGENT': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36',
    'DOWNLOADER_MIDDLEWARES': {
        'scrapy.downloadermiddlewares.offsite.OffsiteMiddleware': None,  # Disables offsite filtering
    },
}
Splash Integration:
The spider uses SplashRequest to render JavaScript-heavy pages.

📘 License

This project is for educational and research purposes only. Scraping eBay content must comply with their terms of service.

Developer:
Leoncio U Coronado 
