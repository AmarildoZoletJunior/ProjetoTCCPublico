import enum
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from data.base import Base
from domain.enum.Operacao import OperacaoEnum


# Tabela TratamentoDados
class TratamentoDados(Base):
    __tablename__ = 'TratamentoDados'

    TDId = Column(Integer, primary_key=True, autoincrement=True)
    TDAtributoModificacao = Column(String)
    TDValorModificacao = Column(String)
    TDValorFiltro = Column(String)
    TDOperacao = Column(enum.Enum(OperacaoEnum))  # Alterado para usar Enum
    TDIdArquivoProduto = Column(Integer, ForeignKey('arquivos_produtos.APId'))
    TDIdUsuario = Column(Integer, ForeignKey('usuarios.id'))

    # Relacionamentos
    arquivo_produto = relationship('ArquivoProdutos', back_populates='TratamentoDados')
    usuario = relationship('Usuarios', back_populates='TratamentoDados')
    

    
    

