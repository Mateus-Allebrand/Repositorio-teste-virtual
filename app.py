import requests
import json

url = "https://guilhermeonrails.github.io/api-restaurantes/restaurantes.json"

response = requests.get(url)

print(response)


if response.status_code == 200:
    dados_json = response.json() 
    print(dados_json)

    dados_restaurante = {}
    
    for item in dados_json:
        
        nome_restaurante = item["Company"]

        if nome_restaurante not in dados_restaurante:
            dados_restaurante[nome_restaurante] = []

        dados_restaurante[nome_restaurante].append({
            "Item":item["Item"],
            "Price":item["price"],
            "Description" : item["description"]
        })



else:
    print(f"O Erro foi {response.status_code}")

# print(dados_restaurante['McDonald’s'])

for nome_restaurante,dados in dados_restaurante.items():
    nome_do_arquivo = f"{nome_restaurante}.json "
    with open(nome_do_arquivo,"w") as arquivo_json:
        json.dump(dados,arquivo_json,indent=4)


# import requests

# url = "https://economia.awesomeapi.com.br/last/USD-BRL"
# response = requests.get(url)

# if response.status_code == 200:
#     data = response.json()


# print(data)