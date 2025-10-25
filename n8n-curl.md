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

