from dataclasses import dataclass


@dataclass
class BaseParam:
    base_preset: int = 0
    base_pitch: float = 1.0
