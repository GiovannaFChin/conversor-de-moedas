import requests
def conversor(valor,de,para):
    de=de.lower()
    para=para.lower()
    url = f"https://economia.awesomeapi.com.br/json/last/{de}-{para}"
    resposta=requests.get(url)

    if resposta.status_code!=200:
        print('erro ao acessar api')
        return None
    
    dados=resposta.json()
    chave=f"{de.upper()}{para.upper()}"

    if chave in dados:
        cotacao=float(dados[chave]['bid'])
        return valor*cotacao
    else:
        print('erro: moeda não encontrada')
        return None


print('------>conversor de moedas<------')
de_moeda=input('Converter de (ex: BRL):').upper()
para_moeda=input('Para (ex: USD):').upper()

try:
    valor=float(input(f"Quantos {de_moeda} você deseja converter?"))
    resultado=conversor(valor,de_moeda,para_moeda)

    if resultado is not None:
        print(f'\n{valor}{de_moeda}={round(resultado,2)}{para_moeda}')
    else:
        print('Não foi possível realizar a conversão')
except ValueError:
    print('Por favor, digite um valor numérico válido')

