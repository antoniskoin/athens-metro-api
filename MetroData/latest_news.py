from bs4 import BeautifulSoup
import requests
from flask_restful import Resource


class News(Resource):
    def get(self):
        url = "http://www.stasy.gr/index.php?id=10"
        r = requests.get(url)
        news = dict()
        if r.status_code == 200:
            soup = BeautifulSoup(r.content, "html.parser")
            content = soup.find("div", {"id": "content"})
            news_container = content.find("div", {"id": "contentin"})
            news_items = news_container.find_all("div", {"class": "news-list-item"})
            count = 0
            for news_item in news_items:
                news_id = count
                date = news_item.find("span", {"class": "news-list-date"}).text.strip()
                heading = news_item.h2.text.strip()
                url = news_item.h2.a["href"]
                description = news_item.p.text
                description = description.replace("[Περισσότερα]", "").replace("...", "").strip()

                if not description:
                    description = "NONE"

                news[news_id] = {
                    "date": date,
                    "heading": heading,
                    "url": url,
                    "description": description
                }

                count += 1

            return news
        else:
            return {"message": f"Request failed with status code: {r.status_code}"}
