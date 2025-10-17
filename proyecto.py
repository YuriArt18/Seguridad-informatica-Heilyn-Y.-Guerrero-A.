import hashlib
texto = input("Ingrese un texto: ")
resultado = hashlib.md5(texto.encode())
print("MD5:", resultado.hexdigest())

import hashlib
texto = input("Ingrese un texto: ")
resultado = hashlib.sha1(texto.encode())
print("SHA-1:", resultado.hexdigest())

import hashlib
texto = input("Ingrese un texto: ")
resultado = hashlib.sha256(texto.encode())
print("SHA-256:", resultado.hexdigest())

import hashlib
texto = input("Ingrese un texto: ")
resultado = hashlib.sha3_256(texto.encode())
print("SHA-3 (256 bits):", resultado.hexdigest())

import hmac
import hashlib
clave = b"clave_secreta"
mensaje = input("Ingrese un mensaje: ").encode()
resultado = hmac.new(clave, mensaje, hashlib.sha256)
print("HMAC (SHA-256):", resultado.hexdigest())