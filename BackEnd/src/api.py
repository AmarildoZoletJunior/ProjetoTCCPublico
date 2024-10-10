
import io
import jwt
import datetime
from functools import wraps
from flask import Flask, request, jsonify, make_response
import pandas as pd
from repositories.usuariosRepository import UserRepository

from repositories.arquivosProdutosRepository import ArquivosProdutosRepository

from Database.DataBase import Database
from Config.configuration import CHAVE


data = Database()
app = Flask(__name__)
secret = app.config['SECRET_KEY'] = CHAVE



def tokenNecessario(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        token = None
        if 'Authorization' in request.headers:
            auth_header = request.headers['Authorization']
            if auth_header.startswith("Bearer "):
                token = auth_header.split(" ")[1]
            else:
                return jsonify({'Erro': 'Formato do token inválido!'}), 401
        else:
            return jsonify({'Erro': 'Token é necessário!'}), 401

        try:
            data = jwt.decode(token, secret, algorithms=["HS256"])
            current_user = data['user_id']
        except jwt.ExpiredSignatureError:
            return jsonify({'Erro': 'Token expirado!'}), 401
        except jwt.InvalidTokenError:
            return jsonify({'Erro': 'Token inválido!'}), 401

        return f(current_user, *args, **kwargs)

    return decorated

def criarTokenJWT(user_id):
    token = jwt.encode({
        'user_id': user_id,
        'exp': datetime.datetime.utcnow() + datetime.timedelta(hours=24)
    }, app.config['SECRET_KEY'], algorithm="HS256")
    return token



@app.route("/login",methods=['POST'])
def SignInAccount():
    try:
        data = request.get_json(force=True)
        UserRep = UserRepository(data)
        response, message = UserRep.ValidUser()
        if not response:
            return jsonify({'Erro': message}), 400
        user_list = UserRep.FindUser()

        if user_list and isinstance(user_list, list) and len(user_list) > 0:
            user = user_list[0]
            user_id = user.get('USUid')
            token = criarTokenJWT(user_id)

            return jsonify({
                'Mensagem': 'Usuário encontrado com sucesso',
                'token': token
            }), 200
        else:
            return jsonify({'Erro': 'Usuário não encontrado'}), 400

    except Exception as e:
        return jsonify({'Erro': f'Ocorreu um erro, erro: {e}'}), 500
    
    
    
    
    
    
    
    
@app.route('/enviarArquivoProduto',methods=['POST'])
def UploadProductsFile():
    try:
        Arquivo = ArquivosProdutosRepository()
        response,message = Arquivo.VerifyData(request)
        if response == 400:
            return jsonify({'Erro': f'Ocorreu um erro, erro: {message}'}), 500
        response,message = Arquivo.InsertDataFile()
        if response == 400:
            return jsonify({'Erro': f'Ocorreu um erro, erro: {message}'}), 500
        return 200
    except Exception as error:
        return jsonify({'Erro': f'Ocorreu um erro, erro: {error}'}), 500
        
@app.route('/removerArquivoProduto/<int:IdArquivo>',methods=['DELETE'])
def DeleteUploadedProductsFile(IdArquivo):
    try:
        Arquivo = ArquivosProdutosRepository()
        response,message = Arquivo.RemoveFileProducts(IdArquivo)
        if response == 400:
            return jsonify({'Erro': f'Ocorreu um erro, erro: {message}'}), 400
        return 200
    except Exception as error:
        return jsonify({'Erro': f'Ocorreu um erro, erro: {error}'}), 500
        
        
        
        
@app.route('/adicionarParametroTreinamento',methods=['POST'])
def CreateTrainingParameters():
    try:
        print("")
    except Exception as error:
        return jsonify({'Erro': f'Ocorreu um erro, erro: {error}'}), 500
        
@app.route('/editarParametroTreinamento/<int:IdParametro>',methods=['PUT'])
def EditTrainingParameters(IdParametro):
    try:
        print("")
    except Exception as error:
        return jsonify({'Erro': f'Ocorreu um erro, erro: {error}'}), 500
        
@app.route('/removerParametroTreinamento/<int:IdParametro>',methods=['DELETE'])
def DeleteTrainingParameters(IdParametro):
    try:
        print("")
    except Exception as error:
        return jsonify({'Erro': f'Ocorreu um erro, erro: {error}'}), 500

@app.route('/listarTodosParametrosTreinamentos',methods=['GET'])
def ListAllTrainingParameters():
    try:
        print("")
    except Exception as error:
        return jsonify({'Erro': f'Ocorreu um erro, erro: {error}'}), 500
        
        
        
    
@app.route('/listarTodosModelos',methods=['GET'])
def ListAllTrainingModels():
    try:
        print("")
    except Exception as error:
        return jsonify({'Erro': f'Ocorreu um erro, erro: {error}'}), 500
        
@app.route('/gerarModelo/<int:IdArquivo>',methods=['POST'])
def GenerateModel(IdArquivo):
    try:
        print("")
    except Exception as error:
        return jsonify({'Erro': f'Ocorreu um erro, erro: {error}'}), 500
        
@app.route('/removerModelo/<int:IdModelo>',methods=['DELETE'])
def DeleteModel(IdModelo):
    try:
        print("")
    except Exception as error:
        return jsonify({'Erro': f'Ocorreu um erro, erro: {error}'}), 500
        
    
        
        
@app.route('/criarTratamentoDados',methods=['GET'])
def CreateDataProcessing():
    try:
        print("")
    except Exception as error:
        return jsonify({'Erro': f'Ocorreu um erro, erro: {error}'}), 500
        
@app.route('/editarTratamentoDados/<int:IdTratamento>',methods=['POST'])
def EditDataProcessing(IdTratamento):
    try:
        print("")
    except Exception as error:
        return jsonify({'Erro': f'Ocorreu um erro, erro: {error}'}), 500
        
@app.route('/removerTratamentoDados/<int:IdTratamento>',methods=['DELETE'])
def DeleteDataProcessing(IdTratamento):
    try:
        print("")
    except Exception as error:
        return jsonify({'Erro': f'Ocorreu um erro, erro: {error}'}), 500
        
        