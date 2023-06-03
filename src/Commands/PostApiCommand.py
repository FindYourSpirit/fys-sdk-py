from abc import ABC, abstractmethod
import asyncio
from http import client

class IApiCommand(ABC):
    @abstractmethod
    async def ExecuteAsync(self, endpoint, content):
        pass

class PostApiCommand(IApiCommand):
    def __init__(self, configuration):
        self._configuration = configuration
        self._httpClient = client.HTTPClient()

    async def ExecuteAsync(self, endpoint, content):
        async with self._httpClient.request("POST", endpoint, body=content) as response:
            return await self._handleResponseAsync(response)

    def _addCommonHeaders(self, request):
        request.headers["Authorization"] = self._configuration.ApiKey
        request.headers["JwtToken"] = self._configuration.JwtToken

    async def _handleResponseAsync(self, response):
        if response.status == 200:
            return await response.read()
        else:
            errorContent = await response.read()
            raise ApiException(f"Error occurred while making API request. Status Code: {response.status}. Response: {errorContent}")

    def Dispose(self):
        self._httpClient.close()
