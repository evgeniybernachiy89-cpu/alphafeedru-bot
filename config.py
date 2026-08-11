```python
import os

# --- Telegram ---
BOT_TOKEN = os.environ.get("BOT_TOKEN")
CHAT_ID = "@Bistrobobot"

# --- OpenAI ---
OPENAI_API_KEY = os.environ.get("OPENAI_API_KEY")

# --- Ключевые слова для фильтрации ---
KEYWORDS = ["IT", "AI", "Python", "автоматизация", "нейросети"]

# --- RSS-источники ---
RSS_FEEDS = [
    "https://habr.com/ru/rss/all/",
    "https://news.ycombinator.com/rss"
]
```