import smtplib
import random

server = smtplib.SMTP('smtp.gmail.com',587)
server.starttls()
server.login('py5303011@gmail.com', 'vglgxyoepvexbhjp')
otp = ''.join([str(random.randint(0,9))for i in range(6)])
message = "hello youtr otp is"+ str(otp)
server.sendmail('py5303011@gmail.com','py5303011@bbdu.ac.in', message)
server.quit()

abc = input("enter the otp send to your email:")
if otp ==abc:
    print("login successful")
else:
     print("invalid otp")
     
     
     
