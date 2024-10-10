from BackEnd.src.data.database import Database
from BackEnd.src.domain.entities.arquivosProdutos import ArquivoProdutos
from BackEnd.src.domain.entities.tratamentoDados import TratamentoDados
from BackEnd.src.domain.entities.usuarios import Usuarios


class TratamentoDadosRepository():
    def __init__(self,data):
        self.Data = data
    
    def CreateDataProcessing(self):
        idArquivo = self.Data.get('idArquivo')
        tipoOP = self.Data.get('tipoOP')
        idUsuario = self.Data.get('idUsuario')
        valorFiltro = self.Data.get('valorFiltro')
        atributoModificacao = self.Data.get('atributoModificacao')
        valorModificacao = self.Data.get('valorModificacao')
        Data = Database()
        response = Data.DoSelect(ArquivoProdutos,APId=idArquivo)
        if len(response) == 0:
            return 400,'Não foi encontrado a base de dados dos produto.'
        response = Data.DoSelect(Usuarios,UsuId=idUsuario)
        if len(response) == 0:
            return 400,'Não foi encontrado o usuário.'
        
        response = Data.DoInsert(TratamentoDados,TDAtributoModificacao=atributoModificacao,TDValorModificacao=valorModificacao,TDValorFiltro=valorFiltro,TDOperacao=tipoOP,TDIdArquivoProduto=idArquivo,TDIdUsuario=idUsuario)
        if response is None:
            return 400,'Ocorreu um erro ao inserir os dados. Tente novamente.'
        
        print("Aqui cria o registro de limpeza.")
        
    def EditDataProcessing():
        print("")
        
    def ValidDataProcessing():
        print("")
        
    def StartDataProcessing(dataSet,arquivoId):
        Data = Database()
        responseArquivo = Data.DoSelect(ArquivoProdutos,APId=arquivoId)
        if len(responseArquivo) == 0:
            return False,'Não foi encontrado a base de dados dos produto.'
        responseTratamentoDados = Data.DoSelect(TratamentoDados,TDIdArquivoProduto=arquivoId)
        if len(responseTratamentoDados) == 0:
            return True,'Não existe regra de tratamento de dados ativo.'
        return True,''
    