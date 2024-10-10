import datetime
import io
import pandas as pd
from data.database import Database

from domain.entities.arquivosProdutos import ArquivoProdutos
from repositories.usuariosRepository import UserRepository

class ArquivosProdutosRepository(): 
    def __init__(self,request):
        self.request = request
        self.ArquivoCSV = None
        self.ConteudoArquivo = None
        
    def InsertDataFile(self):
        versao = self.request.form.get('versao')
        idUsuario = self.request.form.get('idUsuario')
        delimiter = self.request.form.get('delimiter')
        
        response,message = self.VerifyData(self.request,delimiter,idUsuario,versao)
        if response == 400:
            return response,message
        
        
        Data= Database()
        response = Data.DoSelect(ArquivoProdutos,APVersao=versao)
        if len(response) > 0:
            return 400,'Já existe um arquivo com esta versão.'
        
        UserRepo = UserRepository()
        response,message = UserRepo.FindUserById(idUsuario)
        if response == 400:
            return response,message
        
        
        file_content = self.ConteudoArquivo.stream.read()
        
        Data = Database()
        response = Data.DoInsert(ArquivoProdutos,ApQtdeProdutos=int(len(self.ArquivoCSV)),ApDataPostagem = datetime.date,ApArquivo = file_content,ApIdUsuario = idUsuario ,ApVersao = versao)
        if response is None:
            return 400,'Ocorreu um erro ao inserir o registro, tente novamente.'
        
        return 200,''
        
        
    def VerifyData(self,request,delimiter,idUsuario,versao):
        try:
            if 'file' not in request.files:
                return 400,'Nenhum arquivo enviado.'
            
            file = request.files['file']
            if file.filename == '':
                return 400, 'Nenhum nome de arquivo enviado.'
            
            if not file.filename.endswith('.csv'):
                return 400,'O arquivo não é CSV.'
            
            csv_data = pd.read_csv(io.StringIO(file.stream.read().decode('ISO-8859-1')), delimiter=delimiter)
            if len(csv_data) < 4:
                return 400, 'O arquivo não contém os registros mínimos necessários que são 4.'
            
            if not delimiter:
                return 400,'Parâmetro delimiter é obrigatório'
            
            if not idUsuario:
                return 400,'Parâmetro idUsuario é obrigatório'
            
            if not versao:
                return 400,'Parâmetro versao é obrigatório'
            
            self.ArquivoCSV = csv_data
            self.ConteudoArquivo = file
            
            return 200,''
        except Exception as error:
            return 400,error
        
        
        
    def RemoveFileProducts(idArquivo):
        if not idArquivo:
            return 400,'Id de arquivo inválido.'
        Data= Database()
        response = Data.DoSelect(ArquivoProdutos,APId=idArquivo)
        if len(response) == 0:
            return 400,'Arquivo não encontrado.'
        response = Data.DoDelete(ArquivoProdutos,APId=idArquivo)
        if response is None:
            return 400,'Arquivo não encontrado.'
        return 200,''
