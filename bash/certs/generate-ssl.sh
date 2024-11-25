# generating ssl certificate
openssl genrsa -des3 -out ./self-ssl.key 2048
openssl req -new -key ./self-ssl.key -out self-ssl.csr
openssl x509 -req -days 365 -in ./self-ssl.csr -signkey ./self-ssl.key -out ./self-ssl.crt