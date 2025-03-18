# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import datetime

from .._models import BaseModel

__all__ = ["ObjectListResponse", "Object"]


class Object(BaseModel):
    content_type: Optional[str] = None
    """MIME type of the object"""

    key: Optional[str] = None
    """Object key/path in the bucket"""

    last_modified: Optional[datetime] = None
    """Last modification timestamp"""

    size: Optional[str] = None
    """Size of the object in bytes (as string due to potential BigInt values)"""


class ObjectListResponse(BaseModel):
    objects: Optional[List[Object]] = None
