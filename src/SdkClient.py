import asyncio

class SdkClient:
    def __init__(self, configuration):
        self._configuration = configuration
        self._getCommand = GetApiCommand(configuration)
        self._postCommand = PostApiCommand(configuration)
        # Instantiate additional command classes for other HTTP methods as needed

    async def GetApiResponseAsync(self, endpoint):
        return await self._getCommand.ExecuteAsync(endpoint, None)

    async def PostApiResponseAsync(self, endpoint, content):
        return await self._postCommand.ExecuteAsync(endpoint, content)

    # Add additional methods for other HTTP methods using the respective command classes

    def Dispose(self):
        self._getCommand.Dispose()
        self._postCommand.Dispose()