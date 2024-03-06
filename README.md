### README: Configuración de MQTT con TLS y Docker Compose

Este README proporciona instrucciones paso a paso para configurar un servidor MQTT con seguridad TLS utilizando Docker Compose y la biblioteca `paho-mqtt` en Python.

### Pasos a seguir:

#### 1. Instalar la biblioteca paho-mqtt

pip install paho-mqtt

#### 2. Crear el archivo docker-compose.yml sin certificados

#### 3. Configurar el archivo mosquitto.conf
Agregar configuraciones adicionales para MQTT según sea necesario.

#### 4. Crear archivos Python
Crear archivos Python para la publicación y suscripción a los temas MQTT.

#### 5. Probar el funcionamiento sin TLS
Asegúrate de que el servidor MQTT está funcionando correctamente sin TLS ejecutando los scripts Python.

#### 6. Crear certificados CA, servidor y cliente
Generar certificados para la autoridad de certificación (CA), el servidor MQTT y los clientes.

#### 7. Actualizar docker-compose.yml con certificados y puerto 8883

#### 8. Configurar mosquitto.conf
Modificar el archivo mosquitto.conf para habilitar la seguridad TLS.

#### 9. Modificar archivos Python
Actualizar los scripts Python para utilizar TLS, dirección IP y puerto adecuados.

#### 10. Probar el funcionamiento con TLS
Verificar que el servidor MQTT está funcionando correctamente con TLS utilizando comandos MQTT y ejecutando los scripts Python.

### INSTRUCCIONES DE USO

#### 1. Iniciar servicios:

#####  docker-compose up -d
Este comando inicia los servicios definidos en su archivo docker-compose.yml.

#### 2. Verificar servicios en ejecución:

##### docker-compose ps
Este comando muestra una lista de todos los contenedores creados por Docker Compose, incluyendo su estado (ejecutandose, detenido, etc.).

#### 3. Ejecutar scripts de publicación y suscripción:

##### python3 mqtt_subscritor.py
##### python3 mqtt_publicador.py
##### python3 mqtt_publicador2.py
Suponiendo que tiene scripts de Python con estos nombres que interactúan con el broker MQTT, ejecútelos para simular la comunicación del cliente.

#### 4. Verificación manual utilizando comandos:

##### mosquitto_pub -h 172.23.0.2 -p 8883 -t "mqtt" -m "Soy el cliente 1" --cafile certs/ca.crt --cert certs/cliente.crt --key certs/cliente.key
Suscribirse y recibir mensaje (en otro terminal):
##### mosquitto_sub -h 172.23.0.2 -p 8883 -t "mqtt" --cafile certs/ca.crt --cert certs/cliente.crt --key certs/cliente.key -v
Estos comandos permiten la publicación y suscripción manual de mensajes al broker MQTT utilizando TLS. Si la configuración es correcta, el suscriptor debería recibir el mensaje publicado.

Nota:

Reemplace los valores como 172.23.0.2 y las rutas de archivos con los específicos de su configuración.

### Posibles vias de mejora
El protocolo MQTT ofrece tres niveles de Calidad de Servicio (QoS) para la entrega de mensajes, que determinan la fiabilidad de la entrega a costa de rendimiento:

- QoS 0 (Máximo una vez): Los mensajes se transmiten "al vuelo" sin garantías. Puede que el mensaje llegue, se duplique o se pierda. Se utiliza para situaciones donde la pérdida ocasional de datos no es crítica.

- QoS 1 (Al menos una vez): El emisor reenvía el mensaje hasta recibir una confirmación del receptor (PUBACK). Garantiza la entrega al menos una vez, pero existe la posibilidad de mensajes duplicados. Se utiliza cuando la pérdida de datos es tolerable, pero se requiere garantizar la entrega al menos una vez.

- QoS 2 (Exactamente una vez): Ofrece la entrega garantizada de un mensaje exactamente una vez. Se utiliza en escenarios donde la pérdida o duplicación de datos es inaceptable. Es el nivel de QoS más lento y complejo.

La elección del nivel de QoS apropiado depende de los requisitos específicos de su aplicación. Si la fiabilidad de la entrega es crítica, use QoS 1 o 2. Si la velocidad y el uso de recursos son prioridades, QoS 0 puede ser suficiente.

### Retos encontrados

#### 1. Encontrar la dirección IP correcta:  
##### docker inspect -f '{{range .NetworkSettings.Networks}}{{.IPAddress}}{{end}}' mqtt-broker
#### 2. SAN
##### Encontrar información sobre SAN

### Alternativas posibles

MQTT con Mosquitto es un protocolo de mensajería ligero diseñado para dispositivos IoT y sistemas de monitorización, ofreciendo una comunicación eficiente y de baja sobrecarga a través de un modelo de publicación/suscripción. Por otro lado, AMQP con RabbitMQ es más flexible y adecuado para aplicaciones empresariales, proporcionando un modelo avanzado de colas de mensajes, intercambios y enrutamiento, junto con características como enrutamiento de mensajes, colas de mensajes persistentes y confirmaciones de entrega para una comunicación más robusta y escalable entre diferentes componentes de software.

#### Autor: Xabier Telleria Salegi
