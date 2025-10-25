from agentrouter import AgentRouter

# Инициализация клиента
client = AgentRouter(api_key="your-api-key")

# Пример 1: Простой вопрос
print("=== Простой вопрос ===")
answer = client.ask("Что такое Python?", max_tokens=100)
print(answer)
print()

# Пример 2: Чат с историей
print("=== Чат с историей ===")
messages = [
    {"role": "user", "content": "Привет!"},
    {"role": "assistant", "content": "Здравствуйте! Чем могу помочь?"},
    {"role": "user", "content": "Расскажи про Python"}
]
response = client.chat(messages, max_tokens=150)
print(response.choices[0].message.content)
print()

# Пример 3: Потоковая генерация
print("=== Потоковая генерация ===")
for chunk in client.stream("Напиши короткое стихотворение про код", max_tokens=100):
    print(chunk, end="", flush=True)
print("\n")

# Пример 4: Список моделей
print("=== Доступные модели ===")
models = client.list_models()
for model in models:
    print(f"- {model}")
print()

# Пример 5: Подсчет токенов
print("=== Подсчет токенов ===")
response = client.chat("Hello!", max_tokens=50)
tokens = client.count_tokens(response)
print(f"Prompt: {tokens['prompt']} токенов")
print(f"Completion: {tokens['completion']} токенов")
print(f"Всего: {tokens['total']} токенов")
