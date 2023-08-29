import pyspark
from pyspark.sql import SparkSession
from pyspark.sql.types import StructType,StructField, StringType, IntegerType 
from pyspark.sql.types import ArrayType, DoubleType, BooleanType
from pyspark.sql.functions import col,array_contains

spark = SparkSession.builder.appName('example').getOrCreate()

df = spark.read.csv("/home/albanero/Downloads/zipcodes.csv")

df.printSchema()

df2 = spark.read.option("header",True) \
     .csv("/home/albanero/Downloads/zipcodes.csv")
df2.printSchema()
print(f"df2 is \t => ::: {df2}")


df3 = spark.read.options(header='True', delimiter=',') \
  .csv("/home/albanero/Downloads/zipcodes.csv")
df3.printSchema()
print(f"df3 is \t => ::: {df3}")

schema = StructType() \
      .add("RecordNumber",IntegerType(),True) \
      .add("Zipcode",IntegerType(),True) \
      .add("ZipCodeType",StringType(),True) \
      .add("City",StringType(),True) \
      .add("State",StringType(),True) \
      .add("LocationType",StringType(),True) \
      .add("Lat",DoubleType(),True) \
      .add("Long",DoubleType(),True) \
      .add("Xaxis",IntegerType(),True) \
      .add("Yaxis",DoubleType(),True) \
      .add("Zaxis",DoubleType(),True) \
      .add("WorldRegion",StringType(),True) \
      .add("Country",StringType(),True) \
      .add("LocationText",StringType(),True) \
      .add("Location",StringType(),True) \
      .add("Decommisioned",BooleanType(),True) \
      .add("TaxReturnsFiled",StringType(),True) \
      .add("EstimatedPopulation",IntegerType(),True) \
      .add("TotalWages",IntegerType(),True) \
      .add("Notes",StringType(),True)
      
df_with_schema = spark.read.format("csv") \
      .option("header", True) \
      .schema(schema) \
      .load("/home/albanero/Downloads/zipcodes.csv") \

print(df_with_schema.printSchema())

df2.write.option("header",True) \
 .csv("/home/albanero/Downloads/zipcodes12345.csv")
