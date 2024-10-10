from celery_worker.celery_configurations import process_rss_feed

# List of RSS feeds to process
rss_feeds = [
    "http://rss.cnn.com/rss/cnn_topstories.rss",
    "http://qz.com/feed",
    "http://feeds.foxnews.com/foxnews/politics",
    "http://feeds.reuters.com/reuters/businessNews",
    "http://feeds.feedburner.com/NewshourWorld",
    "https://feeds.bbci.co.uk/news/world/asia/india/rss.xml"
]

# Trigger Celery tasks for each feed URL
for feed_url in rss_feeds:
    result = process_rss_feed.delay(feed_url)
    print(f"Task for {feed_url} submitted with task ID: {result.id}")
