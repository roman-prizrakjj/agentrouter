# cURL команда для n8n

## Получить список моделей

```bash
curl -X GET https://agentrouter.org/v1/models \
  -H "Authorization: Bearer YOUR_API_KEY" \
  -H "HTTP-Referer: https://github.com/RooVetGit/Roo-Cline" \
  -H "X-Title: Roo Code" \
  -H "User-Agent: RooCode/1.0.0"
```

## Отправить сообщение в чат

```bash
curl -X POST https://agentrouter.org/v1/chat/completions \
  -H "Authorization: Bearer YOUR_API_KEY" \
  -H "HTTP-Referer: https://github.com/RooVetGit/Roo-Cline" \
  -H "X-Title: Roo Code" \
  -H "User-Agent: RooCode/1.0.0" \
  -H "Content-Type: application/json" \
  -d '{
    "model": "deepseek-v3.2",
    "messages": [{"role": "user", "content": "Hello!"}],
    "temperature": 0.2,
    "max_tokens": 50
  }'
```

# НОДА HTTP
<img width="245" height="188" alt="image" src="https://github.com/user-attachments/assets/818cf227-a37f-4000-9101-4befa79bd9d5" />
# ВЫБРАТЬ ИМПОРТ
<img width="591" height="505" alt="image" src="https://github.com/user-attachments/assets/abd33018-61b4-4604-9acc-95cb5d3aa54b" />
# ВСТАВИТЬ CURL
<img width="631" height="272" alt="image" src="https://github.com/user-attachments/assets/031ac23d-0018-4d59-8ebc-9b4cf7603716" />
#ВСТАВИТЬ КЛЮЧ 
<img width="561" height="413" alt="image" src="https://github.com/user-attachments/assets/53cd3d9e-4790-49b1-ad3f-7213c1e384fb" />



