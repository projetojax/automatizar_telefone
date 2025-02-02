import os
import pandas as pd
import requests
from bs4 import BeautifulSoup
import re

def load_csv_to_dataframe(
    file_path: str = None
):
    try:
        csv_dataframe = pd.read_csv(file_path, sep=",")
        return csv_dataframe
    except FileNotFoundError:
        raise FileNotFoundError("Arquivo não encontrado.")

def export_dataframe_to_csv(
    export_data : pd.DataFrame = pd.DataFrame(), output_file_path: str = None
):

    if not output_file_path.endswith(".csv"):
        raise ValueError("O arquivo de saída deve ser um arquivo CSV.")
    if os.path.exists(output_file_path):
        raise FileExistsError("O arquivo de saída já existe.")
    if export_data is None:
        raise ValueError("O DataFrame a ser exportado não pode ser nulo.")
    if not isinstance(export_data, pd.DataFrame):
        raise ValueError("O objeto a ser exportado deve ser um DataFrame.")

    try:
        export_data.to_csv(output_file_path, index=False)
    except Exception as e:
        raise Exception(f"Erro ao exportar o DataFrame para CSV: {e}")

def sanitize_phone_number(
    phone_number: str = None
):
    sanitized_phone_number = re.sub(r'[()\- ]', '', phone_number)
    return sanitized_phone_number

def find_phone_numbers(
    business_name: str = None, neighborhood: str = None, city: str = None
) -> list:

    search_query_url = f'https://www.google.com/search?q={business_name}+{neighborhood}+{city}'
    response = requests.get(search_query_url)
    soup = BeautifulSoup(response.text, 'html.parser')
    try:
        soup = str(soup)
        phone_number_pattern = r'\(?\d{2}\)?\s?\d{4,5}-?\d{4}|\b0800\s?\d{3}\s?\d{4}\b|\b4004\s?\d{3}\s?\d{4}\b'
        extracted_phone_numbers = re.findall(phone_number_pattern, soup)
        unique_phone_numbers = []
        for phone_number in extracted_phone_numbers:
            sanitized_phone_number = sanitize_phone_number(phone_number)
            if sanitized_phone_number not in unique_phone_numbers:
                unique_phone_numbers.append(sanitized_phone_number)
    except:
        unique_phone_numbers = []
    
    return unique_phone_numbers

def execute_bot(
    input_csv: str = "input.csv",
    output_csv: str = "output.csv"
):

    if not input_csv.endswith(".csv"):
        raise ValueError("O arquivo de entrada deve ser um arquivo CSV.")
    if not output_csv.endswith(".csv"):
        raise ValueError("O arquivo de saída deve ser um arquivo CSV.")
    if os.path.exists(output_csv):
        try:
            os.remove(output_csv)
        except Exception as e:
            raise FileExistsError(f"Não foi possível deletar o arquivo de saída existente: {e}")

    if not os.path.exists(input_csv):
        raise FileNotFoundError("O arquivo de entrada não foi encontrado.")
    if os.path.exists(output_csv):
        raise FileExistsError("O arquivo de saída já existe.")

    try:

        df = load_csv_to_dataframe(input_csv)
        df["tels"] = df.apply(lambda row: " ".join(find_phone_numbers(row["nome_empresa"], row["bairro_empresa"], row["cidade_empresa"])), axis=1)
        export_dataframe_to_csv(df, output_csv)

    except Exception as e:
        raise Exception(f"Erro ao rodar o bot: {e}")
