# Phishing-Attack


-----------------------------------------------------------------------------------------------------------------------------------------

We are a group of students who simulate a phishing attack.

-----------------------------------------------------------------------------------------------------------------------------------------
We created a fake victim with a gmail account and LinkedIn with tha same password.

#### step1:
1) we created a fake login website to LinkedIn
2) we sent to the victim a fake linkedin message with the link to our website
3) The victim will enter the login information on the site
4) The details will be saved in the text file list.txt

-----------------------------------------------------------------------------------------------------------------------------------------
#### step2:
We have created a script that takes all the users saved in list.txt and tries to connect to their gmail and linkedin account.
If the login is successful the user information is saved in the gmailUsers.txt file and the LinkedInUsers.txt file .
In addition, if the connection to LinkedIn was made successfully then a post was written in the victim's account.

!!From the victim's gmail account it is already easy to recover passwords for many accounts of other apps!!


-----------------------------------------------------------------------------------------------------------------------------------------

###requirements:
selenium==3.141.0
urllib3==1.25.7