from BackEnd.src.domain.entities.arquivosProdutos import ArquivoProdutos
from BackEnd.src.domain.entities.parametrosTreinamentos import ParametrosTreinamento
from BackEnd.src.domain.entities.usuarios import Usuarios
from data.database import Database


class ParametrosTreinamentoRepository():
    def __init__(self,data):
        self.Data=data
        
    def CreateParametersToData(self):
        numPca = self.Data.get('numPca')
        qtdeRecomendacao = self.Data.get('qtdeRecomendacao')
        usuId = self.Data.get('usuId')
        ArquivoId = self.Data.get('arquivoId')
        
        response,message  = self.ValidParameters(numPca,qtdeRecomendacao,usuId,ArquivoId)
        if not response:
            return 400,message
        
        Data = Database()
        fileExist = Data.DoSelect(ArquivoProdutos,APId=ArquivoId)
        if len(fileExist) == 0:
            return False,'Não foi encontrado o dataset de produto neste ID.'
        
        userExist = Data.DoSelect(Usuarios,USUid=usuId)
        if len(userExist) == 0:
            return False,'O usuário não existe.'
        
        
        registerExist = Data.DoSelect(ParametrosTreinamento,APNumPca = numPca,APQtdeRecomendacoes = qtdeRecomendacao ,APIdArquivoProduto = ArquivoId)
        if len(registerExist) > 0:
            return False,'Já existe um registro com estes parâmetros de treinamento para este dataset.'
        
        response = Data.DoInsert(ParametrosTreinamento,APNumPca=numPca,APQtdeRecomendacoes=qtdeRecomendacao,APIdArquivoProduto=ArquivoId,APIdUsuario=usuId)
        if response is None:
            return 400,'Não foi possível inserir o registro. Tente novamente.'
        
        return 200,''
        
    def ModifyParametersData(self):
        idParametros = self.Data.get('idParametros')
        numPca = self.Data.get('numPca')
        qtdeRecomendacao = self.Data.get('qtdeRecomendacao')
        self.ValidParameters(numPca,qtdeRecomendacao,1,1)
        
        Data = Database()
        registerExist = Data.DoSelect(ParametrosTreinamento,APId=idParametros)
        if len(registerExist) == 0:
            return False,'Parametros não encontrado.'
        response = Data.DoUpdate(ParametrosTreinamento,APId=idParametros,APQtdeRecomendacoes=qtdeRecomendacao,APNumPca=numPca)
        if response is None:
            return False,'Ocorreu um erro ao modificar o registro. Tente novamente.'
        
        return True,''
        
    def ValidParameters(self,numPca,qtdeRecomendacao,usuId,ArquivoId):
        if not numPca:
            return False,'Parâmetro numPca é obrigatório.'
        
        if not qtdeRecomendacao:
            return False,'Parâmetro qtdeRecomendacao é obrigatório.'
        
        if not usuId:
            return False,'Parâmetro usuId é obrigatório.'
        
        if not ArquivoId:
            return False,'Parâmetro ArquivoId é obrigatório.'
        
        if qtdeRecomendacao < 0:
            return False,'Não é possível recomendar 0 camadas de itens.'
        
        return True,''