
from pymailer import PyMailer
    
pymailer = PyMailer('C:/Users/Lorcan/Desktop/PYTHON TESTING/python-mailer-master/test.html' 'C:/Users/Lorcan/Desktop/PYTHON TESTING/python-mailer-master/emails.csv' 'THE-EMAIL-SUBJECT-IS-CA$H')
    
# send a test email
pymailer.send_test()
    
# send bulk mail
pymailer.send()