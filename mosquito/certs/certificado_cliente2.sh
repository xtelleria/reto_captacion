# Función para crear un certificado de cliente
crear_certificado_cliente_2() {
    local client_name="$1"
    local ip_address="$2"  # Se agrega la dirección IP como argumento
    openssl genrsa -out "$client_name.key" 2048
    openssl req -new -key "$client_name.key" -out "$client_name.csr" -subj "/CN=$client_name"
    openssl x509 -req -in "$client_name.csr" -CA ca.crt -CAkey ca.key -CAcreateserial -out "$client_name.crt" -days 365 -extfile <(printf "subjectAltName=IP:$ip_address")
    echo "Certificado de cliente $client_name creado exitosamente."
}

crear_certificado_cliente_2 "cliente2" "172.23.0.2"