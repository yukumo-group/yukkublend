from dataclasses import dataclass

from .voice import Voice


@dataclass
class Character:
    name: str
    description: str
    avatar: bytes
    binded_models: list[str] = []
    voices: list[Voice] = []
    version: int = 1000
