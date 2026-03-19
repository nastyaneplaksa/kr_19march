# hse_kr/main.py
from datetime import datetime
from config.settings import TARGET_URL, HF_TOKEN
from src.scraper import get_news_text
from src.generator import MediaGenerator

OUTPUT_PATH = "outputs/results.txt"


def save_headline(url, headline):
    now = datetime.now().strftime("%Y-%m-%d %H:%M")
    with open(OUTPUT_PATH, "a", encoding="utf-8") as f:
        f.write(f"[{now}] URL: {url}\n")
        f.write(f"Заголовок: {headline}\n\n")
    print(f"Заголовок сохранён в {OUTPUT_PATH}")


def main():
    print("Получение текста новости с kp.ru...")
    text = get_news_text(TARGET_URL)
    if not text:
        print("Не удалось получить текст новости с сайта.")
        return

    print("Генерация заголовка...")
    generator = MediaGenerator()
    headline = generator.generate_headline(text, style="новостной стиль")

    print("Сохранение результата...")
    save_headline(TARGET_URL, headline)
    print("Готово!")


if __name__ == "__main__":
    main()


