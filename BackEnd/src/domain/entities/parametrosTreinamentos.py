from sqlalchemy import Column, Integer, ForeignKey
from sqlalchemy.orm import relationship
from data.base import Base


# Tabela ParametrosTreinamentos
class ParametrosTreinamento(Base):
    __tablename__ = 'ParametrosTreinamento'

    APId = Column(Integer, primary_key=True, autoincrement=True)
    APNumPca = Column(Integer)
    APQtdeRecomendacoes = Column(Integer)
    APIdArquivoProduto = Column(Integer, ForeignKey('arquivos_produtos.APId'))
    APIdUsuario = Column(Integer, ForeignKey('usuarios.id'))

    # Relacionamentos
    arquivo_produto = relationship('ArquivoProdutos', back_populates='ParametrosTreinamento')
    usuario = relationship('Usuarios', back_populates='ParametrosTreinamento')