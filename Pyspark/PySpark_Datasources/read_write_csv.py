

from pyspark.sql import SparkSession


spark = SparkSession.builder.appName("ExcelProcessing").getOrCreate()


# Read a CSV file into DF
# spark = SparkSession.builder().master("local[1]"). \
#         appName("example1"). \
#         getOrCreate()

df = spark.read.csv("/home/albanero/Downloads/test_compare.csv")
print(df.printSchema())

# OR do it like this...


df1 = spark.read.format("csv") \
                  .load("/home/albanero/Downloads/test_compare.csv")

#or

df2 = spark.read.format("org.apache.spark.sql.csv") \
                  .load("/home/albanero/Downloads/test_compare.csv")



print(df1.printSchema())

print(df2.printSchema())
