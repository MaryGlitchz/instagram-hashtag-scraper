thonimport requests
import time
import json
from extractors.instagram_parser import parse_instagram_post
from outputs.exporters import export_to_json

class InstagramHashtagScraper:
    def __init__(self, hashtag, limit=100, session_cookie=None):
        self.hashtag = hashtag
        self.limit = limit
        self.session_cookie = session_cookie
        self.base_url = "https://www.instagram.com/explore/tags/{}/".format(self.hashtag)
        self.headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36',
            'Cookie': self.session_cookie
        }
    
    def scrape(self):
        usernames = []
        page = 1
        while len(usernames) < self.limit:
            url = f"{self.base_url}?page={page}"
            response = requests.get(url, headers=self.headers)
            if response.status_code != 200:
                print("Error fetching page.")
                break
            data = response.json()
            posts = data.get('graphql', {}).get('hashtag', {}).get('edge_hashtag_to_media', {}).get('edges', [])
            for post in posts:
                username = parse_instagram_post(post)
                if username:
                    usernames.append(username)
                if len(usernames) >= self.limit:
                    break
            page += 1
            time.sleep(2)
        
        export_to_json(usernames, "output.json")

if __name__ == "__main__":
    scraper = InstagramHashtagScraper("travel", limit=10, session_cookie="your_session_cookie")
    scraper.scrape()