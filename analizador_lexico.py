import ply.lex as lex

# Palabras reservadas
reserved = {
    'CREATE': 'CREATE',
    'DATABASE': 'DATABASE'
}

tokens = [
    'SEMICOLON',
    'ID'
] + list(reserved.values())

# Reglas de tokens
t_SEMICOLON = r';'

def t_ID(t):
    r'[a-zA-Z_][a-zA-Z0-9_]*'
    t.type = reserved.get(t.value.upper(), 'ID')
    return t

# Ignorar espacios y saltos de línea
t_ignore = ' \n\t'

# Manejo de errores
def t_error(t):
    print(f"Carácter ilegal '{t.value[0]}'")
    t.lexer.skip(1)

# Construcción del analizador léxico
lexer = lex.lex()