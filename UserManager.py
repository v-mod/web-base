import os.path
import os
class User:
    def __init__(self, userName, password, role):
        self.userName = userName
        self.password = password
        self.role = role
class UserManager:

    def Auth(self,userName,password):
        path = 'User-Info/'
        if os.path.isfile('User-Info/' + userName + '/'  + 'Me.txt'):
            f = open(path + userName + '/'+ 'Me.txt', 'r')
            data = f.read()
            userData = data.split(',')
            f.close()
            cpassword = userData[1]
            if cpassword == password:
                user = User(userData[0], '', userData[2])
                return { 'user': user, 'message': 'User found' }
            else:
                return{'user': None, 'message': 'Incorrect Username or Password'}
        else:
            return { 'user': None, 'message': 'Incorrect Username or Password' }
    def Signup(self, userName, password, role):
        userInfo=userName + ',' + password + ',' + role + ',LM9nwvBd7hqtRo/uIxwINeuFXF/xRWRqkOfXoGPw6RVz00EI3vM0aBI5YStpsI7kmWETt6xkz+xq6L84ZaB6yWPquSIQeWyjf3UTcAA+SO13r6EhV66Tl9geYDl7naumoCAsT2VrwYJv6yNzuL+Ux4CVRiCFnEYCVwIIykc9n1Bv8ETBnaKfFMJZc/w4P2z9dFlqxnXQWR+yugCqmbOZLl7gckovczB/7WJSYzfY/xBG6FqN+DsLOea1Yw1Fw5g+wg2gLK7aI7uw'
        os.mkdir('User-Info/'+userName)
        me = open('User-Info/'+userName+'/Me.txt', 'w')
        me.write(userInfo)
        me.close()
    def getDetails(self, userName):
        path = 'User-Info/'
        if os.path.isfile(r'User-Info/' + userName + '/'  + 'Me.txt'):
            f = open(path + userName + '/'+ 'Me.txt', 'r')
            data = f.read()
            userData = data.split(',')
            f.close()
            return userData
        else:
            return 'MALFUNC_READ_DATA: NO FILE EXIST'
    def change_password(self,uname, new_pwd):
        userData=self.getDetails(uname)
        newData=userData[0]+','+new_pwd+','+userData[2]
        data=open(r'User-Info/' + uname + '/'  + 'Me.txt','w')
        data.write(newData)
        data.close()
    
    def KeyAuth(self, userName,password):
        path = 'User-Info/'
        if os.path.isfile(r'User-Info/' + userName + '/'  + 'Me.txt'):
            f = open(path + userName + '/'+ 'Me.txt', 'r')
            data = f.read()
            userData = data.split(',')
            f.close()
            cpassword = userData[3]
            if cpassword == password:
                user = User(userData[0], '', userData[2])
                return { 'user': user, 'message': 'User found' }
            else:
                return{'user': None, 'message': 'Incorrect Username or Password'}
        else:
            return { 'user': None, 'message': 'Incorrect Username or Password' }