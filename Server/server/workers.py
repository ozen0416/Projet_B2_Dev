from typing import Any, Optional

from .abc import AbstractWorker


class HitWorker(AbstractWorker):
    async def handle(self, request_type: Any, request: Any) -> Optional[str]:
        return f"Hit worker response. Received: {request['data']}"


class PlacementWorker(AbstractWorker):
    async def handle(self, request_type: Any, request: Any) -> Optional[str]:
        return f"Placement request response. Received: {request['data']}"
