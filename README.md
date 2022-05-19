# Bienvenidos al desarrollo

Este software esta utilizando la API de Twilio para enviar **SMS** y **Whatsapp**, para poder utilizar correctamente esta demo, deberán regístrate en la plataforma [www.twilio.com](http://www.twilio.com) y terminar el proceso completo, **No requiere una tarjeta de crédito**.

# Configuración

Hay un archivo llamado **config.json**, *se genera automáticamente en caso de ser borrado*, que contiene las siguientes propiedades:
 

 - ACCOUNT_SID
 - AUTH_TOKEN
 - DEFAULT_NUMBER
 - SMS_SID
 
| Propiedad | Uso |
| -- | -- |
| ACCOUNT_SID  | Identificador de su cuenta, el cual es único y se encuentra en la pagina principal de su proyecto. |
|AUTH_TOKEN| Token de acceso y de autentificación para poder consumir los diversos servicios que la plataforma entrega. |
|DEFAULT_NUMBER| El número que se usará para enviar los WSP, que es proporcionado por la página, debe tener el siguiente formato **“whatsapp:numero”** **Solo llenar si se requiere enviar Whatsapp** |
| SMS_SID |  Identificador del número usado para enviar mensajes SMS, es dado por la plataforma **Solo llenar si se requiere enviar SMS** |

> Para obtener más información sobre las variables, le recomiendo leer la documentación oficial [Documentos de Twilio: Referencia de la API, tutoriales e integración | Twilio](https://www.twilio.com/es-mx/docs)

# Uso
Para usar el software deberá instalar las librerías necesarias que se encuentran en el archivo

    pip install -r requirements.txt

Para luego iniciar el software, con

    python main.py


Listo a enviar mensajes por whatsapp o sms :D
