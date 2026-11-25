from dataclasses import dataclass

from .base_param import BaseParam

@dataclass
class Aq2Param(BaseParam):
    phont_data: bytes = b""