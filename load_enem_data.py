import boto3
import pandas as pd

# Criar um cliente para interagir com o AWS S3
s3_client = boto3.client('s3')


s3_client.upload_file("data/MICRODADOS_ENEM_2020.csv",
                      "datalake-elobo-edc",
                      "raw-data/enem/2020/MICRODADOS_ENEM_2020.csv")


df_enem = pd.read_csv("MICRODADOS_ENEM_2020.csv", sep= ";")
print(df_enem)                     