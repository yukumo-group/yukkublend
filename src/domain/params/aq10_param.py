from dataclasses import dataclass
from enum import Enum

from .base_param import BaseParam


class Aq10BaseVoice(Enum):
    F1E = 0
    F2E = 1
    M1E = 2

@dataclass
class Aq10Param(BaseParam):
    base_voice: Aq10BaseVoice = Aq10BaseVoice.F1E
    accentuation: int = 100
    resonance_peak: int = 100