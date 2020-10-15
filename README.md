# Bot para envio de multiplos e-mails em Python

## Sobre 

Bot criado para enviar várias vezes o mesmo e-mail para um determinado remetente através do gmail.

O bot utiliza a biblioteca interna `smtplib` para fazer o envio de e-mails e a biblioteca `decouple` para acessar variáves ambientes.

## Pré Requisitos

O programa utiliza a biblioteca `decouple` para acessar as variáveis ambiente. A intalação da biblioteca pode ser feita com o comando abaixo:

```bash
pip install python-decouple
```



Agora precisamos criar o arquivo que irá guardar nossas variáveis ambientes. Elas servirão para nos conectar ao servidor do gmail.

Crie um arquivo `.env` com o conteúdo abaixo:

````
PYTHON_APP_USER=<AQUI_VOCE_COLOCA_SEU_USUARIO>
PYTHON_APP_PASS=<AQUI_VOCE_COLOCA_A_SUA_SENHA>
````

Feito isso já podemos utilizar nosso programa.

_**OBS:** não esqueça de trocar a mensagem e o assunto no código do programa_

## Utilização

Para utlizar abra o terminal na pasta do programa e rode o comando abaixo:

```bash
python3 e_mail_sender.py <QTD> <REMETENTE>
```

- `<QTD>`: número de vezes que o e-mail será enviado, ex: 1, 2, 10...
- `<REMETENTE>` : e-mail que receberá a mensagem ex: voce@hotmail.com

## Possiveis Erros

- O google por padrão não deixa que apps menos seguros acessem sua conta. Para liberar que o acesso seja feito acesse o [link](myaccount.google.com/u/0/) e selecione ativar. 

  _**Log do erro**_: `smtplib.SMTPAuthenticationError: (535, b'5.7.8 Username and Password not accepted. Learn more at\n5.7.8  https://support.google.com/mail/?p=BadCredentials [...]')`

  

- Além disso o google não permite que você encha a caixa de e-mail de uma pessoa de uma unica vez. Então quando muitos e-mail são enviados em um curto periodo de tempo ele encerra a conexão. Além disso google também possui um limite diário de e-mails que podem ser enviados, fique alerta.

  _**Log do erro**_: `smtplib.SMTPSenderRefused: (421, b'4.7.0 Try again later, closing connection. (MAIL) [...]', '<USER>')`

