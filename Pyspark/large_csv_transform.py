# TESTED AND WORKING ...
'''This is a sample python script that demonstrates reading a large CSV file(~2GB) and performs 
a transformation of 2 or more columns to snake_case and write the transformed data to a new CSV file named
'transformed_output.csv'
'''


from pyspark.sql import SparkSession
from pyspark.sql.functions import lower, regexp_replace, upper
from pyspark.sql.types import StringType


spark = SparkSession.builder.appName("CSVTransformation").getOrCreate()

# i/p csv file. FIx this to work ...
csv_path = "/home/albanero/Downloads/test_compare.csv"

# Read CSV2PySpark DF
df = spark.read.csv(csv_path, header=True, inferSchema=True)


# simulating some transformation process 1 ... 

# Apply trim to each cell of the first two columns
columns_to_trim = ["first_name"]
for col_name in columns_to_trim:
    df = df.withColumn(col_name, upper(df[col_name]))

# transformation process 2
# Columns to transform to snake_case
#-x-x-x-x-
# columns_to_transform = ["column_name_1", "column_name_2"]
# for col_name in columns_to_transform:
#     df = df.withColumn(col_name, lower(regexp_replace(df[col_name], "[\s\-]", "_")).cast(StringType()))

# Write the transformed data to a new CSV file
output_csv_path = "/home/albanero/Downloads/output_OUTPUT9.csv"
df.write.csv(output_csv_path, header=True, mode="overwrite")

# Stop the SparkSession
spark.stop()


"""
Q) Are these operations being performed using chunking and NOT loading entire df in memory ... 

1. PySpark's DataFrame operations, like withColumn(), trim(), and regexp_replace(), are performed lazily
2. Here 
"""
