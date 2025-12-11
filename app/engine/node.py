from typing import Callable, Dict, Any


class Node:
    def __init__(self, name: str, func: Callable):
        self.name = name
        self.func = func

    async def run(self, state: Dict[str, Any]) -> Dict[str, Any]:
        return await self.func(state)
