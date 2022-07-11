import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
 

class Correo:
	
	def enviar(self):
	
		remitente = 'TUCORREO@outlook.com'
		contrasena = 'TU_CONTRASEÑA'
		
		asunto = 'CORREO DE PRUEBA'
		cuerpo = 'EL CONTENIDO DE EL MENSAJE'
		ruta_adjunto = 'x.jpg'
		nombre_adjunto = 'x.jpg'

		f = open("lista.txt", "r")
		for direccion in f:
			mensaje = MIMEMultipart()
			mensaje['From'] = remitente
			mensaje['To'] = direccion
			mensaje['Subject'] = asunto
			mensaje.attach(MIMEText(cuerpo, 'plain'))
			archivo_adjunto = open(ruta_adjunto, 'rb')
			adjunto_MIME = MIMEBase('application', 'octet-stream')
			adjunto_MIME.set_payload((archivo_adjunto).read())
			encoders.encode_base64(adjunto_MIME)
			adjunto_MIME.add_header('Content-Disposition', "attachment; filename= %s" % nombre_adjunto)
			mensaje.attach(adjunto_MIME)
			sesion_smtp = smtplib.SMTP('smtp-mail.outlook.com:587')
			sesion_smtp.starttls()
			sesion_smtp.login(remitente,contrasena)
			texto = mensaje.as_string()
			sesion_smtp.sendmail(remitente, direccion, texto)
			print("MENSAJE ADJUNTO ENVIADO")
			sesion_smtp.quit()
			
		f.close()


if __name__ == '__main__':
	mail=Correo()
	mail.enviar()
