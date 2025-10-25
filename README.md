# AgentRouter SDK

Библиотека для общения с AI моделями через AgentRouter API

## Быстрый старт

### 1. Установка
```bash
pip install agentrouter-sdk
```

### 2. Подключение
```python
from client import AgentRouter

client = AgentRouter(api_key="ваш-ключ")
```

### 3. Задать вопрос AI
```python
ответ = client.ask("Привет, как дела?")
print(ответ)
```

Готово! 🎉

---

## Основные функции

### `ask()` - Простой вопрос-ответ
Задайте вопрос, получите текстовый ответ.

**Параметры:**
- `question` - ваш вопрос (текст)
- `model` - название AI модели (по умолчанию: `"deepseek-v3.2"`)
- `temperature` - креативность ответа от 0 до 2 (по умолчанию: `0.7`)
- `max_tokens` - максимальная длина ответа (по умолчанию: `1000`)

**Пример:**
```python
ответ = client.ask(
    question="Что такое Python?",
    model="deepseek-v3.2",
    temperature=0.5,
    max_tokens=200
)
```

---

### `chat()` - Диалог с историей
Ведите беседу с AI, сохраняя контекст предыдущих сообщений.

**Параметры:**
- `messages` - список сообщений или одна строка
- `model` - название AI модели
- `temperature` - креативность (0-2)
- `max_tokens` - максимальная длина ответа
- `stream` - потоковый режим (True/False)

**Пример:**
```python
история = [
    {"role": "user", "content": "Привет!"},
    {"role": "assistant", "content": "Здравствуйте!"},
    {"role": "user", "content": "Расскажи про Python"}
]

response = client.chat(история, max_tokens=300)
print(response.choices[0].message.content)
```

---

### `stream()` - Получение ответа частями
AI отвечает постепенно, слово за словом (как ChatGPT в браузере).

**Параметры:**
- `messages` - ваш вопрос или список сообщений
- `model` - название AI модели
- `temperature` - креативность (0-2)
- `max_tokens` - максимальная длина ответа

**Пример:**
```python
for часть in client.stream("Напиши стихотворение про код"):
    print(часть, end="", flush=True)
```

---

### `list_models()` - Список доступных AI моделей
Узнайте, какие модели можно использовать.

**Пример:**
```python
модели = client.list_models()
print(модели)  # ['deepseek-v3.2', 'gpt-5', 'glm-4.6', ...]
```

---

### `count_tokens()` - Подсчет использованных токенов
Узнайте, сколько "слов" использовалось в запросе и ответе.

**Пример:**
```python
response = client.chat("Привет!")
токены = client.count_tokens(response)
print(f"Всего токенов: {токены['total']}")
```

---

## Полный пример

```python
from agentrouter import AgentRouter

# Подключаемся
client = AgentRouter(api_key="ваш-ключ")

# Простой вопрос
ответ = client.ask("Напиши Hello World на Python")
print(ответ)

# Узнаем доступные модели
модели = client.list_models()
print("Доступны модели:", модели)

# Потоковый ответ
print("AI отвечает: ", end="")
for часть in client.stream("Расскажи анекдот", max_tokens=100):
    print(часть, end="", flush=True)
```

---

## Дополнительные настройки (опционально)

Обычно достаточно указать только API ключ. Но можно изменить настройки:

```python
client = AgentRouter(
    api_key="ваш-ключ"           # только это обязательно!
    
    # Остальное можно не трогать, работает по умолчанию:
    # base_url="https://agentrouter.org/v1"
    # referer="https://github.com/RooVetGit/Roo-Cline"
    # title="Roo Code"
    # user_agent="RooCode/1.0.0"
)
```
