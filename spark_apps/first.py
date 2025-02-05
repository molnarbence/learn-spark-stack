from pyspark.sql import SparkSession, DataFrame
from pyspark.sql.functions import col, avg

import polars as pl

spark = SparkSession.builder.appName(
    "Hello world"
).getOrCreate()

df = pl.DataFrame({
        "name": ["Alice", "Bob", "Charlie"],
        "age": [24, 32, 45]
    })

print(df)

hello_df: DataFrame = spark.read.csv("/opt/spark/data/hello.csv", header=True)

average_age = hello_df.select(avg(col("age")))

average_age.write.csv("/opt/spark/data/out/hello_out.csv", header=True)