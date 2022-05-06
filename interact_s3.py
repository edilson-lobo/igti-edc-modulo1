import boto3
import pandas as pd

# Criar um cliente para interagir com o AWS S3
s3_client = boto3.client('s3')

s3_client.download_file('datalake-elobo-edc',
                        'data/dimensao_mesoregioes_mg.csv',
                        'data/dimensao_mesoregioes_mg.csv')


df = pd.read_csv('data/dimensao_mesoregioes_mg.csv', sep= ",")
print(df)

s3_client.upload_file("data/pnadc20203.csv",
                      "datalake-elobo-edc",
                      "data/pnadc20203.csv")


s3_client.upload_file("data/MICRODADOS_ENEM_2019.csv",
                      "datalake-elobo-edc",
                      "raw-data/enem/2019/MICRODADOS_ENEM_2019.csv")