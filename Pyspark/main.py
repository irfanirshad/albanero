'''Code examples of Pyspark
'''

# Create a session 
from pyspark.sql import SparkSession

spark = SparkSession.builder.getOrCreate()

print(spark)