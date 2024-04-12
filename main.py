
import requests
from fastapi import FastAPI,Query

app = FastAPI()

@app.get('/api/hello')
def hello_world():
    """EndPoint Hello World!"""
    return {'Hello':'World'}



@app.get("/api/restaurantes/")
def get_restaurantes(restaurante:str = Query(None)):
    """EndPoint para ver um restaurante específico e seu respectivo cardápio"""

    url = "https://guilhermeonrails.github.io/api-restaurantes/restaurantes.json"
    response = requests.get(url)

    print(response)

    if response.status_code == 200:
        dados_json = response.json() 
        print(dados_json)

        if restaurante is None:
            return {"Dados":dados_json}


        dados_restaurante = []
        
        for item in dados_json:
            
            if item["Company"] == restaurante:


                dados_restaurante.append({
                "Item":item["Item"],
                "Price":item["price"],
                "Description" : item["description"]
            })
        return {"Restaurante": restaurante,"cardapio":dados_restaurante}


    else:
        print(f"O Erro foi {response.status_code}")


#uvicorn main:app --reload comando para executar o arquiovo main.py do framework fastapi