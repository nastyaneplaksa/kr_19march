from bs4 import BeautifulSoup
import requests

def get_news_text(url):
    try:
        headers = {
            "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36"
        }
        resp = requests.get(url, headers=headers, timeout=10)
        resp.raise_for_status()

        soup = BeautifulSoup(resp.text, "html.parser")

        # Эвристика для kp.ru: обычно текст в основном теге <div> или <article>
        # Можно чуть уточнить под текущую страницу, но сделаем просто‑просто
        article = soup.find("article") or soup.find("div", class_="news-feed_item")
        if not article:
            article = soup  # если не найдено, хотя бы всё, что есть

        # Убираем ненужные блоки: реклама, подписные формы и т.п.
        for ads in article.find_all(["script", "style", "aside", "footer"]):
            ads.decompose()

        text = article.get_text(separator=" ", strip=True)
        return text[:10000]  # ограничение на длинные статьи
    except Exception as e:
        print(f"Ошибка парсинга новости: {e}")
        return None
