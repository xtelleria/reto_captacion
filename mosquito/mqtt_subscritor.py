import paho.mqtt.client as mqtt
import ssl

# Definir función de callback para recibir mensajes
def on_message(client, userdata, message):
    print("Mensaje recibido en el tema:", message.topic)
    print("Contenido del mensaje:", str(message.payload.decode("utf-8")))

def on_connect(client, userdata, flags, rc, d):
    if rc == 0:
        print("Conexión establecida con éxito al broker MQTT")
        # Suscribirse al tema después de la conexión
        client.subscribe("mqtt")
    else:
        print("Error de conexión al broker MQTT. Código de resultado:", rc)

# Configurar conexión MQTT con certificado
mqtt_client = mqtt.Client(mqtt.CallbackAPIVersion.VERSION2)
mqtt_client.on_connect = on_connect
mqtt_client.on_message = on_message

# Configurar TLS para confiar en el certificado del servidor
mqtt_client.tls_set(ca_certs="./certs/ca.crt", certfile="./certs/cliente.crt", keyfile="./certs/cliente.key", tls_version=ssl.PROTOCOL_TLS)

# Conectar al broker MQTT
mqtt_client.connect("172.23.0.2", 8883, 30)

# Iniciar loop para recibir mensajes
mqtt_client.loop_forever()