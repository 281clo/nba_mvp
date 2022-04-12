import findspark
findspark.init()
from pyspark.sql import SparkSession

if __name__ == '__main__':
    spark = SparkSession.builder\
    .appName("Read from S3")\
    .master("local[*]")\
    .getOrCreate()
    
    df = spark.read\
        .format("csv")\
        .option("header", "true")\
        .option("inferSchema", "true")\
        .csv("cleaned_data/clean_nickname.csv")
    df.printSchema()
    df.show(truncate=False)
    