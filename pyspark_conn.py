from pyspark.sql import SparkSession


spark = SparkSession.builder.appName("Read from S3").master("local[*]").getOrCreate()
    
spark._jsc.hadoopConfiguration().set("fs.s3a.access.key", "AKIAYQXFRQHBMY7TPAAH")
spark._jsc.hadoopConfiguration().set("fs.s3a.secret.key", "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")
spark._jsc.hadoopConfiguration().set("fs.s3a.endpoint", "s3.amazonaws.com")


    
df = spark.read.format("csv").option("header", "true").option("inferSchema", "true").csv("s3a://mvpdata2022/cleaned_data/clean_nickname.csv/")
df.printSchema()
df.show(truncate=False)
    