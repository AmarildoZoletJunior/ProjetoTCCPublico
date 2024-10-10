import re
from data.database import Database
from domain.entities.usuarios import Usuarios


class UserRepository():
    def __init__(self,Data):
        self.Data = Data
        self.pattern = r"^(?=.*[0-9])(?=.*[!@#$%^&*(),.?\":{}|<>])(?=.*[A-Z])(?=.*[a-z]).+$"

    def ValidUser(self):
        login = self.Data.get('login')
        password = self.Data.get('password')
        if not login:
            return False,'Usuário não é válido.'
        if not password:
            return False,'Senha não é válida.'
        self.login = login
        self.password = password
        return True,''
    
    def FindUser(self):
        Data = Database()
        resultado  = Data.DoSelect(Usuarios,USUsername = self.login,USUpassword = self.password)
        return resultado
        
        
    def FindUsername(self,login):
        Data = Database()
        resultado  = Data.DoSelect(Usuarios,USUsername = login)
        if len(resultado) > 0:
            return True
        else:
            return False
        
    def CreateUser(self):
        response,message = self.ValidUserRegister()
        if not response:
            return 400,message
        Data = Database()
        response = Data.DoSelect(Usuarios,USUsername=self.login)
        if len(response) > 0:
            return 400,'Já existe um usuário com este nome'
        response = Data.DoInsert(Usuarios,USUsername=self.login,USUpassword=self.password)
        if response is None:
            return 400,'Ocorreu um erro ao gravar registro, tente novamente.'
        else:
            return 200,'Registro gravado com sucesso.'
        
    def ValidUserRegister(self):
        login = self.Data.get('login')
        password = self.Data.get('password')
        if not login:
            return False,'Usuário não pode ser nulo.'
        if len(login) < 4:
            return False,'Usuário não pode ter menos de 4 caracteres.'
        response = self.FindUsername(login)
        if response:
            return False,'Usuário não pode ser cadastrado pois já existe outra conta com o mesmo usuário.'
        response,message = self.ValidPassword(password)
        if not response:
            return False,message
        self.login = login
        self.password = password
        return True,''
    
    def ValidPassword(self,password):
        if not password:
            return False,'Senha não é válida.'
        if len(password) < 4:
            return False,'Senha não pode conter menos de 4 caracteres.'
        match = re.match(self.pattern, password)
        if not match:
            return False,'Senha não contém os caracteres necessários.'
        return True,''
    
    def ResetPassword(self):
        self.login = self.Data.get('login')
        self.password = self.Data.get('password')
        newPassword = self.Data.get('newPassword')
        response = self.FindUsername(self.login)
        if not response:
            return 400,'Usuário não encontrado.'
        response = self.FindUser()
        if not response:
            return 400,'Senha incorreta.'
        response,message = self.ValidPassword(newPassword)
        if not response:
            return 400,message
        Data = Database()
        response = Data.DoUpdate(Usuarios,{"USUsername":self.login,"USUpassword":self.password},{"USUpassword":newPassword})
        if response is None:
            return 400,'Ocorreu um erro ao alterar registro. Tente novamente'
        else:
            return 200,'Registro modificado com sucesso.'
        
        
    def FindUserById(self,idUsuario):
        Data = Database()
        response = Data.DoSelect(Usuarios,USUid=idUsuario)
        if len(response) > 0:
            return 200,''
        else:
            return 400,'Usuário não encontrado.'
        