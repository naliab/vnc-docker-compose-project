import sys
from pyspark.sql import SparkSession, SQLContext

def main():
    spark = SparkSession \
        .builder \
        .appName('Mean house price app') \
        .master('spark://spark-master:7077') \
        .config('spark.jars', '/jdbc.jar') \
        .getOrCreate()

    df = spark.read \
        .format('jdbc') \
        .option('url', 'jdbc:postgresql://db:5432/spark') \
        .option('dbtable', 'house_prices') \
        .option('user', 'spark_user') \
        .option('password', 'spark_password') \
        .option('driver', 'org.postgresql.Driver') \
        .load()

    df.createOrReplaceTempView('house_prices')

    spark.sql('''
        WITH cte AS (
            SELECT
                *, baths + bedrooms AS num_rooms
            FROM
                house_prices
        )
        SELECT
            city AS City,
            location AS Area,
            num_rooms AS Num_of_rooms,
            format_number(AVG(price), 2) AS house_and_flat_prices
        FROM
            cte
        WHERE
            property_type IN ("House", "Flat")
        GROUP BY
            city, location, num_rooms
        ORDER BY
            city, location, num_rooms
    ''').show(20)

if __name__ == '__main__':
        main()