import fitz  # PyMuPDF
import pandas as pd

def extrair_texto(pdf_path, pagina_num, bbox):  #função responsavel por extrair o texto
    pagina = fitz.open(pdf_path).load_page(pagina_num)
    return pagina.get_text("text", clip=fitz.Rect(bbox)).strip()


pdf_path = r"C:\Users\efran\OneDrive\Área de Trabalho\estudos_ufal\tea_eletiva\aut_extracao_de_texto\nfe\download (1).pdf"
pagina_num = 0  #a pag do pdf

# coordenadas de cada elemento
coordenadas = {
    "emitente": (31, 698, 181, 706),
    "cnpj": (120, 39, 180, 44),
    "data_de_emissao": (31, 712, 61, 720),
    "data_de_vencimento": (394, 683, 424, 692),
    "valor": (226, 170, 277, 185)
}

# guarda as infos extraidas em sua variavel correspondente
emitente, cnpj, data_de_emissao, data_de_vencimento, valor = [
    extrair_texto(pdf_path, pagina_num, bbox) for bbox in coordenadas.values()
]


dados = {
    "Emitente": [emitente],
    "CNPJ": [cnpj],
    "Data de Emissão": [data_de_emissao],
    "Data de Vencimento": [data_de_vencimento],
    "Valor": [valor]
}

df = pd.DataFrame(dados)

# Salvar o DataFrame em um arquivo CSV
df.to_csv('dadosextraidos.csv', mode='a', header=False, index=False, encoding='utf-8')


print(f"Emitente: {emitente}")
print(f"CNPJ: {cnpj}")
print(f"Data de Emissão: {data_de_emissao}")
print(f"Data de Vencimento: {data_de_vencimento}")
print(f"Valor: {valor}")

