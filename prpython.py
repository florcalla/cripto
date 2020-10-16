
from base64 import b64encode, b64decode
from Crypto.Cipher import AES
from string import Template
def crearHtml() :
	f = open('index.html','w')
	message = """<p>Este sitio contiene un mensaje secreto</p>
<div class="AES" id="$mensaje">  </div>
<div class="iv" id="$iv">  </div>"""
	f.write(message)
	f.close()
def cifrar() : 
	llave = input("ingresar llave (32 digitos) : ")
	iv = input("ingresar IV (32 digitos) : ")
	mensaje = input("ingrese mensaje : ")

	#transformar a binarios	
	llave_byte = bytearray.fromhex(llave)
	iv_byte = bytearray.fromhex(iv)

	#cifrado AES en modo OFB 
	cipher = AES.new(llave_byte, AES.MODE_OFB, iv_byte)
	ct_bytes = cipher.encrypt(mensaje.encode("utf-8"))

	print("mensaje cifrado : " ,ct_bytes.hex())

	#escribir mensaje cifrado en html  
		
	f = open('index.html')
	src = Template(f.read())
	d = { 'mensaje' : ct_bytes.hex() , 'iv' : iv}
	result = src.substitute(d)
	file = open('index.html','w')
	file.writelines(result)


crearHtml()
cifrar()
#datos
llave_hex = '58a53a92e90ca0e97fc5754ae5189f79'
iv_hex = '6a94919f3f248a22a35d50d651a4243c'
