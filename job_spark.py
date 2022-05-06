# Comentário para modificar o arquivo .py
# Job para ler dado no s3 e converter para parquet
from pyspark.sql.functions import mean, max, min, col, count
from pyspark.sql import SparkSession

spark = (
    SparkSession.builder.appName("ExerciseSpark")
    .getOrCreate()
    
)

enem = (
    spark
    .read
    .format("csv")    
    .option("header", True)
    .option("inferSchema", True)
    .option("delimiter", ";")
    .load("s3://datalake-elobo-edc/raw-data/enem/2019/")
)


(    
    enem
    .write
    .mode("overwrite")
    .format("parquet")
    .partitionBy("year")
    .save("s3://datalake-elobo-edc/staging/enem/")
)