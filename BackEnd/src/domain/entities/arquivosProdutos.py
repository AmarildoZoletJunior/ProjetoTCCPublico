from sqlalchemy import Column, Integer, String, Date, ForeignKey, LargeBinary
from sqlalchemy.orm import relationship
from data.base import Base

# Tabela ArquivoProdutos
class ArquivoProdutos(Base):
    __tablename__ = 'ArquivosProdutos'

    APId = Column(Integer, primary_key=True, autoincrement=True)
    APQtdeProdutos = Column(Integer)
    APDataPostagem = Column(Date)
    APArquivo = Column(LargeBinary)
    APIdUsuario = Column(Integer, ForeignKey('usuarios.id'))
    APVersao = Column(String)

    # Relacionamentos
    usuario = relationship('Usuarios', back_populates='ArquivosProdutos')
    modelos = relationship('Modelos', back_populates='arquiArquivosProdutosvo_produto')
    parametros_treinamentos = relationship('ParametroTreinamentos', back_populates='ArquivosProdutos')
    tratamentos_dados = relationship('TratamentoDados', back_populates='ArquivosProdutos')