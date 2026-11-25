from dataclasses import dataclass, field

from .voice import Voice


@dataclass
class Character:
    name: str
    description: str
    avatar: bytes
    related_models: list[str] = field(default_factory=list)
    voices: list[Voice] = field(default_factory=list)
    version: int = 1000
