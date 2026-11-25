from dataclasses import dataclass

from .. import Engine
from ..voice import Voice
from .supported_languages import Languages


@dataclass
class Sentence:
    voice: Voice
    engine_override: Engine
    language: Languages
    content: str
    speed_factor: float = 1.0
    pitch_factor: float = 1.0
    volume_factor: float = 1.0
    panning: float = 0.0
