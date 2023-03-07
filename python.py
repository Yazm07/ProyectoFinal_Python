print("Bienvenido a tu evaluación de Matemáticas")
nombre=input("Ingresa tu nombre: ")
nom=nombre.capitalize()
print(nom," elige cuál es tu grado escolar [1,2,3,4,5,6]")
grado=["1=Primero","2=Segundo","3=Tercero","4=Cuarto","5=Quinto","6=Sexto"]
print(grado)
grado=int(input())
if grado==1:
 print(nom,",bienvenido a tu evaluación de primer grado")
 print("MATEMÁTICAS")
 print("El examen consta de 10 preguntas y cada una vale 1 punto, al final se te dará tu calificación.")
 print("")
 print("Instrucciones: lee y responde los problemas. Solo colocar el resultado en número y no en letras")
 print("")
 p1=int(input("1. En una granja hay 2 perros grandes y 3 perros pequeño, ¿cuántos perros hay en total? "))
 if p1!=5:
  p1=0
 else:
  p1=1
 print("")
 p2=int(input("2. Ariana ha comprado 6 huevos y se le ha roto 1. ¿Cuántos huevos le quedan a Ariana?"))
 if p2!=5:
  p2=0
 else:
  p2=1
 print("")
 p3=int(input("3. Dentro de un salón de clases hay 12 niños, pero se salieron 9.¿Cuántos niños quedan en el salón de clases?"))
 if p3!=3:
  p3=0
 else:
  p3=1
 print("")
 p4=int(input("4. Mamá está calentando tortillas, primero ha colocado en la mesa 9 tortillas, luego colocó otras 3 y por último colocó otras 4.¿Cuántas tortillas hay en total en la mesa?"))
 if( p4!=16):
  p4=0
 else:
  p4=1
 print("")
 p5=int(input("Pamela tiene 15 duraznos y le regaló 8 a su abuelita. ¿Cuántos duraznos le quedan?"))
 if p5!=7:
  p5=0
 else:
  p5=1
 print("")
 print("Contesta las siguientes operaciones")
 print("")
 p6=int(input("a) 9 + 7 = "))
 if p6!=16:
  p6=0
 else:
  p6=1
 print("")
 p7=int(input("b) 18 - 11 = "))
 if p7!=7:
  p7=0
 else:
  p7=1
 print("")
 p8=int(input("c) 25 + 13 = "))
 if p8!=38:
  p8=0
 else:
  p8=1
 print("")
 p9=int(input("d) 27 - 16 = "))
 if p9!=11:
  p9=0
 else:
  p9=1
 print("")
 p10=int(input("e) 19 + 14 = "))
 if p10!=33:
  p10=0
 else:
  p10=1
 print("")
 print("Gracias por responder el examen")
 resultado=p1+p2+p3+p4+p5+p6+p7+p8+p9+p10
 print("")
 print("Tu calificación es: ", resultado)
if grado==2:
 print(nom,",bienvenido a tu evaluación de segundo grado")
 print("Instrucciones:responde las operaciones y coloca el resultado en números y no escrito.")
 print()
 print("Observa el precio de los juguetes y responde las preguntas 1 a la 4.")
 print()
 print("Tambor=$42      Oso=$18      Carrito=25     Pato=$15 ")
 print()
 p1=int(input("1. Miguel compró un tambor y un oso. ¿Cuánto tuvo que pagar?"))
 if p1!=60:
  p1=0
 else:
  p1=1
 print()
 p2=int(input("2. Si tiene $15, ¿cuánto más necesita para comprar un carrito?"))
 if p2!=10:
  p2=0
 else:
  p2=1
 print ()
 p3=int(input("3. Marcos quiere comprar un tambor, un oso, un carrito y un pato. Si decide hacerlo,¿cuánto es lo que va ha pagar? "))
 if p3!=100:
  p3=0
 else:
  p3=1
 print ()
 p4=int(input("4. Y si decide solo comprar 2 carritos y un pato,¿cuánto va a pagar? "))
 if p4!=65:
  p4=0
 else:
  p4=1
 print()
 p5=int(input("5. Para celebrar una fiesta hay un saquito con 423 caramelos, otro saquito con 402 gominolas y una caja con 127 barritas de chocolate. ¿Cuántos dulces hay en total?"))
 if p5!=952:
  p5=0
 else:
  p5=1
 print()
 p6=int(input("6. Mi padre tiene 96 pesos y mi madre 59 pesos. ¿Cuánto dinero tiene más mi padre que mi madre?"))
 if p6!=155:
  p6=0
 else:
  p6=1
 print()
 p7=int(input("7. Mi cuaderno tenia 90 hojas, pero ya he gastado 29. ¿Cuántas hojas puedo usar aún?"))
 if p7!=61:
  p7=0
 else:
  p7=1
 print()
 print("Resuelve las siguientes operaciones: ")
 p8=int(input("a) 16 + 14 + 5 = "))
 if p8!=35:
  p8=0
 else:
  p8=1
 print()
 p9=int(input("b) 20 + 10 + 5 = "))
 if p9!=35:
  p9=0
 else:
  p9=1
 p10=int(input("c) 744 - 597 = ") )
 if p10!=147:
  p10=0
 else:
  p10=1
 print("Gracias por responder el examen")
 resultado=p1+p2+p3+p4+p5+p6+p7+p8+p9+p10
 print("")
 print("Tu calificación es: ", resultado)
if grado==3:
 print(nom,",bienvenido a tu evaluación de tercer grado")
 print()
 print("Instrucciones:responde las operaciones y coloca el resultado en números y no escrito.")
 print()
 p1=int(input("1. En el almacén de una tienda de abarrotes hay 30 centenas de botellas de agua. ¿Cuántas botellas hay en total?"))
 if p1!=300:
  p1=0
 else:
  p1=1
 print()
 p2=int(input("2. Un camión, tiene un peso de 4578 kg. lleva una carga de 3458 kg. de zanahorias. ¿Cuántos kilogramosva a marcar la báscula cuando lo pesen?"))
 if p2!=8036:
  p2=0
 else:
  p2=1
 print ()
 p3=int(input("3. Una piscina tiene 54789 litros se han sacado 8970 litros por la mañana y 12678 litros por la tarde. ¿Cuántos litros de agua quedan en la piscina?"))
 if p3!=33141:
  p3=0
 else:
  p3=1
 print ()
 p4=int(input("4. Clara tiene 7 paquetes de chocolates con 5 chocolates cada paquete. Si además tiene 4 chocolates sueltos. ¿Cuántos chocolates tiene en total?"))
 if p4!=39:
  p4=0
 else:
  p4=1
 print()
 p5=int(input("5. La mamá de Ariana tiene 43 años y su padre, 9 años más. ¿Cuántos años tiene entre los dos?"))
 if p5!=95:
  p5=0
 else:
  p5=1
 print()
 p6=int(input("6. Un ganadero realizó las siguientes ventas: 38 cameros el dia lunes, 37 ovejas, 71 chivos y 33 conejos el dia martes. ¿Cuántos animales vendió en total?"))
 if p6!=179:
  p6=0
 else:
  p6=1
 print()
 p7=int(input("7. Un padre reparte propinas a sus cuatro hijos de la siguiente manera: $120 al primero, $130 al segundo, $140 al tercero y $150 al cuatro. ¿Cuánto fue el total repartido? $__"))
 if p7!=540:
  p7=0
 else:
  p7=1
 print()
 p8=int(input("8. ¿Qué número sigue en esta sucesión: 17, 21, 25, 29, 33; ? "))
 if p8!=37:
  p8=0
 else:
  p8=1
 print()
 p9=int(input("9. Juan desea comprarse un televisor que cuesta 300 pesos pero solamente tiene 174 pesos. ¿Cuánto le falta para poder comprar el televisor? "))
 if p9!=126:
  p9=0
 else:
  p9=1
 p10=int(input("10. Anita tiene 3 billetes de $20 y 3 monedas de $10. Si quiere comprarse una bicicleta que cuesta $98, ¿cuánto dinero le falta?") )
 if p10!=8:
  p10=0
 else:
  p10=1
 print()
 print("Gracias por responder el examen")
 resultado=p1+p2+p3+p4+p5+p6+p7+p8+p9+p10
 print("")
 print("Tu calificación es: ", resultado)
if grado==4:
 print(nom,",bienvenido a tu evaluación de cuarto grado")
 print()
 print("Instrucciones:responde las operaciones y coloca el resultado en números y no escrito.")
 print()
 p1=int(input("1. Mi mamá compro en la farmacia un frasco con 700 tabletas Si ha de tomar diariamente 4 tabletas ¿Para cuanto dias alcanzará el frasco?"))
 if p1!=175:
  p1=0
 else:
  p1=1
 print()
 p2=int(input("2. ¿Qué número sigue en la siguiente sucesión: 216, 215, 213, 210, 206? "))
 if p2!=201:
  p2=0
 else:
  p2=1
 print ()
 p3=int(input("3. Si a un número le sumas 92 obtienes el número 240. ¿Cuál es el número? "))
 if p3!=148:
  p3=0
 else:
  p3=1
 print ()
 p4=int(input("4. Un padre de familia gana $840 y gasta $150 en pasajes, $220 en alimentos y $210 en útiles caseros ¿Cuánto le queda en total?"))
 if p4!=260:
  p4=0
 else:
  p4=1
 print()
 p5=float(input("5. En el estadio hay una tienda en la que venden diferentes productos con el escudo del equipo. Mi padre ha comprado 3 camisetas por $13.50 cada una y 8 chapas por $1.75 cada una. Si pagó con un billete de $100, ¿cuánto dinero le devolvieron? "))
 if p5!=45.50 or p5!=45.5:
  p5=0
 else:
  p5=1
 print()
 p6=float(input("6. Vamos de viaje a una ciudad que está a 625.400 km. Hemos hecho el recorrido en tres tramos. En el primero hemos recorrido 143.870 km y en el segundo 145. 320 km más que en el primero. ¿Cuántos kilómetros recorreremos en el tercer tramo?"))
 if p6!=192.340 or p6!=192.34:
  p6=0
 else:
  p6=1
 print()
 print("Resuelve las siguientes sumas de fracciones")
 print("a)")
 print("1 3  ")
 print("-+- = -")
 print("2 8  ")
 p71=int(input(" Numerador= "))
 if p71!=7:
  p71=0
 else:
  p71=0.5
 p72=int(input(" Denominador= "))
 if p72!=8:
  p72=0
 else:
  p72=0.5
 p7=p71+p72
 print()
 print("b)")
 print("8 5  ")
 print("-+- = -")
 print("6 7  ")
 p81=int(input("numerador= "))
 if p81!=43:
  p81=0
 else:
  p81=0.5
 p82=int(input("denominador= "))
 if p82!=21:
  p82=0
 else:
  p82=0.5
 p8=p81+p82
 print()
 print("c)")
 print("7 3  ")
 print("-+- = -")
 print("8 2 ")
 p91=int(input("numerador= "))
 if p91!=43:
  p91=0
 else:
  p91=0.5
 p92=int(input("denominador= "))
 if p92!=21:
  p92=0
 else:
  p92=0.5
 p9=p91+p92
 print()
 print("d)")
 print("4 2  ")
 print("-+- = -")
 print("9 3 ")
 p101=int(input("numerador= "))
 if p101!=10:
  p101=0
 else:
  p101=0.5
 p102=int(input("denominador= "))
 if p102!=9:
  p102=0
 else:
  p102=0.5
 p10=p101+p102
 print()
 print("Gracias por responder el examen")
 resultado=p1+p2+p3+p4+p5+p6+p7+p8+p9+p10
 print("")
 print("Tu calificación es: ", resultado)
if grado==5:
 print(nom,"bienvenido a tu evaluación de quinto grado")
 print()
 print("Instrucciones:responde las operaciones y coloca el resultado en números y no escrito.")
 print()
 p1=int(input("1. Alma fue al supermercado y compró 6 paquetes de 1/2 kg de café y 7 paquetes de 3/7 kg de galletitas. Al salir las bolsas estaban muy pesadas. ¿Cuánto peso estaba cargando (la respuesta sera en enteros y no fracción)?")) 
 if p1!=6:
  p1=0
 else:
  p1=1
 print()
 p2=float(input("2. ¿Cuánto es el doble de 3,45?"))
 if p2!=6.9 or p2!=6.90:
  p2=0
 else:
  p2=1
 print ()
 p3=int(input("3. El verdulero de Carmen compra 200 kg de bananas por $110, y los vende al público a $2,5 el kilo. ¿Cuánto dinero habrá ganado el verdulero si vende todas las bananas?"))
 if p3!=390:
  p3=0
 else:
  p3=1
 print ()
 p4=float(input("4. La granja de gallinas de Paco ha vendido 1092 huevos. Si Paco vende la docena de huevos a $1.25 ¿Cuánto dinero ganó Paco?"))
 if p4!=113.75:
  p4=0
 else:
  p4=1
 print()
 p5=int(input("5. En el grudo de Aldo, hay 22 varones, que son 2/3 de los alumnos del curso. ¿Cuántas niñas hay en el grado?"))
 if p5!=11:
  p5=0
 else:
  p5=1
 print()
 p6=float(input("6. Luciano gasta en el alquiler de su departamento $1.300, que es exactamente 1/3 de su sueldo. ¿Cuál es el sueldo de Luciano?"))
 if p6!=3900 or p6!=3.900:
  p6=0
 else:
  p6=1
 print()
 p7=int(input("7. Natalia comió 5/8 de un chocolate y Juana comió 3/8 del chocolate. ¿Cuánto chocolate quedó?"))
 if p7!=0:
  p7=0
 else:
  p7=1
 print()
 print("8. El ha pintado 5/8 de la pared de verde, 1/4 de marrón y el resto no está pintada todavía. ¿Qué parte no está pintada?")
 p81=int(input("Nominador= "))
 if p81!=1:
  p81=0
 else:
  p81=0.5
 p82=int(input("Denominador= "))
 if p82!=8:
  p82=0
 else:
  p82=0.5
 p8=p82+p81
 print()
 p9=int(input("9. Si en una granja se han recogido 3.852 huevos de gallina, ¿cuántas docenas de huevos de gallina hay en la granja?"))
 if p9!=321:
  p9=0
 else:
  p9=1
 print()
 p10=int(input("10. Si un pastor necesita 96 kilos de hierbas para dar de comer a sus animales durante 30 días, ¿cuántos kilos de hierbas necesitará en 10 días?"))
 if p10!=32:
  p10=0
 else:
  p10=1
print()
print("Gracias por responder el examen")
resultado=p1+p2+p3+p4+p5+p6+p7+p8+p9+p10
print("")
print("Tu calificación es: ", resultado)
if grado==6:
 print(nom,",bienvenido a tu evaluación de sexto grado")
 print()
 print("Instrucciones:responde las operaciones y coloca el resultado en números y no escrito.")
 print()
 p1=float(input("1. Para comprar una casa, Pilar aporta $13.854 más que Sandra y Alicia $36.841 menos que Sandra. Si Sandra aportó $214.693, ¿cuánto pagaron por la casa? "))
 if p1!=621.092:
  p1=0
 else:
  p1=1
 print()
 p2=float(input("2. Los 16 alumnos del grado de Dalia han salido de excursión al parque de atracciones. Cada entrada al parque cuesta $14,60. ¿Cuánto tienen que pagar por todas las entradas? "))
 if p2!=233.60 :
  p2=0
 else:
  p2=1
 print ()
 p3=int(input("3. Un tanque de agua tiene capacidad para 56.280 litros. Si se distribuye equitativamente el agua del tanque durante el mes de septiembre. ¿Cuántos litros diarios se podrán gastar?"))
 if p3!=1876:
  p3=0
 else:
  p3=1
 print ()
 p4=int(input("4. Andrea leyó 120 páginas que representan 3/4 partes de un libro, ¿cuántas páginas le falta leer?"))
 if p4!=40:
  p4=0
 else:
  p4=1
 print()
 print("5. Luz pegó 27 figuritas en su álbum. Si el álbum tiene 54 figuritas, ¿qué parte del álbum completó?")
 p51=int(input("Nominador= "))
 if p51!=1:
  p51=0
 else:
  p51=0.5
 p52=int(input("Denominador= "))
 if p52!=2:
  p52=0
 else:
  p53=0.5
 p5=p51+p52
 print()
 p6=int(input("6. Algunos amigos decidieron que al terminar la fiesta se dividirían el resto de la torta en partes iguales. Si sobró un cuarto de la torta, y cada amigo se llevó 1/16 de torta, ¿cuántos amigos eran? "))
 if p6!=4:
  p6=0
 else:
  p6=1
 print()
 p7=int(input("7. En el bar de José se despacharon 15 botellas de vino, obteniendo de cada botella 12 copas que se vendieron a 0,65 pesos cada una. Si José pagó 4,8 euros cada botella, ¿cuál fue la ganancia del bar?" ))
 if p7!=45:
  p7=0
 else:
  p7=1
 print()
 p8=int(input("8. De una tira de cinta de 30 metros de largo, se cortó primero 1/5 y luego 1/4 de lo que quedaba. ¿Cuántos metros de cinta quedaron después del segundo corte? "))
 if p8!=18:
  p8=0
 else:
  p8=1
 print()
 p9=float(input("9. La fotocopiadora del trabajo de Andrea hace 48 copias cada minuto. Si cada fotocopia cuesta 0,08 pesos ¿Cuánto costarán todas las fotocopias que puede hacer la fotocopiadora durante 8 horas? "))
 if p9!=1843.2:
  p9=0
 else:
  p9=1
 p10=int(input("10. En la biblioteca de las escuela hay 15 estantes con 7 diccionarios en cada uno. También hay 8 estantes con 12 libros de historia y 8 libros de geografía en cada uno. ¿Cuántos libros hay en todos los estantes? "))
 if p10!=8:
  p10=0
 else:
  p10=1
 print()  
 print("Gracias por responder el examen")
 resultado=p1+p2+p3+p4+p5+p6+p7+p8+p9+p10
 print("")
 print("Tu calificación es: ", resultado)