from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from data.base import Base
from sqlalchemy import Column, DateTime, Integer, String
from sqlalchemy.sql import func

# Tabela Usuarios
class Usuarios(Base):
    __tablename__ = 'Usuarios'
    USUid = Column(Integer, primary_key=True, autoincrement=True)
    USUsername = Column(String)
    USUpassword = Column(String)
    USUcreated_at = Column(DateTime, server_default=func.now(), onupdate=func.now(), nullable=False)

    
    # Relacionamentos
    modelos = relationship('Modelos', back_populates='Usuarios')
    arquivos_produtos = relationship('ArquivoProdutos', back_populates='Usuarios')
    parametros_treinamentos = relationship('ParametrosTreinamento', back_populates='Usuarios')
    tratamentos_dados = relationship('TratamentoDados', back_populates='Usuarios')
