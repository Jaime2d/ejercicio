import math
def area_cuadrado(lado):
	area=lado**2
	print(f"El area es {area}")
	
area_cuadrado(5) 
	

# volumen de un paralelepipedo Jaime Díaz
def Volumen_del_paralelepipedo(n1,n2,n3):
    volum = (n1*n2*n3)
    return volum
    
n1 = float( input("Ingreasa medida del lado a: " ))
n2 = float( input("Ingreasa medida del lado b: " ))
n3 = float( input("Ingreasa medida del lado c: " ))

res = Volumen_del_paralelepipedo(n1,n2,n3)
print(f"El volumen es {res}")
