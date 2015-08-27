
# coding: utf-8

### Tarea1. Andres Felipe Rodriguez Corcho

# In[3]:

#Libreria Matematica
get_ipython().magic(u'pylab inline')


# In[4]:

#Funcion producto Cruz
def Cruz(V1,V2):
    return numpy.cross(V1,V2)


# In[5]:

#Funcion Magnitud Vector
def Magnitud(v):
    return sqrt(v[0]**2+v[1]**2+v[2]**2)


# In[6]:

def VelocidadRelativa (w,lat,lon,latEu,lonEu):
    #Transformacion de coordenadas de grados a Radianes
    lat=radians(lat)
    lon=radians(lon)
    latEu=radians(latEu)
    lonEu=radians(lonEu)
    w=w*(numpy.pi/180) #rad/yr
    rtierra=6371*10**3 #metros
    
    #Conversion a Coordenadas cartesianas
    Punto=[sin((numpy.pi/2)-lat)*cos(lon),cos(lat)*sin(lon),sin(lat)]
    Polo=[w*sin((numpy.pi/2)-latEu)*cos(lonEu),w*cos(latEu)*sin(lonEu),w*sin(latEu)]
    
    
    #Producto Cruz
    v=rtierra*Cruz(Polo,Punto)
    
    #Conversion al sistema local de coordenadas
    
    #Matriz de Transformacion
    Transf=numpy.zeros((3,3))
    #Fila 1
    Transf[0][0]=-sin(lat)*cos(lon)
    Transf[0][1]=-sin(lat)*sin(lon)
    Transf[0][2]=cos(lat)
    #Fila 2
    Transf[1][0]=-sin(lon)
    Transf[1][1]=cos(lon)
    Transf[1][2]=0
    #Fila 3
    Transf[2][0]=-cos(lat)*cos(lon)
    Transf[2][1]=-cos(lat)*sin(lon)
    Transf[2][2]=-sin(lat)
    
    #Multiplicacion Matricial
    V=numpy.matrix(v).T
    Vtan=Transf*V
    
    #Devuelve el vector calculado   
    return Vtan
    


#### Calculos Punto 2

# In[7]:

#Calculo de la Velocidad del Volcan Mauna Loa
Va=VelocidadRelativa(9.67*10**-7,19.475,-155.608,-61.7,97.2)

print Va,"m/yr"


# In[8]:

#Calculo Magnitud
Vmaga=Magnitud(Va)
#Despejamos el tiempo, usando la distancia dada de 100 km
ta=(100*10**3)/Vmaga
#Resultados
print "La magnitud de la velocidad tangencial es ",Vmaga," m/yr"
print "\nEl tiempo en el cual el Volcan Mauna Loa se mueve 100 km sobre el hotspot es de:",ta/10**6," Millones años"


# De esta Manera la cadena de islas se mueve a una velocidad de 0.0972m/yr hacia el noroccidente.

#### Parte B El volcan Mauna Loa se mueve hacia el NorOeste segun el vector V=(N,E,U) calculado.

# In[9]:

from IPython.display import Image
Image(filename='Hawai.PNG')


# En la imagen se muestra la cadena de islas del problema, que se dezplaza hacia el noroccidente a la velocidad calculada anteriormente (La isla mas grande que se observa es Hawai, las demas han sido erosionadas con el tiempo). Es posible observar, que a lo largo del tiempo el patron de movimiento de la placa del pacifico ha cambiado, por lo cual, se tendra en cuenta el que se presenta en la actualid

# Considerando que la cadena de islas (Placa del Pacifico respecto al Hotsop) siga el mismo patron colisionara con la masa de tierra (Perteneciente a territorio Japones) que se observa en la imagen, deslizandose debajo de la trinchera observada, a una distancia de:

# In[10]:

from IPython.display import Image
Image(filename='MasaTierra.PNG')


# De esta manera para que esta primera isla colisione debera avanzar 5856.16 km, junto con las coordenadas del lugar, asi que, usando lo programado anteriormente, tenemos:

# In[11]:

#Datos
#Punto Colision
LatB=29.267187
LonB=142.336490
#Polo Euler
w3=-9*10**-7
LaTEB=61.1
LonEB=85.8

#Calculo de la Velocidad de la Primera isla
Vb=VelocidadRelativa(w3,LatB,LonB,-61.7,97.2)

print Vb,"m/yr"


# In[12]:

#Calculo Magnitud
Vmagb=Magnitud(Vb)
#Despejamos el tiempo, usando la distancia dada de 100 km
tb=(5856.16*10**3)/Vmagb
#Resultados
print "La magnitud de la velocidad tangencial es ",Vmagb," m/yr"
print "\nEl tiempo en el cual la primera isla se mueve 5856.16 km es de:",tb/10**6," Millones años"


### Calculos Punto 3

# In[13]:

#Este punto se realizara usando estadistica de varios puntos tomados para verificar las velocidades calculadas, tomaremos seis.
Lat1= 26.861280 #°
Lon1= 86.368437 #°
Lat2= 26.786975 #°
Lon2= 88.489034 #°
Lat3= 27.551165 #°
Lon3= 83.801183 #°
Lat4= 28.795444 #°
Lon4= 80.799421 #°
Lat5= 32.525292 #°
Lon5= 75.137280 #°
Lat6= 27.611310 #°
Lon6= 94.517372 #°

#Coordenadas del Polo Euler y velocidad angular en radianes/yr
w3=5.3*10**-7 #deg/yr
Lat=24.4 #°
Lon=17.7 #°


# In[14]:

#Calculo de la Velocidad de diferentes puntos en el Plateau de Tibet
V1=VelocidadRelativa(w3,Lat1,Lon1,Lat,Lon)
V2=VelocidadRelativa(w3,Lat2,Lon2,Lat,Lon)
V3=VelocidadRelativa(w3,Lat3,Lon3,Lat,Lon)
V4=VelocidadRelativa(w3,Lat4,Lon4,Lat,Lon)
V5=VelocidadRelativa(w3,Lat5,Lon5,Lat,Lon)
V6=VelocidadRelativa(w3,Lat6,Lon6,Lat,Lon)

#Resultados
print "Las velocidades en m/ yr de los puntos son (en orden ascendente 1 a 6):\n",V1,"\n",V2,"\n",V3,"\n",V4,"\n",V5,"\n",V6


# In[15]:

#Magnitudes
Vmag1=Magnitud(V1)
Vmag2=Magnitud(V2)
Vmag3=Magnitud(V3)
Vmag4=Magnitud(V4)
Vmag5=Magnitud(V5)
Vmag6=Magnitud(V6)

#Resultados
print "Las magnitudes correspondientes en m/ yr de los puntos son (en orden ascendente 1 a 6):\n",Vmag1,"\n",Vmag2,"\n",Vmag3
print Vmag4,"\n",Vmag5,"\n",Vmag6


# In[16]:

from IPython.display import Image
Image(filename='Tibet.PNG')


# Podemos observar que las magnitudes (y los vectores) de velocidad son muy similares en los diferentes puntos de el Plateau del Tibet tomados (como se puede observar en el mapa). Sin embargo, se calculara la desviacion estandar de estos, para tener un valor cuantitativo de mayor validez.

# In[17]:

#Array con velocidades
Vel3=[Vmag1,Vmag2,Vmag3,Vmag4,Vmag5,Vmag6]

#Calculo Desviacion
Desv=numpy.std(Vel3)

#Resultados
print "La desviacion estandar calculada es: ", Desv


# Teniendo en cuenta la desviacion estandar calculada, se puede calcular un promedio de las velocidades.

# In[18]:

Vprom=numpy.mean(Vel3)
print "La velocidad promedio de convergencia entre las placas de Eurasia e India es de: ",Vprom," m/yr"


#### Paper con Densidades de modelo isostatico 

# http://www.seismo.ethz.ch/research/groups/stek/people/hetenyig/pub/Hetenyi2007.pdf

# In[18]:



