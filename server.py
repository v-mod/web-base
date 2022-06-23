# Importing flask and neccesary items
from flask import Flask, session, redirect, render_template
import UserManager as UM
# Constructing app
app = Flask(__name__)
# Secret Key setup
app.secret_key='AAAAB3NzaC1yc2EAAAABJQAAAQEAvI+0heuc2jKKSiaUEMTay7xsOhEOwapBsosHgo8jFbiELcXB1gwtELKmiLdkFRoowBb2Ga1VRJVtgeLtetM4FYu7xbRtoQB/E3tbnAJbiMy4pUCGMeI2lIFTFL0vWHGsqH/5qdoXu0dFijfdyxqvj/F5SZH7vpIXNZJu9Nvsr4UEnDWl16ndcVHsel1aMdW93I2OGLpEf8yvMR+Lq7ugVldUu2dC3FJMbZ4OkQiafDqA4ulLKk1SFRC0SsFlhIm/7XZVua4ckxEYdFRAn5NIC76ARyQUBANhIHhGkdApHm4m6ykhtozEPVagjIsNtuaZKFqOESL3ltIotHIHar/HL4Q'
# Creating an instance of UserManager
userManager = UM.UserManager()
# Setting variables
userInfo = None
userName = None

# Index
@app.route('/')
def index():
    if 'UserId' in session:
        userId = session['UserId']
        return render_template('home.html', userId=userId)
    else:
        userId= ''
        return render_template('home.html', userId=userId)


# Login/Logout/Signup/Profiles
@app.route('/login')
@app.route('/auth/login')
def login():
    return render_template('login.html')
@app.route('/logout')
@app.route('/auth/logout')
def logout():
    userInfo=None
    session.pop('UserId', None)
    return render_template('logout.html')
@app.route('/service/auth', methods=['POST']) 
def auth_service():
    UserId = request.form['uname']
    Pwd = request.form['psw']
    print(UserId,Pwd)
    res = userManager.Auth(UserId, Pwd)
    userInfo = res['user'] 
    if userInfo != None:    
        userName=UserId
        session['UserId'] = UserId
        userData = userManager.getDetails(UserId)
        session['role'] = userData[2]
        return redirect(url_for('index'))     
    else:   
        return redirect(url_for('login'))
@app.route('/auth/signup/<signup_key>')
def signup(signup_key):
    keys=open(r'User-Info/signup_keys.keys', 'r')
    signup_keys=keys.read()
    keys.close()
    if signup_key in signup_keys:
        return render_template('signup.html')
    else:
        return render_template('access_denied.html')
@app.route('/service/signup', methods=['POST'])
def signup_service():
    userName=request.form['userName']
    password=request.form['pwd']
    userManager.Signup(userName, password,'teacher')
    return redirect('/auth/login')
@app.route('/service/auth/password',methods=['POST'])
def change_password():
    newpassword=request.form['psw']
    userManager.change_password(session['UserId'] ,newpassword)
    return redirect('/')
@app.route('/profile')
def profile():
    return render_template('editPwd.html')

if __name__ == "__main__":
    app.run()
