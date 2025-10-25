from openai import OpenAI
from typing import List, Dict, Optional, Iterator, Union


class AgentRouter:
    """
    Простой SDK для работы с AgentRouter API
    """
    
    def __init__(
        self,
        api_key: str,
        base_url: str = "https://agentrouter.org/v1",
        referer: str = "https://github.com/RooVetGit/Roo-Cline",
        title: str = "Roo Code",
        user_agent: str = "RooCode/1.0.0"
    ):
        """
        Инициализация клиента
        
        Args:
            api_key: API ключ
            base_url: Базовый URL (по умолчанию agentrouter.org)
            referer: HTTP Referer заголовок
            title: X-Title заголовок
            user_agent: User-Agent заголовок
        """
        self.api_key = api_key
        self.base_url = base_url
        
        default_headers = {
            "HTTP-Referer": referer,
            "X-Title": title,
            "User-Agent": user_agent
        }
        
        self.client = OpenAI(
            api_key=api_key,
            base_url=base_url,
            default_headers=default_headers
        )
    
    def chat(
        self,
        messages: Union[str, List[Dict[str, str]]],
        model: str = "deepseek-v3.2",
        temperature: float = 0.7,
        max_tokens: int = 1000,
        stream: bool = False,
        **kwargs
    ):
        """
        Отправка сообщения в чат
        
        Args:
            messages: Сообщение (строка) или список сообщений
            model: Название модели
            temperature: Температура (0-2)
            max_tokens: Максимум токенов в ответе
            stream: Потоковый режим
            **kwargs: Дополнительные параметры для API
            
        Returns:
            Ответ от API или итератор (если stream=True)
        """
        # Преобразуем строку в формат сообщений
        if isinstance(messages, str):
            messages = [{"role": "user", "content": messages}]
        
        response = self.client.chat.completions.create(
            model=model,
            messages=messages,
            temperature=temperature,
            max_tokens=max_tokens,
            stream=stream,
            **kwargs
        )
        
        return response
    
    def ask(
        self,
        question: str,
        model: str = "deepseek-v3.2",
        temperature: float = 0.7,
        max_tokens: int = 1000,
        **kwargs
    ) -> str:
        """
        Простой вопрос-ответ
        
        Args:
            question: Вопрос
            model: Название модели
            temperature: Температура
            max_tokens: Максимум токенов
            **kwargs: Дополнительные параметры
            
        Returns:
            Текст ответа
        """
        response = self.chat(
            messages=question,
            model=model,
            temperature=temperature,
            max_tokens=max_tokens,
            stream=False,
            **kwargs
        )
        
        return response.choices[0].message.content
    
    def stream(
        self,
        messages: Union[str, List[Dict[str, str]]],
        model: str = "deepseek-v3.2",
        temperature: float = 0.7,
        max_tokens: int = 1000,
        **kwargs
    ) -> Iterator[str]:
        """
        Потоковая генерация ответа
        
        Args:
            messages: Сообщение или список сообщений
            model: Название модели
            temperature: Температура
            max_tokens: Максимум токенов
            **kwargs: Дополнительные параметры
            
        Yields:
            Части ответа
        """
        response = self.chat(
            messages=messages,
            model=model,
            temperature=temperature,
            max_tokens=max_tokens,
            stream=True,
            **kwargs
        )
        
        for chunk in response:
            if chunk.choices[0].delta.content is not None:
                yield chunk.choices[0].delta.content
    
    def list_models(self) -> List[str]:
        """
        Получить список доступных моделей
        
        Returns:
            Список названий моделей
        """
        models = self.client.models.list()
        return [model.id for model in models]
    
    def count_tokens(self, response) -> Dict[str, int]:
        """
        Получить информацию об использованных токенах
        
        Args:
            response: Ответ от метода chat()
            
        Returns:
            Словарь с информацией о токенах
        """
        if hasattr(response, 'usage'):
            return {
                "prompt": response.usage.prompt_tokens,
                "completion": response.usage.completion_tokens,
                "total": response.usage.total_tokens
            }
        return {"prompt": 0, "completion": 0, "total": 0}
