import ply.lex as lex

# Lista de tokens
tokens = (
    'SELECT',
    'FROM',
    'WHERE',
    'IDENTIFIER',
    'OPERATOR',
    'COMMA',
    'NUMBER'
)

# Regras de RE para tokens
t_SELECT = r'(?i)select'
t_FROM = r'(?i)from'
t_WHERE = r'(?i)where'
t_IDENTIFIER = r'[a-zA-Z_]\w*'
t_OPERATOR = r'[<>=]+'
t_COMMA = r','

def t_NUMBER(t):
    r'[\+-]?\d+'
    t.value = int(t.value)
    return t

# Ignorar espaços em branco e tabulações
t_ignore = ' \t'

# Nova linha
def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)

# Erro de token
def t_error(t):
    print(f"Carácter ilegal: {t.value[0]}")
    t.lexer.skip(1)

# Construir o analisador léxico
lexer = lex.lex()

# Teste
data = "Select id, nome, salario From empregados Where salario >= 820"
lexer.input(data)

while tok := lexer.token():
    print(tok)