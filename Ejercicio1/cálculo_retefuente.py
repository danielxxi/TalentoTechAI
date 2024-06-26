# -*- coding: utf-8 -*-
"""Cálculo Retefuente.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1neKVCpfeydMPv6bZN7mE86gOcaWxtTY1
"""

#CODIGO EN PHYTON PARA EL CALCULO DE LA RETENCION EN LA FUENTE PARA COLOMBIA AÑO 2024

# Por favor ingresar el salario base del Empleado
salario_base = float(input("Ingrese el salario base del empleado en pesos: "))
print(f"El salario ingresado para el empleado es: ${salario_base:,.2f} ")

# Cáculo de los descuentos de Ley salud pensiones y fondo solidario
descuentos_ley = salario_base * 0.09 #9% correspondiente al total de descuentos de ley
print (f"Descuentos por ley: ${descuentos_ley:,.2f}") #Impresión del valor correspondiente a los descuentos por ley

#Cáculo del salario descontando parafiscales
salario2 = salario_base-descuentos_ley
#Impresion del salario con descuentos parafiscales salud, pensión y fondo solidario
print(f"Salario con descuentos parafiscales: ${salario2:,.2f}")

#Cáculo del salario base para la determinación de la retención en la fuente
salario3 = salario2*.75


#Cáculo salario sin retención
if salario3<4471175:
  print("No tiene retención")
  #Cálculo final del salario a pagar al empleado despues de parafiscales
  salempleado = salario_base-descuentos_ley
  #Impresión final del salario a pagar al Empelado
  print("\033[1m" + f"Salario a pagar al empleado: ${salempleado:,.2f}"+ "\033[0m")

#Cáculo retención del 19%
elif salario3<7059750:
  print (f"Salario base para gravamen de retefuente: ${salario3:,.2f}")
  #Cálculo de la retención del 19% de acuerdo al salario base del gravamen
  retencion19 = salario3*0.19
  print("\033[1m" + f"Salario tiene retención del 19% ; ${retencion19:,.2f}" + "\033[0m")
  #Cálculo final del salario a pagar al empleado despues de impuestos y parafiscales
  salempleado = salario_base-descuentos_ley-retencion19
  #Impresión final del salario a pagar al Empelado
  print("\033[1m" + f"Salario a pagar al empleado: ${salempleado:,.2f}"+ "\033[0m")

#Cáculo retención del 28%
elif salario3<16943400:
  print (f"Salario base para gravamen de retefuente: ${salario3:,.2f}")
  #Cálculo de la retención del 28% de acuerdo al salario base del gravamen
  retencion28 = salario3*0.28
  print("\033[1m" + f"Salario tiene retención del 28% ; ${retencion28:,.2f}" + "\033[0m")
  #Cálculo final del salario a pagar al empleado despues de impuestos y parafiscales
  salempleado = salario_base-descuentos_ley-retencion28
  #Impresión final del salario a pagar al Empelado
  print("\033[1m" + f"Salario a pagar al empleado: ${salempleado:,.2f}"+ "\033[0m")

#Cáculo retención del 33%
elif salario3<30121600:
  print (f"Salario base para gravamen de retefuente: ${salario3:,.2f}")
  #Cálculo de la retención del 33% de acuerdo al salario base del gravamen
  retencion33 = salario3*0.33
  print("\033[1m" + f"Salario tiene retención del 33% ; ${retencion33:,.2f}" + "\033[0m")
  #Cálculo final del salario a pagar al empleado despues de impuestos y parafiscales
  salempleado = salario_base-descuentos_ley-retencion33
  #Impresión final del salario a pagar al Empelado
  print("\033[1m" + f"Salario a pagar al empleado: ${salempleado:,.2f}"+ "\033[0m")

#Cáculo retención del 35%
elif salario3<44476425:
  print (f"Salario base para gravamen de retefuente: ${salario3:,.2f}")
  #Cálculo de la retención del 35% de acuerdo al salario base del gravamen
  retencion35 = salario3*0.35
  print("\033[1m" + f"Salario tiene retención del 35% ; ${retencion35:,.2f}" + "\033[0m")
  #Cálculo final del salario a pagar al empleado despues de impuestos y parafiscales
  salempleado = salario_base-descuentos_ley-retencion35
  #Impresión final del salario a pagar al Empelado
  print("\033[1m" + f"Salario a pagar al empleado: ${salempleado:,.2f}"+ "\033[0m")

#Cáculo retención del 37%
elif salario3<108248500:
  print (f"Salario base para gravamen de retefuente: ${salario3:,.2f}")
  #Cálculo de la retención del 37% de acuerdo al salario base del gravamen
  retencion37 = salario3*0.37
  print("\033[1m" + f"Salario tiene retención del 37% ; ${retencion37:,.2f}" + "\033[0m")
  #Cálculo final del salario a pagar al empleado despues de impuestos y parafiscales
  salempleado = salario_base-descuentos_ley-retencion37
  #Impresión final del salario a pagar al Empelado
  print("\033[1m" + f"Salario a pagar al empleado: ${salempleado:,.2f}"+ "\033[0m")

#Cáculo retención del 39%
elif salario3<235325000:
  print (f"Salario base para gravamen de retefuente: ${salario3:,.2f}")
  #Cálculo de la retención del 39% de acuerdo al salario base del gravamen
  retencion39 = salario3*0.39
  print("\033[1m" + f"Salario tiene retención del 39% ; ${retencion39:,.2f}" + "\033[0m")
  #Cálculo final del salario a pagar al empleado despues de impuestos y parafiscales
  salempleado = salario_base-descuentos_ley-retencion39
  #Impresión final del salario a pagar al Empelado
  print("\033[1m" + f"Salario a pagar al empleado: ${salempleado:,.2f}"+ "\033[0m")