from dataclasses import dataclass

from ..voice import Voice
from .supported_languages import Languages


@dataclass
class Sentence:
    voice: Voice
    language: Languages
    content: str
    speed_factor: float = 1.0
    pitch_factor: float = 1.0
    volume_factor: float = 1.0
    panning: float = 0.0
