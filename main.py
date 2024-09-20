import fitz  # PyMuPDF
import pandas as pd

def extrair_texto(pdf_path, pagina_num, bbox):  #função responsavel por extrair o texto
    pagina = fitz.open(pdf_path).load_page(pagina_num)
    return pagina.get_text("text", clip=fitz.Rect(bbox)).strip()


pdf_path =
pagina_num = 0  #a pag do pdf

# coordenadas de cada elemento
coordenadas = {
    "emitente": (109, 84, 274, 100),
    "cnpj": (395, 214, 503, 227),
    "data_de_emissao": (514, 244, 574, 257),
    "valor": (442, 493, 464, 501)
}

# guarda as infos extraidas em sua variavel correspondente
emitente, cnpj, data_de_emissao, valor = [
    extrair_texto(pdf_path, pagina_num, bbox) for bbox in coordenadas.values()
]

dados = {
    "Emitente": [emitente],
    "CNPJ": [cnpj],
    "Data de Emissão": [data_de_emissao],
    "Valor": [valor]
}

df = pd.DataFrame(dados)

# Salvar o DataFrame em um arquivo CSV
df.to_csv('dadosextraidos.csv', mode='a', header=False, index=False, encoding='utf-8')


print(f"Emitente: {emitente}")
print(f"CNPJ: {cnpj}")
print(f"Data de Emissão: {data_de_emissao}")
print(f"Valor: {valor}")
