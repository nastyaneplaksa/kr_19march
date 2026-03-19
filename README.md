# 1. Клонировать репозиторий

git clone https://github.com/nastyaneplaksa/kr_19march.git

cd hse_kr

# 2. Установить зависимости

python3 -m venv venv

source venv/bin/activate

pip install -r requirements.txt

# 3. Вставить токен в config/settings.py
# 4. Указать URL новости в config/settings.py
# 5. Запустить

python main.py

Результат:

В outputs/results.txt сохраняются все заголовки:
