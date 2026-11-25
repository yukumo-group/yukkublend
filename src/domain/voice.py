from dataclasses import dataclass

from .engines import Engine
from .params import BaseParam


@dataclass
class Voice:
    name: str
    params: dict[Engine, BaseParam]
    base_speed: float = 1.0
    monotone: bool = False
