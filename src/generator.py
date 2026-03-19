# hse_kr/src/generator.py
from huggingface_hub import InferenceClient
from config.settings import HF_TOKEN


class MediaGenerator:
    def __init__(self):
        self.client = InferenceClient(
            base_url="https://router.huggingface.co/v1",
            api_key=HF_TOKEN,
        )

    def generate_headline(self, news_text, style="новостной стиль"):
        prompt = f"""
На основе этой новости сгенерируй короткий, цепляющий заголовок для соцсетей.
Стиль: {style}.
Максимум 100 символов.
Новость:
{news_text}
        """.strip()

        messages = [
            {"role": "user", "content": prompt}
        ]
        try:
            resp = self.client.chat.completions.create(
                model="meta-llama/Llama-3.1-8B-Instruct",
                messages=messages,
                max_tokens=64,
                temperature=0.7,
            )
            return resp.choices[0].message.content.strip()
        except Exception as e:
            return f"Ошибка: {e}"


