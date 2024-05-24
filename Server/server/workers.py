from typing import Any, Optional

from .abc import AbstractWorker


class HitWorker(AbstractWorker):
    async def handle(self, request_type: Any, request: Any) -> Optional[str]:
        return f"Hit worker response. Received: {request['data']}"
