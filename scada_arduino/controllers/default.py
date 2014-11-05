
import serial
import time
puerto_Serie=serial.Serial('/dev/ttyACM0', 115200,timeout=2)
puerto_Serie.close()
puerto_Serie.open()

def index():
    
    response.flash = T("Welcome to web2py!")
    return dict(message=T('Hello World'))
    
import pdb
  
def recibe_datos():
	cadena=""
	recibe=[]
	valor=str(request.vars.valor)
	
	#pdb.set_trace()

	if (valor=='1'):
		
		cadena='a'
	if (valor=='0'):
		
		cadena='b'
	
	
	puerto_Serie.write(cadena)
	if puerto_Serie.inWaiting() > 0:
		recibe = puerto_Serie.readline()
		recibe_puerta=recibe[8]
		recibe_term=recibe[16:]
		
		resultado = {"Puerta":recibe_puerta, "Termometro":int(recibe_term)}
	
	return resultado
	time.sleep(0.1) 
	
	
def user():
    
    return dict(form=auth())
@cache.action()
def download():
    
    return response.download(request, db)
def call():
    
    return service()
@auth.requires_login() 
def api():
    
    from gluon.contrib.hypermedia import Collection
    rules = {
        '<tablename>': {'GET':{},'POST':{},'PUT':{},'DELETE':{}},
        }
    return Collection(db).process(request,response,rules)
