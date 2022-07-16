import re
import sys

if len(sys.argv) > 1:
    input_file = sys.argv[1]
else:
    raise Exception("Especifica el nombre del archivo a analizar.")

# Nuestra funcion
def fun_go(cadena, diccionario,regexSin,regexIn,stringTipo):
  splited = cadena.split(',')
  for i in splited:
    matches_1 = re.findall(regexSin, i)
    for match in matches_1:
      if len(match)>0:
        cadena = cadena.replace(match,"", 1)
        result = re.search(" *([a-zA-Z][a-zA-Z0-9_]*) *(=|:)", match)
        nom_var = result.group(1)
        if nom_var in diccionario:
          raise Exception("Ya se inicializo este variable.")
        else:
          diccionario[nom_var] = [stringTipo, False]

  lista = re.findall(regexIn, cadena)
  for match in lista:
    for group in match:
      if len(group)>0:
        cadena = cadena.replace(group,"", 1)
        result = re.search(" *([a-zA-Z][a-zA-Z0-9_]*) *(=|:)", group)
        nom_var = result.group(1)
        diccionario[nom_var] = [stringTipo, True]
        
  return cadena

archivo_input_rLSI = open("regexListStrInit.txt","r")
archivo_input_rSI = open("regexStrInit.txt","r")

# Nuestros Regex
regexListaStringSin = r"""([a-zA-Z][a-zA-Z0-9_]* *(?:: *(?:Array *< *String *>|\[ *String *\]){1}){1} *)"""
regexListaStringIn = archivo_input_rLSI.read()
regexListaCharacterSin = r"""([a-zA-Z][a-zA-Z0-9_]* *(?:: *(?:Array *< *Character *>|\[ *Character *\]){1}){1} *)$"""
regexListaCharacterIn = r"""([a-zA-Z][a-zA-Z0-9_]* *(?:: *(?:Array *< *Character *>|\[ *Character *\]){1}){1} *= *\[ *(?:|(?:"(?:[^\\"]|\\.){1}"|"(?:\\u\{[a-fA-F0-9]{1,4}\})+")|(?:"(?:[^\\"]|\\.){1}"|"(?:\\u\{[a-fA-F0-9]{1,4}\})+"){1}(?: *, *(?:"(?:[^\\"]|\\.){1}"|"(?:\\u\{[a-fA-F0-9]{1,4}\})+") *)+) *\] *)|([a-zA-Z][a-zA-Z0-9_]* *= *Array *< *Character *> *\( *\))|([a-zA-Z][a-zA-Z0-9_]* *= *\[ *Character *\] *\( *\))"""
regexStringSin = r"""([a-zA-Z][a-zA-Z0-9_]* *(?:: *String *) *)"""
regexStringIn = archivo_input_rSI.read()
regexCharacterSin = r"""([a-zA-Z][a-zA-Z0-9_]* *(?:: *Character *) *)$"""
regexCharacterIn = r"""([a-zA-Z][a-zA-Z0-9_]* *: *Character *= *(?:"(?:[^\\"]|\\.){1}"|"(?:\\u\{[a-fA-F0-9]{1,4}\})+"))|([a-zA-Z][a-zA-Z0-9_]* *= *(?:"(?:[^\\"]|\\.){1}"|"(?:\\u\{[a-fA-F0-9]{1,4}\})+"))|([a-zA-Z][a-zA-Z0-9_]* *(?:: *(?: *Character *)){0,1} *= *Character *\( *\))"""
regexListaDoubleSin = r"""([a-zA-Z][a-zA-Z0-9_]* *(?:: *(?:Array *< *Double *>|\[ *Double *\]){1}){1} *)$"""
regexListaDoubleIn = r"""([a-zA-Z][a-zA-Z0-9_]* *(?:: *(?:Array *\< *Double *\>|\[ *Double *\]){1} *){1} *= *\[ *(?:|(?:\+|-){0,1} *\d+(?:\.\d{1,15}){0,1}|(?:(?:\+|-){0,1} *\d+(?:\.\d{1,15}){0,1}(?: *, *(?:\+|-){0,1} *\d+(?:\.\d{1,15}){0,1})+)) *\] *)|([a-zA-Z][a-zA-Z0-9_]* *= *Array *< *Double *> *\( *\))|([a-zA-Z][a-zA-Z0-9_]* *= *\[ *Double *\] *\( *\))"""
regexDoubleSin = r"""([a-zA-Z][a-zA-Z0-9_]* *(?:: *Double *) *)$"""
regexDoubleIn = r"""([a-zA-Z][a-zA-Z0-9_]* *: *Double *= *(?:\+|-){0,1} *\d+(?:\.\d{1,15}){0,1})|([a-zA-Z][a-zA-Z0-9_]* *= *(?:\+|-){0,1} *\d+(?:\.\d{1,15}))|([a-zA-Z][a-zA-Z0-9_]* *(?:: *(?: *Double *)){0,1} *= *Double *\( *\))"""
regexListaFloatSin = r"""([a-zA-Z][a-zA-Z0-9_]* *(?:: *(?:Array *< *Float *>|\[ *Float *\]){1}){1} *)$"""
regexListaFloatIn = r"""([a-zA-Z][a-zA-Z0-9_]* *(?:: *(?:Array *\< *Float *\>|\[ *Float *\]){1} *){1} *= *\[ *(?:|(?:\+|-){0,1} *\d+(?:\.\d{1,6}){0,1}|(?:(?:\+|-){0,1} *\d+(?:\.\d{1,6}){0,1}(?: *, *(?:\+|-){0,1} *\d+(?:\.\d{1,6}){0,1})+)) *\] *)|([a-zA-Z][a-zA-Z0-9_]* *= *\[ *(?:(?:\+|-){0,1} *\d+(?:\.\d{1,6})|(?:(?:\+|-){0,1} *\d+(?:\.\d{1,6})(?: *, *(?:\+|-){0,1} *\d+(?:\.\d{1,6}))+)) *\] *)|([a-zA-Z][a-zA-Z0-9_]* *= *Array *< *Float *> *\( *\))|([a-zA-Z][a-zA-Z0-9_]* *= *\[ *Float *\] *\( *\))"""
regexFloatSin = r"""([a-zA-Z][a-zA-Z0-9_]* *(?:: *Float *) *)$"""
regexFloatIn = r"""([a-zA-Z][a-zA-Z0-9_]* *: *Float *= *(?:\+|-){0,1} *\d+(?:\.\d{1,6}){0,1})|([a-zA-Z][a-zA-Z0-9_]* *= *(?:\+|-){0,1} *\d+(?:\.\d{1,6}))|([a-zA-Z][a-zA-Z0-9_]* *(?:: *(?: *Float *)){0,1} *= *Float *\( *\))"""
regexListaBoolSin = r"""([a-zA-Z][a-zA-Z0-9_]* *(?:: *(?:Array *< *Bool *>|\[ *Bool *\]){1}){1} *)$"""
regexListaBoolIn = r"""([a-zA-Z][a-zA-Z0-9_]* *(?:: *(?:Array *< *Bool *>|\[ *Bool *\]){1}){1} *= *\[ *(?:|(?:true|false){1}|(?:true|false){1}(?: *, *(?:true|false){1} *)+) *\] *)|([a-zA-Z][a-zA-Z0-9_]* *= *\[ *(?:(?:true|false){1}|(?:true|false){1}(?: *, *(?:true|false){1} *)+) *\] *)|([a-zA-Z][a-zA-Z0-9_]* *= *Array *< *Bool *> *\( *\))|([a-zA-Z][a-zA-Z0-9_]* *= *\[ *Bool *\] *\( *\))"""
regexBooleanSin = r"""([a-zA-Z][a-zA-Z0-9_]* *(?:: *(?:Array *< *Bool *>|\[ *Bool *\]){1}){1} *)$"""
regexBooleanIn = r"""([a-zA-Z][a-zA-Z0-9_]* *: *Bool *= *(?:true|false))|([a-zA-Z][a-zA-Z0-9_]* *= *(?:true|false))|([a-zA-Z][a-zA-Z0-9_]* *(?:: *(?: *Bool *)){0,1} *= *Bool *\( *\))"""
regexListaIntSin = r"""([a-zA-Z][a-zA-Z0-9_]* *(?:: *(?:Array *< *Int *>|\[ *Int *\]){1}){1} *)$"""
regexListaIntIn = r"""([a-zA-Z][a-zA-Z0-9_]* *(?:: *(?:Array *\< *Int *\>|\[ *Int *\]){1} *){1} *= *\[ *(?:|(?:\+|-){0,1} *\d+|(?:(?:\+|-){0,1} *\d+(?: *, *(?:\+|-){0,1} *\d+)+)) *\] *)|([a-zA-Z][a-zA-Z0-9_]* *= *\[ *(?:(?:\+|-){0,1} *\d+|(?:(?:\+|-){0,1} *\d+(?: *, *(?:\+|-){0,1} *\d+)+)) *\] *)|([a-zA-Z][a-zA-Z0-9_]* *= *Array *< *Int *> *\( *\))|([a-zA-Z][a-zA-Z0-9_]* *= *\[ *Int *\] *\( *\))"""
regexIntSin = r"""([a-zA-Z][a-zA-Z0-9_]* *: *Int *)$"""
regexIntIn = r"""([a-zA-Z][a-zA-Z0-9_]* *: *Int *= *(?:\+|-){0,1} *\d+)|([a-zA-Z][a-zA-Z0-9_]* *= *(?:\+|-){0,1} *\d+)|([a-zA-Z][a-zA-Z0-9_]* *(?:: *(?: *Int *)){0,1} *= *Int *\( *\))"""

# Leemos el archivo
archivo_input = open(input_file,"r")

# Lo pasamos a un String llamado contenido
contenido = archivo_input.read()

# Diccionario de Datos
diccionario = {}

# Separamos por cada "var" y por cada "let" al principio de una línea
step_one_list = re.split("\nlet |\nvar ",contenido)

# Por cada String que ocurre después de un "let" o un "var"
for i in step_one_list:
  #i = line[1]
  # Contamos las listas de Chars
  i = fun_go(i, diccionario, regexListaCharacterSin, regexListaCharacterIn, "Arreglo Character")
  # Contamos las listas de Strings
  i = fun_go(i, diccionario, regexListaStringSin, regexListaStringIn, "Arreglo String")
  # Contamos los Chars
  i = fun_go(i, diccionario, regexCharacterSin, regexCharacterIn, "Character")
  # Contamos los Strings
  i = fun_go(i, diccionario, regexStringSin, regexStringIn, "String")
  # Contamos las listas de Float
  i = fun_go(i, diccionario, regexListaFloatSin, regexListaFloatIn, "Arreglo Float")
  # Contamos los Float
  i = fun_go(i, diccionario, regexFloatSin, regexFloatIn, "Float")
  # Contamos las listas de Double
  i = fun_go(i, diccionario, regexListaDoubleSin, regexListaDoubleIn, "Arreglo Double")
  # Contamos los Double
  i = fun_go(i, diccionario, regexDoubleSin, regexDoubleIn, "Double")
  # Contamos las listas de Int
  i = fun_go(i, diccionario, regexListaIntSin, regexListaIntIn, "Arreglo Int")
  # Contamos los Int
  i = fun_go(i, diccionario, regexIntSin, regexIntIn, "Int")
  # Contamos las listas de Boolean
  i = fun_go(i, diccionario, regexListaBoolSin, regexListaBoolIn, "Arreglo Boolean")
  # Contamos los Boolean
  i = fun_go(i, diccionario, regexBooleanSin, regexBooleanIn, "Boolean")
  


print("-----------------------------")
print("Tus resultados estan listos:")
print("-----------------------------")
print("")

# Numero total de variables declaradas.
print("Número total de variables declaradas: " + str(len(diccionario)) + ".")
print("")

# Numero total de tipos utilizados en las declaraciones encontradas.
lista2 = []
for i in diccionario:
  lista2.append((diccionario[i])[0])
lista2 = set(lista2)
print("Número total de tipos utilizados en las declaraciones encontradas: " + str(len(lista2)) + ".")
print("")

# Numero total de variables declaradas de cada tipo:
diccionario_tipos = {}
for i in diccionario.values():
  if i[0] in diccionario_tipos:
    diccionario_tipos[i[0]] += 1
  else:
    diccionario_tipos[i[0]] = 1
print("Numero total de variables declaradas de cada tipo: ")
for i in diccionario_tipos:
  print(str(diccionario_tipos[i]) + " variables de tipo " + i + ".")
print("")

# Numero total de variables inicializadas.
dato4 = 0
for i in diccionario.values():
  if i[1]:
    dato4 += 1
print("Numero total de variables inicializadas: " + str(dato4) + ".")
print("")

# Numero total de variables declaradas pero no inicializadas.
print("Numero total de variables declaradas pero no inicializadas: " + str(len(diccionario)-dato4) + ".")
print("")

# Numero total de variables de tipo arreglo.
dato5 = 0
for i in diccionario.values():
  if ("Arreglo") in i[0]:
    dato5 += 1
print("Numero total de variables de tipo arreglo: " + str(dato5) + ".")
print("")

# Clasificación de todos los nombres de variables por tipo declarado.
diccionario_inverso = {}
for i in diccionario:
  if diccionario[i][0] in diccionario_inverso:
    diccionario_inverso[diccionario[i][0]].append(i)
  else:
    diccionario_inverso[diccionario[i][0]] = [i]

for i in diccionario_inverso:
  print("Variables de tipo " + i + ":")
  print(diccionario_inverso[i])
print("")