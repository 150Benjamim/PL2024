
def parse_csv(file_path, emd_dict, modalidades, escaloes):

    with open(file_path, 'r') as file:

        # Skip the header line
        next(file)
        
        atletas_aptos = 0

        for line in file:

            # Remove newline character
            line = line.strip()
            
            # Split the line by comma
            values = line.split(',')
            
            # Extract _id and create dictionary entry
            _id = values[0]
            data = {
                "index": values[1],
                "dataEMD": values[2],
                "nome/primeiro": values[3],
                "nome/último": values[4],
                "idade": values[5],
                "género": values[6],
                "morada": values[7],
                "modalidade": values[8],
                "clube": values[9],
                "email": values[10],
                "federado": values[11],
                "resultado": values[12]
            }
            emd_dict[_id] = data

            modalidades.add(data["modalidade"])

            if data["resultado"] == "true":
                atletas_aptos += 1

            escalao_key = (int(data["idade"]) // 5) * 5
            escaloes[escalao_key] = escaloes.get(escalao_key,0) + 1        
        
        return atletas_aptos



# Dictionary with all users
emd_dict = {}

# Set to save modalidades
modalidades = set()

# Dictionary to save escaloes
escaloes = {}



atletas_aptos = parse_csv("emd.csv",emd_dict, modalidades, escaloes)



def print_modalidades(modalidades):
    print(f"Modalidades:\n{sorted(modalidades)}")


def print_atletas_aptos(atletas_aptos, emd_dict):
    total_atletas = len(emd_dict)
    atletas_aptos_percentagem = atletas_aptos/total_atletas * 100
    print(f'Atletas aptos: {atletas_aptos_percentagem}%')
    print(f'Atletas não aptos: {100-atletas_aptos_percentagem}%')

def print_escaloes(escaloes, emd_dict):
    total_atletas = len(emd_dict)
    sorted_escaloes = dict(sorted(escaloes.items()))    
    # Print the sorted escaloes
    for key, value in sorted_escaloes.items():
        print(f"[{key}-{key+4}]: {int(value)} atletas")



print_modalidades(modalidades)

print_atletas_aptos(atletas_aptos, emd_dict)

print_escaloes(escaloes,emd_dict)