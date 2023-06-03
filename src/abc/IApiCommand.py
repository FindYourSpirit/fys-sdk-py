from abc import ABC, abstractmethod
import asyncio

class IApiCommand(ABC):
    @abstractmethod
    async def ExecuteAsync(self, endpoint, content):
        pass
