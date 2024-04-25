import reflex as rx
from typing import Optional
from sqlmodel import Field

class AlertasCalidad(rx.Model, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    CodArticolo: str
    RisorseAvvisoQualita: str
    MotivazioneAvvisoQualita: str
