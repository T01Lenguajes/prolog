import cherrypy
## Escribe Bien el Archivo
from cherrypy import expose
#decorador
from cherrypy import quickstart
from jinja2 import Environment, FileSystemLoader
env= Environment(loader=FileSystemLoader('templates'))  
#session_filter.on = True 
cherrypy.server.socket_host= 'localhost'
cherrypy.server.socket_port = 8000


class Home: # Aplicaicon root
  
    @expose()
    def index(self): # raiz del url
	 
	 tmpl=env.get_template("inicio.html")
         return tmpl.render()

    @expose()
    def  Agregar_Restaurante(self): # raiz del url
	 tmpl=env.get_template("ejempplo.html")
         return tmpl.render()

    @expose
    def Agregar_Platillo(self): # raiz del url
	 tmpl=env.get_template("platillo.html")
         return tmpl.render()
    
    @expose
    def Consulta_Platillo(self): # raiz del url
	 tmpl=env.get_template("Consultaplatillo.html")
         return tmpl.render()
	
    @expose
    def Consultas_Restaurante(self): # raiz del url
	 tmpl=env.get_template("Consultares.html")
         return tmpl.render()
	

if __name__ == "__main__":
    quickstart(Home())
