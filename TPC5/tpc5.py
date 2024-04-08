import ply.lex as lex
import json
from datetime import datetime



def valor_to_int(value_str):

    transformed_value = 0

    if value_str.endswith('e'):
        if value_str in ['1e', '2e']:
            transformed_value = int(value_str[:-1])*100

    elif value_str.endswith('c'):
        if value_str in ['1c', '2c', '5c', '10c', '20c', '50c']:
            transformed_value = int(value_str[:-1])

    if transformed_value == 0:
        print(f"Moeda {value_str} não válida")
    
    return transformed_value



def int_to_valor(value):

    if (value == 0):
        return "0e"
    
    euros = value // 100
    cents = value % 100

    euros_str = f"{euros}e" if euros != 0 else ""
    cents_str = f"{cents}c" if cents != 0 else ""

    return euros_str + cents_str


def get_item_by_cod(cod):
    for item in stock:
        if item["cod"] == cod:
            return item
    return None

def buy_item(cod):
    for item in stock:
        if item["cod"] == cod:
            item["quant"] -= 1
            break

def calcular_troco(saldo):

    coins = {'2e': 0, '1e': 0, '50c': 0, '20c': 0, '10c': 0, '5c': 0, '2c': 0, '1c': 0}
    coin_values = {'2e': 200, '1e': 100, '50c': 50, '20c': 20, '10c': 10, '5c': 5, '2c': 2, '1c': 1}
    change = []
    
    for coin_name, coin_value in coin_values.items():
        while saldo >= coin_value:
            coins[coin_name] += int(saldo / coin_value)
            saldo = saldo % coin_value

        if coins[coin_name] > 0:
            change.append(f"{coins[coin_name]}x {coin_name}")
            
    return ", ".join(change)




# Read data from JSON file
with open('stock.json', 'r') as file:
    data = json.load(file)

# Extract stock information
stock = data['stock']



# Lista de tokens
tokens = (
    'LISTAR',
    'MOEDA',
    'VALOR',
    'SELECIONAR',
    'COD',
    'SAIR',
    'COMMA'
)


# Regras de RE para tokens
t_LISTAR = r'LISTAR'
t_MOEDA = r'MOEDA'
t_VALOR = r'\d+[ec]'
t_SELECIONAR = r'SELECIONAR'
t_COD = r'[A-Z]\d+'    # Convert integer to euros and cents

t_SAIR = r'SAIR'
t_COMMA = r','

t_ignore = ' \t\n'


def t_error(t):
    print(f"Carácter ilegal: {t.value[0]}")
    t.lexer.skip(1)


lexer = lex.lex()





# Get today's date
today_date = datetime.today().date()


print(f"maq: {today_date}, Stock carregado, Estado atualizado.")


print("maq: Bom dia. Estou disponível para atender o seu pedido.")

saldo = 0

while True:

    data = input(">> ")

    lexer.input(data)
    tok = lexer.token()

    if tok:

        if tok.type == 'SAIR':
            if (saldo>0):
                print(f"maq: Pode retirar o troco: {calcular_troco(saldo)}")
            print("maq: Até à próxima")
            break

        elif tok.type == 'LISTAR':

            format_str = "{:<5} | {:<30} | {:<10} | {:<5}\n"
            lista = format_str.format("cod", "nome", "quantidade", "preço")
            lista += "-" * 55 + "\n"

            for item in stock:
                lista += format_str.format(item['cod'], item['nome'], item['quant'], item['preco'])

            print(lista)
        

        elif tok.type == "MOEDA":

            while tok := lexer.token():
                
                if tok.type == "VALOR":

                    saldo += valor_to_int(tok.value)
            
            print("maq: Saldo = " + int_to_valor(saldo))
        
        
        elif tok.type == "SELECIONAR":

            tok = lexer.token()

            if (tok):

                if tok.type == "COD":

                    item = get_item_by_cod(tok.value)

                    if (item is None):
                        print("Não existe nenhum item com este código!")

                    elif(item["quant"] == 0):
                        print("Item sem stock")

                    elif (saldo>=item["preco"]*100):
                        print("maq: Pode retirar o produto dispensado: " + item["nome"])
                        saldo -= item["preco"]*100
                        buy_item(item["cod"])

                    else:
                        print("maq: Saldo insufuciente para satisfazer o seu pedido")
                        print(f"maq: Saldo = {int_to_valor(saldo)}; Pedido = {int_to_valor(item['preco'])}")

                else:
                    print("Tem de selecionar um código")
            
            else:
                print("Sem seleção de código")



#Como extra pode adicionar um comando para adicionar alguns produtos ao stock existente(produtos novos ou já existentes).