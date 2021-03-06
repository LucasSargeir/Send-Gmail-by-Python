import sys
import time
import smtplib
from email.mime.text import MIMEText
from decouple import config

if(len(sys.argv) != 3):
	print("Parametros inválidos")
	print(sys.argv[0] + "<QUANTIDADE> <REMETENTE>")
	quit()

else:
	repeat = int(sys.argv[1])
	to_email = sys.argv[2]


print("Enviando " + str(repeat) + " e-mails...")
print("")



smtp_ssl_host = 'smtp.gmail.com'
smtp_ssl_port = 465


username = config('PYTHON_APP_USER')
password = config('PYTHON_APP_PASS')


from_addr = config('USER')
to_addrs = [to_email]


message = MIMEText('Aqui vem a sua mensagem')
message['subject'] = 'Assunto'
message['from'] = from_addr
message['to'] = ', '.join(to_addrs)


server = smtplib.SMTP_SSL(smtp_ssl_host, smtp_ssl_port)


server.login(username, password)


for i in range(0, repeat):

	server.sendmail(from_addr, to_addrs, message.as_string())
	print("Enviando e-mail "+ str(i + 1))

	time.sleep(2)


server.quit()