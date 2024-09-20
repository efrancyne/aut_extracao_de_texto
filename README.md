# Extração Automática de Informações de Notas Fiscais (DANFE) com Python

## Descrição do Projeto
Este projeto foi desenvolvido para a disciplina de Tópicos Especiais de Automação e tem como objetivo automatizar o processo de extração de informações de Notas Fiscais Eletrônicas (DANFE) e a geração de um arquivo csv para armazenar as informações. Utilizando Python e as bibliotecas PyMuPDF e Pandas, o sistema lê e organiza os dados presentes nos arquivos PDF das notas fiscais, gerando automaticamente um arquivo CSV com as informações extraídas.

## Funcionalidades
- Extração de dados estruturados de arquivos PDF de DANFE.
- Organização e manipulação dos dados com o uso de Pandas.
- Geração automática de um arquivo CSV contendo as informações extraídas.
- Possibilidade de gerar relatórios ou planilhas para análise posterior.

## Tecnologias Utilizadas
- **Python**: Linguagem de programação principal.
- **PyMuPDF (fitz)**: Para manipulação e extração de texto de arquivos PDF.
- **Pandas**: Para organização e tratamento de dados em tabelas e geração do CSV.

## Pré-requisitos
Antes de executar o projeto, é necessário instalar as seguintes dependências:

```bash
pip install pymupdf pandas
