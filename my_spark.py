import sys
#import psycopg2
#from pyspark import SparkContext, SparkConf
from pyspark.sql import SparkSession, SQLContext

def main():
    spark = SparkSession \
        .builder \
        .appName("Mean house price app") \
        .master("spark://spark-master:7077") \
        .config("spark.jars", "/jdbc.jar") \
        .getOrCreate()

    df = spark.read \
        .format("jdbc") \
        .option("url", "jdbc:postgresql://db:5432/spark") \
        .option("dbtable", "house_prices") \
        .option("user", "spark_user") \
        .option("password", "spark_password") \
        .option("driver", "org.postgresql.Driver") \
        .load()

    df.printSchema()

if __name__ == "__main__":
        main()