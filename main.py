'''
DESAFIO:
Crie um programa que gere o e-mail institucional de um aluno a partir 
do seu nome.
'''

# Função center para centralizar o texto em 40 espaços.
print("=" * 40)
print("GERADOR DE EMAIL INSTITUCIONAL".center(40))
print("=" * 40)

# Lista contendo alguns dos "nomes" que queremos ignorar:
excecoes = ["de", "do", "da", "dos", "das"]

# Função lower será utilizada para que possamos converter todo o nome
# para minúsculo antes de salvarmos o valor na variável nome_completo.
nome_completo = input("Qual é o nome completo do aluno? ").lower()

# Função split é responsável por separar uma string em pedaços
# delimitados por um caracter especifico. O padrão é o " ".
nomes_separados = nome_completo.split()

# Iniciamos a variável com um texto vazio para que ele possa ser preenchido 
# durante o percurso da lista.
email_institucional = ""

# Estrutura de repetição para percorremos toda a lista, elemento por elemento.
for nome in nomes_separados:
    # Se o nome não estiver dentro de excecoes...
    if nome not in excecoes:
        # Lembre-se que em uma string (texto) os elementos possuem índices.
        # Acessamos os elementos utilizando: variavel_string[indice]
        primeira_letra = nome[0]
        # Pegaremos a primeira letra de cada um dos nomes e 
        # adicionaremos à variável email_institucional:
        email_institucional = email_institucional + primeira_letra
    
# Finalmente adicionaremos a extensão padrão ao final da variável:
email_institucional = email_institucional + "@discente.ifpe.edu.br"

print(f"O email institucional é: {email_institucional}")
