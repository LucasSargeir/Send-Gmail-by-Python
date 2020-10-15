import sys
import smtplib
from email.mime.text import MIMEText
from decouple import config

# verifica se foi passada a quatidade
if(len(sys.argv) != 2):
	print ("Passe o numero de repeticoes que deseja fazer")
	quit()

else:
	repeticoes = int(sys.argv[1])

print("Enviando " + str(repeticoes) + " e-mails...")

# conexão com os servidores do google
smtp_ssl_host = 'smtp.gmail.com'
smtp_ssl_port = 465

# username ou email para logar no servidor
username = '<usuario>'
password = '<senha>'

from_addr = '<email_de>'
to_addrs = ['<e-mail_para']

# usa o MIME Text para enviar somente texto
message = MIMEText('Aqui vem a sua mensagem')
message['subject'] = 'Assunto'
message['from'] = from_addr
message['to'] = ', '.join(to_addrs)

# conecta de forma segura usando SSL
server = smtplib.SMTP_SSL(smtp_ssl_host, smtp_ssl_port)

# faz login no servidor externo
server.login(username, password)

# faz o envio do e-mail
for i in range(0, repeticoes):
	server.sendmail(from_addr, to_addrs, message.as_string())
	print("Enviando e-mail "+ str(i))

server.quit()