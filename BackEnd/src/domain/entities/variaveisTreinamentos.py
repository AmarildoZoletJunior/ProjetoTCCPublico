import enum
from BackEnd.src.domain.enum.tipoDado import TipoDado
from data.base import Base
from sqlalchemy import Column, Integer, String


class VariaveisTreinamentos(Base):
    __tablename__ = 'VariaveisTreinamentos'
    VTId = Column(Integer, primary_key=True, autoincrement=True)
    VTNome = Column(String)
    VTTipoDado = Column(enum.Enum(TipoDado))
