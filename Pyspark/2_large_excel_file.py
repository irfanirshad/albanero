''' 
    Saw on this StackOverflow on how to handle reading, transforming & writing from large excel files
    without using Pandas. 

"""
        You need to install these 2 libraries on your databricks cluster to read excel files. Follow these paths to install:

        Clusters -> select your cluster -> Libraries -> Install New -> Maven -> in Coordinates: com.crealytics:spark-excel_2.12:0.13.5

        Clusters -> select your cluster -> Libraries -> Install New -> PyPI-> in Package: xlrd

        Now, you will be able to read your excel as follows:

        sdf = spark.read.format("com.crealytics.spark.excel") \
            .option("header", "true") \
            .option("inferSchema", "true") \
            .option("dataAddress", "'NameOfYourExcelSheet'!A1") \
            .load(filePath)
"""
-----x----x----x
'''


from pyspark.sql import SparkSession


spark = SparkSession.builder.appName("ExcelProcessing").getOrCreate()


# fix this to properly run
file_path = "path_to_your_excel_file.xlsx"

# Read Excel data into PySpark DataFrame
sdf = spark.read.format("com.crealytics.spark.excel") \
    .option("header", "true") \
    .option("inferSchema", "true") \
    .option("dataAddress", "'NameOfYourExcelSheet'!A1") \
    .load(file_path) # source file

# Perform a transformation step here
# Say, here , perform snake_case transformation on specific columns  
columns_to_transform = ["column_name_1", "column_name_2"]
for col_name in columns_to_transform:
    sdf = sdf.withColumn(col_name, lower(regexp_replace(sdf[col_name], "[\s\-]", "_")).cast(StringType()))

# Here NameOfYourExcelSheet = <Name_of_your_sheet>
# A1 - is the header
output_file_path = "transformed_output.xlsx"
sdf.write.format("com.crealytics.spark.excel") \
    .option("header", "true") \
    .option("dataAddress", "'NameOfYourExcelSheet'!A1") \
    .save(output_file_path) # o/p file




spark.stop()
