import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
class Correo:
	
	def enviar(self):
		
		#NOS LOGEAMOS CON NUESTRA CUENTA DE OUTLOOK
		remitente = 'tu_correo@outlook.com'
		contraseña= 'tu_contraseña'
	
		#ESCRIBIMOS EL MENSAJE EN TEXTO PLANO
		cuerpo = 'Este es el contenido del mensaje'
		
		#LEEMOS LA LISTA DE CORREOS Y ENVIAMOS A CADA UNO
		f = open("lista.txt", "r")
		for direccion in f:
			#OBJETO MENSAJE
			mensaje = MIMEMultipart()
 
			#ESTRUCTURAMOS EL CORREO
			mensaje['From'] = remitente
			mensaje['To'] = direccion
			mensaje['Subject'] = 'Correo de prueba'



			#LO AGREGAMOS AL OBJETO
			mensaje.attach(MIMEText(cuerpo, 'plain'))

			#CONEXION AL SERVIDOR
			sesion_smtp = smtplib.SMTP('smtp-mail.outlook.com:587')
  
			#CIFRADO DE LA CONEXION
			sesion_smtp.starttls()
  
			#NOS LOGUEAMOS
			sesion_smtp.login(remitente,contraseña)

			#OBJETO A TIPO TEXTO
			texto = mensaje.as_string()

			#LO ENVIAMOS
			sesion_smtp.sendmail(remitente, direccion, texto)
			print("MENSAJE ENVIADO")
			#LOGOUT
			sesion_smtp.quit()
		f.close()
		
		
if __name__ == '__main__':
	
	
	#OBJETO
	mail=Correo()
	mail.enviar()
