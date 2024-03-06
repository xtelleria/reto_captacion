import ssl
import paho.mqtt.publish as publish
import paho.mqtt.client as mqtt

# Configuración de certificados
ca_cert = "./certs/ca.crt"
client_cert = "./certs/cliente.crt"
client_key = "./certs/cliente.key"

# Configuración de mensajes a publicar
topic = "mqtt"
mensaje = "Hola, soy el cliente 1"

# Publicar mensaje
publish.single(topic, mensaje, hostname="172.23.0.2", port=8883, client_id="", auth=None, tls={'ca_certs': ca_cert, 'certfile': client_cert, 'keyfile': client_key}, protocol=mqtt.MQTTv311)