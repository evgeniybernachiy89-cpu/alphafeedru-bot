```python
import requests
from config import BOT_TOKEN, CHAT_ID
from database import get_ready_posts, mark_published

def run():
    posts = get_ready_posts(limit=3)
    for post_id, text in posts:
        url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"
        payload = {"chat_id": CHAT_ID, "text": text, "parse_mode": "HTML"}
        try:
            r = requests.post(url, json=payload)
            if r.ok:
                mark_published(post_id)
                print(f"Пост #{post_id} опубликован")
            else:
                print(f"Ошибка публикации поста #{post_id}: {r.text}")
        except Exception as e:
            print(f"Ошибка: {e}")

if __name__ == "__main__":
    run()
```