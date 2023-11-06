#1
import random

resultados = [0, 0, 0, 0, 0, 0]


for _ in range(100):
    resultado_dado = random.randint(1, 6)
    
    
    resultados[resultado_dado - 1] += 1

for i in range(6):
    print(f"Valor {i+1} foi obtido {resultados[i]} vezes.")


#
import json

dados_alunos = {}

while True:
    matricula = input("Digite a matrícula do aluno (ou 'sair' para encerrar): ")
    
    if matricula.lower() == "sair":
        break

    nome = input("Digite o nome do aluno: ")
    email = input("Digite o e-mail do aluno: ")

    dados_alunos[matricula] = {"nome": nome, "e-mail": email}

with open("alunos.json", "w") as arquivo_json:
    json.dump(dados_alunos, arquivo_json, indent=4)

print("Os dados dos alunos foram salvos no arquivo alunos.json.")


#2
from datetime import datetime

def data_por_extenso(data_str):
    try:
        data = datetime.strptime(data_str, '%d/%m/%Y')
        data_formatada = data.strftime('%d de %B de %Y')
        return data_formatada
    except ValueError:
        return None

# Exemplo de uso da função
data_informada = input("Digite a data no formato DD/MM/AAAA: ")
data_formatada = data_por_extenso(data_informada)

if data_formatada:
    print("Data formatada:", data_formatada)
else:
   print("Data inválida. Por favor, insira uma data no formato DD/MM/AAAA válido.")

#3
from datetime import datetime

def converter_data_por_extenso(data_str):
    meses = [
        "Janeiro", "Fevereiro", "Março", "Abril",
        "Maio", "Junho", "Julho", "Agosto",
        "Setembro", "Outubro", "Novembro", "Dezembro"
    ]
    
    try:
        partes = data_str.split('/')
        if len(partes) == 3:
            dia, mes, ano = map(int, partes)
            data = datetime(ano, mes, dia)
            data_formatada = f"{data.day} de {meses[data.month - 1]} de {data.year}"
            return data_formatada
    except (ValueError, IndexError):
        pass

    
    return None
data_input = input("Digite uma data no formato DD/MM/AAAA: ")
data_por_extenso = converter_data_por_extenso(data_input)

if data_por_extenso:
    print("Data formatada:", data_por_extenso)
else:
    print("Data inválida. Por favor, insira uma data no formato DD/MM/AAAA válido.")