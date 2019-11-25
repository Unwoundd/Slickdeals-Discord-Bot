import feedparser

def get_frontpage(): #Merge this function with get_item and using a default parameter
    feed = feedparser.parse("https://slickdeals.net/newsearch.php?mode=frontpage&searcharea=deals&searchin=first&rss=1")
    hold_msgs = []
    build_msg = ""
    for key in feed.entries:
        title = key['title']
        link = key['link']
        print("Key:",title," link:",link)
        build_msg = f"> {link}"
        hold_msgs.append(build_msg)
    return hold_msgs

def get_item(link):
    feed = feedparser.parse(link)
    hold_msgs = []
    build_msg = ""
    for key in feed.entries:
        title = key['title']
        link = key['link']
        print("Key:",title," link:",link)
        build_msg = f"> {link}" 
        hold_msgs.append(build_msg)
    return hold_msgs

