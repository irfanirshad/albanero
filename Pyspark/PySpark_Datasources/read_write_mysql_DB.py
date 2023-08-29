# NEEDS FIX: integrate localhost mysql driver ...
'''
Demonstrates reading and writing from a mysql DB.

FIX: try a localhost mysql
URL: https://sparkbyexamples.com/pyspark/pyspark-read-and-write-mysql-database-table/
'''
from pyspark.sql import SparkSession


spark = SparkSession.builder \
           .appName('example_rw_mysql') \
           .config("spark.jars", "mysql-connector-java-8.0.13.jar") \
           .getOrCreate()

# create df
columns = ["id", "name","age","gender"]
data = [(1, "James",30,"M"), (2, "Ann",40,"F"),
    (3, "Jeff",41,"M"),(4, "Jennifer",20,"F")]

sampleDF = spark.sparkContext.parallelize(data).toDF(columns)

# 
# Write2mysql table
# specify query with dbtable such as '.option("dbtable", "select id,age from employee where gender='M'")'
sampleDF.write \
  .format("jdbc") \
  .option("driver","com.mysql.jdbc.Driver") \
  .option("url", "jdbc:mysql://localhost:3306/database_name") \
  .option("dbtable", "employee") \
  .option("user", "root") \
  .option("password", "root") \
  .save()

# read from DB
df = spark.read \
    .format("jdbc") \
    .option("driver","com.mysql.jdbc.Driver") \
    .option("url", "jdbc:mysql://localhost:3306/database_name") \
    .option("dbtable", "employee") \
    .option("user", "root") \
    .option("password", "root") \
    .load()

df.show()
