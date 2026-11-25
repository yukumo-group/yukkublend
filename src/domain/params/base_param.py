from dataclasses import dataclass


@dataclass
class BaseParam:
    """
    Base class for all voice synthesis parameters across engines

    :param base_preset: The integer preset for a specific engine. Preset definitions should come from the engine.
    :type base_preset: int
    :param base_pitch: The pitch for the voice
    :type base_pitch: float
    """
    base_preset: int = 0
    base_pitch: float = 1.0
