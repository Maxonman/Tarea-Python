import re


DIGITO = r"[1-9]"
DIGITO_O_0 = r"[1-9]|0"
VARIABLE = r"[A-Z|a-z][A-Z|a-z|0-9]*"
BOOLEANO = r"True|False"
STRING = r"#[A-Z|a-z|0-9]+#"
ENTERO = r"[1-9][0-9]*"
PARENTESIS_IN = r"\("
END_LINEA = r";"
PARENTESIS_OUT = r"\)"
DECLARACION = r"(?:int|bool|str)\ +[A-Za-z][A-Za-z0-9]*\ *;"
OPER_SIMBOLO = r"(?:\+|-|\/|\*|<|==)"  
OPER_BIN = fr"(?:(?:{VARIABLE}|{BOOLEANO}|{STRING}|{ENTERO})\ *{OPER_SIMBOLO})+\ *(?:{VARIABLE}|{BOOLEANO}|{STRING}|{ENTERO})"
COND_SIMBOLO = r"(?:<|==)"  
CONDICION = fr"(?:(?:{VARIABLE}|{BOOLEANO}|{STRING}|{ENTERO})\ *{COND_SIMBOLO})+\ *(?:{VARIABLE}|{BOOLEANO}|{STRING}|{ENTERO})"  
IN_BLOQUE = r"(?:\{)"
OUT_BLOQUE = r"(?:\})"
CONDICIONAL_IF = fr"(?:if\s*{PARENTESIS_IN})(?:\s*|{CONDICION}|\s*)+(?:{PARENTESIS_OUT})"
CONDICIONAL_ELSE = fr"(?:else\s*)"
IGUAL = fr"(?:{VARIABLE})(?:\s*=)(?:\ *|(?:{OPER_BIN}|{VARIABLE}|{BOOLEANO}|{STRING}|{ENTERO})|\ *)*(?:\s*{END_LINEA}\ *)"
CICLO = fr"(?:while\s*{PARENTESIS_IN})(?:\s*|{CONDICION}|\s*)+(?:{PARENTESIS_OUT})"
START_MAIN = fr"int\s+main\(\)\s*{IN_BLOQUE}"
END_MAIN = fr"(?:\s*return\s*0)\s*{END_LINEA}\s*{OUT_BLOQUE}"
NOT_PROBAR = fr"{START_MAIN}|{END_MAIN}|{IN_BLOQUE}|{OUT_BLOQUE}|{END_MAIN}|{END_LINEA}|{PARENTESIS_IN}|{CONDICION}|{OPER_BIN}|{PARENTESIS_OUT}|{DECLARACION}|{CONDICIONAL_IF}|{CONDICIONAL_ELSE}|{CICLO}|{IGUAL}|[^\s]+"
PROBAR = fr"{START_MAIN}|{END_MAIN}|{IN_BLOQUE}|{OUT_BLOQUE}|{END_MAIN}|{END_LINEA}|{PARENTESIS_IN}|{CONDICION}|{OPER_BIN}|{PARENTESIS_OUT}|{DECLARACION}|{CONDICIONAL_IF}|{CONDICIONAL_ELSE}|{CICLO}|{IGUAL}"
pattern = r"([;{}])"



with open("codigo.txt", "r") as archivo:
    contenido = archivo.read()



tokens = re.findall(PROBAR, contenido)


not_tokens = re.findall(NOT_PROBAR, contenido)
flag = False
i=0
for token in not_tokens:
    if (re.match(PROBAR, token) == None):
        
        flag = True
        break
    else:
        i+=1

if(flag):
    tokens = tokens[0:i]

match = re.search(START_MAIN, contenido)

size_tokens=len(tokens)
 
flag2 = True

if(match == None):
    with open("formateado.txt", "w") as f:
        f.write("")
    flag2 = False    


elif(match.start()!=0):
    with open("formateado.txt", "w") as f:
        f.write("")
    flag2 = False

final=0

for i, elemento in enumerate(tokens):
    if re.search(END_MAIN, elemento):
        final=i
        

if(final != size_tokens-1 and flag == False):
    tokens=tokens[0:final-1]
    flag=True


i = 0
ExisteIf = False
for token in tokens:
    i += 1
    if len(token) >= 2 and token[0:2] == "if":
        ExisteIf = True
    elif len(token) >= 4 and token[0:4] == "else":
        if(ExisteIf == False):
            tokens=tokens[0:i-1]
            flag = True
        ExisteIf=False

if(flag == False):
    i = 0
    pila = []
    for token in tokens:
        i += 1
        if token == "{":
            pila.append(i)
        elif token == "}":
            if(len(pila)==0):
                tokens=tokens[0:i-1]
            else:
                pila.pop()
    if len(pila) != 0:
        i = pila.pop()
        tokens=tokens[0:i-1]

# leer_configuracion
# -------------------------
# Sin parámetros
# -------------------------
# Lee el archivo de configuración "config.txt" y devuelve una tupla con tres valores: espacios, saltos de línea y tabs.
def leer_configuracion():
    with open("config.txt", "r") as f:
        config = f.read().split()
        return tuple(map(int, config))

# quitar_saltos_de_linea
# -------------------------
# Parametro 1 : codigo (str)
# -------------------------
# Remueve todos los saltos de línea en el código y devuelve el código modificado.
def quitar_saltos_de_linea(codigo):
    return codigo.replace('\n', '')

# formatear_codigo1
# -------------------------
# Parametro 1 : codigo (str)
# Parametro 2 : config (tuple)
# -------------------------
# Aplica espacios, saltos de línea y tabs según la configuración dada, y devuelve el código formateado.
def formatear_codigo1(codigo, config):
    espacios, saltos_de_linea, tabs = config
    resultado = []
    texto = ""
    posicion = 0
    for linea in codigo:
        linea = linea.strip()
        linea = quitar_saltos_de_linea(linea)
        linea = re.sub(r"\s*\{\s*","{", linea)
        linea = re.sub(r"\s*\}\s*","}", linea)
        linea = re.sub(rf"\s*{END_LINEA}\s*", " " * espacios + ";", linea)
        linea = re.sub(r"\s*\(\s*", " " * espacios + "(" + " " * espacios, linea)
        linea = re.sub(r"\s*\)\s*", " " * espacios + ")"+ " " * espacios, linea)
        linea = re.sub(r"\s*\+\s*", " " * espacios + "+" + " " * espacios, linea)
        linea = re.sub(r"\s*\-\s*", " " * espacios + "-" + " " * espacios, linea)
        linea = re.sub(r"\s*\*\s*", " " * espacios + "*" + " " * espacios, linea)
        linea = re.sub(r"\s*/\s*", " " * espacios + "/" + " " * espacios, linea)
        
        

        if("==" in linea):
            linea = re.sub(r"\s*==\s*", " " * espacios + "==" + " " * espacios, linea)
        else:
            linea = re.sub(r"\s*=\s*", " " * espacios + "=" + " " * espacios, linea)

        linea = re.sub(r"\s+", " ", linea)
        resultado.append(linea)
    texto="".join(resultado) 
    nuevo_texto = re.sub(pattern, r"\1"+"\n"*saltos_de_linea, texto)
    resultado = []
    resultado = nuevo_texto.splitlines()
    return resultado
# formatear_codigo2
# -------------------------
# Parametro 1 : codigo (str)
# Parametro 2 : config (tuple)
# -------------------------
# Aplica indentación basada en bloques (usando tabs) según la configuración dada y devuelve el código formateado.
def formatear_codigo2(codigo, config):
    espacios, saltos_de_linea, tabs = config
    indentacion = 0
    linea = []
    final = []
    for lineas in codigo:
        if("{" in lineas):
            lineas = "\t"*indentacion+lineas
            final.append(lineas)
            indentacion += 1
        elif("}" in lineas):
            indentacion -= 1
            lineas = "\t"*indentacion+lineas
            final.append(lineas)        
        else:
            lineas = "\t"*indentacion+lineas
            final.append(lineas)
    return "\n".join(final)

config = leer_configuracion()
codigo_formateado1 = formatear_codigo1(tokens, config)
codigo_formateado2 = formatear_codigo2(codigo_formateado1, config)
if(flag2):
    with open("formateado.txt", "w") as f:
        f.write(codigo_formateado2)

