from pyswip import*
prolog= Prolog()

def crear_Archivo():
	archi=open('Archivito.pl','a')
	print ("HOla")
	archi.close()

#********************************************************************************************************************************************************	

#funcion que crea el archivo donde iran almacenada la informacion de los platillos de cada restaurante

def crear_Archivo2():
	archi=open('Platillos.pl','a')
	#print ("HOla")
	archi.close()

#**************************************************************************************************************
# Se encarga de escribir en un archivo los datos del restaurante que agrega el usuario 

def escribir_Archivo(): 
	print("Datos del restaurante")
	Nombre=input("Ingrese el nombre del restaurante:")
	Tipo_Comida=input("Ingrese el tipo de comida del restaurante:")
	Ubicacion= input("Ingrese la ubicacion del restaurante:")
	Telefono=input("Ingrese el telefono del restaurante:")
	Horario= input("Ingrese el horario del restaurante:")	

	Archivito=open('Archivito.pl','a')
	Archivito.write(Nombre + "," + Tipo_Comida + "," + Ubicacion + ","+ Telefono + "," + Horario )
	Archivito.write("\n")
	Archivito.close()

#***********************************************************************************************

#funcion que escribe los datos del platillo en el archivo Platillos.pl

def escribir_Archivo2():
 
	print("Datos del platillo")
	print("\n")
	Restaurante=raw_input("Ingrese el nombre del restaurante:")
	Platillo=raw_input("Ingrese el nombre del platillo:")
	Sabor= raw_input("Ingrese el sabor del platillo (picante /salado /dulce /agridulce /amargo):")
	Pais_origen=raw_input("Ingrese el pais de origen del platillo:")
	Ingredientes=raw_input("Ingrese los ingredientes del platillo:")	

	Platillos=open('Platillos.pl','a')
	Platillos.write(Restaurante + "," + Platillo + "," + Sabor + ","+ Pais_origen + "," + Ingredientes )
	Platillos.write("\n")
	Platillos.close()




#***********************************************************************************************
# Se encarga de leer el archivo en donde se encuentran los datos del restaurante ingresado 

def leer_Archivo():

    archi=open('Archivito.pl','r')
    lista=[]
    linea=archi.readlines() # Lista que contiene todas las lineas del archivo.    

    for li in linea:

 
	elimina=li.strip("\n") # elimina el salto de linea 
	y=elimina
	#print("HOla" + y)
	lista= lista + [lista.append([str(y)])]
	#print(li)
     
    archi.close()
    lista= filter(None,lista)	
    #x=len(lista)
    #print(x)
   # print (lista)
    return lista

#************************************************************************************************
#funcion que lee el archivo donde estan los platillos e ingresa cada linea del archivo en una lista, devuelve una lista con sublistas

def leer_Archivo2():

    archi=open('Platillos.pl','r')
    lista=[]
    linea=archi.readlines() # Lista que contiene todas las lineas del archivo.    

    for li in linea:

 
	elimina=li.strip("\n") # elimina el salto de linea 
	y=elimina
	#print("HOla" + y)
	lista= lista + [lista.append([str(y)])]
	#print(li)
     
    archi.close()
    lista= filter(None,lista) #elimina el NONE
    #x=len(lista)
    #print(x)
   # print (lista)
    return lista


#***************************************************************************************************
# Se encarga de realizar la consulta de los restaurantes  

def  consulta_restaurantes():   	    

  contador=0
  lista=leer_Archivo()
  largo= len(lista)	
 # print(lista)
  while (contador < largo): # Recorre la lista principal/ la que recibe

	lista_restaurantes=lista[contador] #tiene a listita

	lista_restaurantesFinal= lista_restaurantes[0].split(",") #tiene a listita conlos strings separados

	print(lista_restaurantesFinal)

	Nombre=lista_restaurantesFinal[0]
	print("EL nombre es: " + Nombre)
	Tipo_Comida=lista_restaurantesFinal[1]
	Ubicacion=lista_restaurantesFinal[2]
	Telefono=lista_restaurantesFinal[3]
	Horario=lista_restaurantesFinal[4]
	
	linea="restaurante("+Nombre+","+Tipo_Comida+","+Ubicacion+","+Telefono+","+Horario+")" #son los hechos q van a ir en la BC

	linea2="restaurante("+"X"+","+Tipo_Comida+","+Ubicacion+","+Telefono+","+Horario+")" #busca por nombre de restaurante
	     	
	prolog.assertz(linea) #agrega a la BC
        contador= contador + 1 


  list(prolog.query(linea2)) #enlista la consulta

  for soln in prolog.query("restaurante(X,Y,Z,D,C)"): #realiza la consulta
	
	print("Si sirvio")
	print "Nombre restaurante:" , soln["X"] 


#*********************************************************************************************************************

# Lista de Restaurantes filtrados por tipo de comida 

def Consulta_Tipo_Comida(): 
	Tipo_Comida_Ingresada=raw_input("Ingrese el tipo de comida para realizar la consulta:")
	contador=0
	lista=leer_Archivo()
	largo= len(lista)	
	 # print(lista)
	while (contador < largo): # Recorre la lista principal/ la que recibe

		lista_restaurantes=lista[contador] #tiene a listita

		lista_restaurantesFinal= lista_restaurantes[0].split(",") #tiene a listita conlos strings separados

		#print(lista_restaurantesFinal)

		Nombre=lista_restaurantesFinal[0]
		#print("EL nombre es: " + Nombre)
		Tipo_Comida=lista_restaurantesFinal[1]
		Ubicacion=lista_restaurantesFinal[2]
		Telefono=lista_restaurantesFinal[3]
		Horario=lista_restaurantesFinal[4]
		
		prolog.assertz("comida(X,A):-restaurante(A,X,_,_,_)")
	        linea="restaurante("+Nombre+","+Tipo_Comida+","+Ubicacion+","+Telefono+","+Horario+")" #son los hechos q van a ir en la BC
		prolog.assertz(linea) #agrega a la BC
		linea2= "comida(X,A)"
		X= Tipo_Comida_Ingresada
        	contador= contador + 1 


	list(prolog.query(linea2)) #enlista la consulta
		
	for soln in prolog.query("comida("+ X + "," +"A"+")"):	
		
		print "Nombre restaurante:" , soln["A"] 
	

#******************************************************************************************

#realiza la la busqueda de restaurantes por nombre

def  consulta_restaurantes_por_nombre():   	    

  Restaurante_Ingresado=raw_input("Ingrese el nombre del resturante para realizar la consulta:")
  contador=0
  lista=leer_Archivo() #lista que tiene las listitas en las cuales estan las lineas del archivo
  largo= len(lista)	


  #en este bucle se forman las reglas y hechos que iran en la base de conocimientos

  while (contador < largo): # Recorre la lista principal/ la que recibe

	lista_restaurantes=lista[contador] #tiene a listita

	lista_restaurantesFinal= lista_restaurantes[0].split(",") #tiene a listita con los strings separados

	#cada uno de los parametros que iran en el hecho restaurante 

	Nombre=lista_restaurantesFinal[0]
	Tipo_Comida=lista_restaurantesFinal[1]
	Ubicacion=lista_restaurantesFinal[2]
	Telefono=lista_restaurantesFinal[3]
	Horario=lista_restaurantesFinal[4]
	
	#linea es el hecho que ira en la base de conocimientos
	
	linea="restaurante("+Nombre+","+Tipo_Comida+","+Ubicacion+","+Telefono+","+Horario+")"
	     	
	prolog.assertz(linea) #ingresa cada hecho en la base de conocimientos
	
        contador= contador + 1 
	linea2="restaurante("+"A"+","+"B"+","+"C"+","+"D"+","+"E"+")"
	A= Restaurante_Ingresado

  list(prolog.query(linea2)) #se enlista la regla 
 
  #ciclo que que busca si el restaurante ingresado se encuentra en la base de conocimientos

  for soln in prolog.query("restaurante("+ A + "," +"B"+ "," + "C" + "," + "D" + "," + "E)"): 
	
	#print("Si sirvio")
	print "El restaurante si se encuentra"  #indica si el restaurante se encuentra en la base de conocimientos

#***************************************************************************************************

#Consulta: Lista de platillos de un restaurante especifico

def  platillos_rest_especifico():   	    

  Restaurante_Ingresado=raw_input("Ingrese el nombre del resturante para realizar la consulta:")	
  contador=0
  lista=leer_Archivo() #lista que tiene las listitas en las cuales estan las lineas del archivo
  lista2=leer_Archivo2()
  largo= len(lista)	
 # print(lista)

  #en este bucle se forman las reglas y hechos que iran en la base de conocimientos

  while (contador < largo): # Recorre la lista principal/ la que recibe

	lista_restaurantes=lista[contador] #tiene a listita

	lista_restaurantesFinal= lista_restaurantes[0].split(",") #tiene a listita con los strings separados

	#cada uno de los parametros que iran en el hecho restaurante 

	Nombre=lista_restaurantesFinal[0]
	Tipo_Comida=lista_restaurantesFinal[1]
	Ubicacion=lista_restaurantesFinal[2]
	Telefono=lista_restaurantesFinal[3]
	Horario=lista_restaurantesFinal[4]
	
	#linea es el hecho que ira en la base de conocimientos
	
	linea="restaurante("+Nombre+","+Tipo_Comida+","+Ubicacion+","+Telefono+","+Horario+")"

	     	
	prolog.assertz(linea) #ingresa cada hecho en la base de conocimientos
	
        contador= contador + 1 

  contador=0
  largo=len(lista2)

  while (contador < largo): # Recorre la lista principal/ la que recibe

	lista_platillos=lista2[contador] #tiene a listita

	lista_platillos_final= lista_platillos[0].split(",") #tiene a listita con los strings separados

	i=len(lista_platillos_final)

	contador2=4
	
	Ingredientes=[]

	#cada uno de los parametros que iran en el hecho restaurante 

	Restaurante=lista_platillos_final[0]
	#print("EL nombre es: " + Nombre)
	Platillo=lista_platillos_final[1]
	Sabor=lista_platillos_final[2]
	Pais_Origen=lista_platillos_final[3]

	#ciclo en donde se almacenan los ingredientes en una lista

	while contador2!=i:
		
		Ingredientes= Ingredientes + [Ingredientes.append(str(lista_platillos_final[contador2]))]
		contador2=contador2+1
	
	#linea es el hecho que ira en la base de conocimientos
 
        Ingredientes= filter(None,Ingredientes) #elimina el NONE
	str1 = ','.join(Ingredientes) #convierte una lista a string y separa cada elemento por ","
	#print(str1)
	
	linea="nombre_platillo("+Restaurante+","+Platillo+","+Sabor+","+Pais_Origen+","+"["+str1+"]"+")"
	
	
        #print linea

	#linea2="restaurante("+"A"+","+"B"+","+"C"+","+"D"+","+"E"+")"
	     	
	prolog.assertz(linea) #ingresa cada hecho en la base de conocimientos
	
        contador= contador + 1 
	A= Restaurante_Ingresado
 
 
  prolog.assertz("platillos(A,B):-restaurante(A,_,_,_,_),nombre_platillo(A,B,_,_,_)")
  linea2="restaurante("+"A"+","+"B"+","+"C"+","+"D"+","+"E"+")"
  linea3="nombre_platillo("+"A"+","+"B"+","+"C"+","+"D"+","+"E"+")"
  list(prolog.query(linea2)) #se enlista la regla de restaurantes
  list(prolog.query(linea3)) #se enlista la regla de platillos
   
  #ciclo que realiza la busqueda en la base de conocimientos

  for soln in prolog.query("platillos("+ A + "," +"X)"): 
	
	#print("Si sirvio")
	print "Los platillos son: " + soln["X"] #imprime los platillos del restaurante

#****************************************************************************************************************
#Consulta: Lista de restaurantes que tienen platillos de algun pais especifico

def  lista_pais():   	    


  contador=0
  Pais_Ingresado=raw_input("Ingrese el tipo de comida para realizar la consulta:")	
  lista=leer_Archivo() #lista que tiene las listitas en las cuales estan las lineas del archivo
  lista2=leer_Archivo2()
  largo= len(lista)	
 # print(lista)

  #en este bucle se forman las reglas y hechos que iran en la base de conocimientos

  while (contador < largo): # Recorre la lista principal/ la que recibe

	lista_restaurantes=lista[contador] #tiene a listita

	lista_restaurantesFinal= lista_restaurantes[0].split(",") #tiene a listita con los strings separados

	#print(lista_restaurantesFinal)

	#cada uno de los parametros que iran en el hecho restaurante 

	Nombre=lista_restaurantesFinal[0]
	#print("EL nombre es: " + Nombre)
	Tipo_Comida=lista_restaurantesFinal[1]
	Ubicacion=lista_restaurantesFinal[2]
	Telefono=lista_restaurantesFinal[3]
	Horario=lista_restaurantesFinal[4]
	
	#linea es el hecho que ira en la base de conocimientos
	
	linea="restaurante("+Nombre+","+Tipo_Comida+","+Ubicacion+","+Telefono+","+Horario+")"
	#print linea
	#linea2="restaurante("+"A"+","+"B"+","+"C"+","+"D"+","+"E"+")"
	     	
	prolog.assertz(linea) #ingresa cada hecho en la base de conocimientos
	
        contador= contador + 1 

  contador=0
  largo=len(lista2)

  while (contador < largo): # Recorre la lista principal/ la que recibe

	lista_platillos=lista2[contador] #tiene a listita

	lista_platillos_final= lista_platillos[0].split(",") #tiene a listita con los strings separados

	i=len(lista_platillos_final)

	contador2=4
	
	Ingredientes=[]

	#print(lista_restaurantesFinal)

	#cada uno de los parametros que iran en el hecho restaurante 

	Restaurante=lista_platillos_final[0]
	#print("EL nombre es: " + Nombre)
	Platillo=lista_platillos_final[1]
	Sabor=lista_platillos_final[2]
	Pais_Origen=lista_platillos_final[3]

	#ciclo en donde se almacenan los ingredientes en una lista

	while contador2!=i:
		
		Ingredientes= Ingredientes + [Ingredientes.append(str(lista_platillos_final[contador2]))]
		contador2=contador2+1
	
	#linea es el hecho que ira en la base de conocimientos
	
 
        Ingredientes= filter(None,Ingredientes) #elimina el NONE
	str1 = ','.join(Ingredientes) #convierte una lista a string y separa cada elemento por ","
	#print(str1)
	
	linea="nombre_platillo("+Restaurante+","+Platillo+","+Sabor+","+Pais_Origen+","+"["+str1+"]"+")"
	     	
	prolog.assertz(linea) #ingresa cada hecho en la base de conocimientos
	
        contador= contador + 1 
	X= Pais_Ingresado
 
 
  prolog.assertz("lista_pais(X,Y):- restaurante(Y,B,C,D,E),nombre_platillo(Y,F,G,X,I)")
  lista_restaurantes=[]
  contador=0 
	
  #ciclo que realiza la busqueda en la base de conocimientos

  for soln in prolog.query("lista_pais(" + X  + "," + "Y)"): 
	
	lista_restaurantes= lista_restaurantes + [lista_restaurantes.append(soln["X"])]
	#print "Los restaurantes con platillos de ese pais son: " + soln["X"]

  lista_restaurantes=list(set(lista_restaurantes))
  lista_restaurantes= filter(None,lista_restaurantes) #elimina el NONE
  print lista_restaurantes


#********************************************************************************************

#Consulta: Lista de platillos de un restaurante especifico que tengan un ingrediente en particular

def  busqueda_ingrediente_particular():   	    

  contador=0
  lista=leer_Archivo() #lista que tiene las listitas en las cuales estan las lineas del archivo
  lista2=leer_Archivo2()
  largo= len(lista)	
 # print(lista)

  #en este bucle se forman las reglas y hechos que iran en la base de conocimientos

  while (contador < largo): # Recorre la lista principal/ la que recibe

	lista_restaurantes=lista[contador] #tiene a listita

	lista_restaurantesFinal= lista_restaurantes[0].split(",") #tiene a listita con los strings separados

	#cada uno de los parametros que iran en el hecho restaurante 

	Nombre=lista_restaurantesFinal[0]
	
	Tipo_Comida=lista_restaurantesFinal[1]
	Ubicacion=lista_restaurantesFinal[2]
	Telefono=lista_restaurantesFinal[3]
	Horario=lista_restaurantesFinal[4]
	
	#linea es el hecho que ira en la base de conocimientos
	
	linea="restaurante("+Nombre+","+Tipo_Comida+","+Ubicacion+","+Telefono+","+Horario+")"
	     	
	prolog.assertz(linea) #ingresa cada hecho en la base de conocimientos
	
        contador= contador + 1 

  contador=0
  largo=len(lista2)

  while (contador < largo): # Recorre la lista principal/ la que recibe

	lista_platillos=lista2[contador] #tiene a listita

	lista_platillos_final= lista_platillos[0].split(",") #tiene a listita con los strings separados

	i=len(lista_platillos_final)

	contador2=4
	
	Ingredientes=[]

	#print(lista_restaurantesFinal)

	#cada uno de los parametros que iran en el hecho restaurante 

	Restaurante=lista_platillos_final[0]
	#print("EL nombre es: " + Nombre)
	Platillo=lista_platillos_final[1]
	Sabor=lista_platillos_final[2]
	Pais_Origen=lista_platillos_final[3]

	#ciclo en donde se almacenan los ingredientes en una lista

	while contador2!=i:
		
		Ingredientes= Ingredientes + [Ingredientes.append(str(lista_platillos_final[contador2]))]
		contador2=contador2+1
	
	#linea es el hecho que ira en la base de conocimientos
	
 
        Ingredientes= filter(None,Ingredientes) #elimina el NONE
	str1 = ','.join(Ingredientes) #convierte una lista a string y separa cada elemento por ","
	#print(str1)
	
	linea="nombre_platillo("+Restaurante+","+Platillo+","+Sabor+","+Pais_Origen+","+"["+str1+"]"+")"
	
	     	
	prolog.assertz(linea) #ingresa cada hecho en la base de conocimientos
	
        contador= contador + 1 
 
 
  prolog.assertz("ingrediente_particular(X,Y,A):-restaurante(X,_,_,_,_),nombre_platillo(X,A,_,_,B),miembro(Y,B)")
  prolog.assertz("miembro(X,[X|Cola])") #busca si el ingrediente esta en la lista donde estan todos los ingredientes de "x" platillo
  prolog.assertz("miembro(X,[Cabeza|Cola]):-miembro(X,Cola)")

  #ciclo que realiza la busqueda en la base de conocimientos

  for soln in prolog.query("ingrediente_particular(mac,chile,X)"): 
	
	print("Si sirvio")
	print "Los platillos con dicho ingrediente son: " + soln["X"] #imprime los platillos con dicho ingrediente
	
  #ciclo que realiza la busqueda en la base de conocimientos

  for soln in prolog.query("lista_pais(" + X  + "," + "Y)"): 
	
	lista_restaurantes= lista_restaurantes + [lista_restaurantes.append(soln["X"])]
	#print "Los restaurantes con platillos de ese pais son: " + soln["X"]

  lista_restaurantes=list(set(lista_restaurantes))
  lista_restaurantes= filter(None,lista_restaurantes) #elimina el NONE
  print lista_restaurantes



#************************************************************************************************************************

def main():

  crear_Archivo()

  #escribir_Archivo()
  leer_Archivo()
  #Consulta_Tipo_Comida()
  consulta_restaurantes_por_nombre()			
  #consulta_restaurantes()	
  



main()
 

