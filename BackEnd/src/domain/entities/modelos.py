from sqlalchemy import Column, Integer, String, Date, ForeignKey, LargeBinary
from sqlalchemy.orm import relationship
from data.base import Base

# Tabela Modelos
class Modelos(Base):
    __tablename__ = 'Modelos'

    MDId = Column(Integer, primary_key=True, autoincrement=True)
    MDVersao = Column(String)
    MDArquivo = Column(LargeBinary)
    MDIdArquivoProd = Column(Integer, ForeignKey('arquivos_produtos.APId'))
    MDIdUsuario = Column(Integer, ForeignKey('usuarios.id'))
    MDDataPostagem = Column(Date)

    # Relacionamentos
    usuario = relationship('Usuarios', back_populates='Modelos')
    arquivo_produto = relationship('ArquivoProdutos', back_populates='Modelos')