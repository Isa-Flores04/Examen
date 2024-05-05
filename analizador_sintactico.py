import ply.yacc as yacc
from analizador_lexico import tokens

# Definición de reglas sintácticas
def p_statement(p):
    '''
    statement : CREATE DATABASE ID SEMICOLON
    '''
    p[0] = f"CREATE DATABASE {p[3]};"

def p_error(p):
    if p:
        print(f"Error de sintaxis en el token '{p.value}' en la línea {p.lineno}")
    else:
        print("Error de sintaxis: No se pudo construir el árbol de análisis")

parser = yacc.yacc()

# Función de análisis
def parse_code(code):
    try:
        result = parser.parse(code)
        return result
    except Exception as e:
        return str(e)