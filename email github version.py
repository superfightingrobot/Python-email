import smtplib, ssl                             #Import of the SMTP library and import of the SSL library, SSL may be required on some email platforms.

server = smtplib.SMTP('IP address', port number)        #SMTP Server address and port number 
server.sendmail(                                #This is the send mail tag   
  "Test@gmail.com",                     #From email, this can be anything technically 
  "Randomdude@gmail.com",                   #The recipient email 
  "Test to Random Dude via Python")            #Reserved for message 
server.quit()                                   #Tells the program to log off after sending
print ("email sent successfully")               #Print statement can be any message