'''Given a scenario, where we have a file of 10GB size while our system merely only has 4GB RAM , how will you accomplish
the task of reading, transforming and writing this 10GB file.
You are allowed to leverage the power of Pandas and Pyspark.(Vanilla Python + Pandas + Pyspark)
'''


'''Idea #1
The idea is to use PySpark to process the data in chunks and then write each chunk to an Excel file using Pandas. 
This approach allows you to work with large datasets that don't fit into memory while taking 
advantage of Pandas' Excel writing capabilities.


1. Use PySpark to Read and Process in Chunks:
Use PySpark to read and process the large dataset in smaller chunks. You can use the DataFrameReader API's 
option("inferSchema", "true") to infer the schema from the data while reading the Excel file. Process each chunk using PySpark's
transformation operations.

2. Convert Chunks to Pandas DataFrames:
After processing each chunk, convert it to a Pandas DataFrame. This involves collecting the data from the PySpark DataFrame 
into a Pandas DataFrame. Since you're working with chunks, the amount of data you collect into memory at a time is limited.

3. Use Pandas to Write Chunks to Excel:
Use Pandas to write the processed chunk to an Excel file. The Pandas to_excel() function supports writing data in chunks by
specifying the chunksize parameter. This allows you to write data to the Excel file in manageable portions that fit within 
your available memory.

4. Repeat for Each Chunk:
Repeat steps 1 to 3 for each chunk of data until all the data has been processed and written to the Excel file.


By processing the data in chunks and using Pandas' ability to write data in chunks to Excel,
you can effectively work with large datasets even when your available memory is limited.
'''


import pandas as pd
from pyspark.sql import SparkSession

spark = SparkSession.builder.appName("ExcelProcessing").getOrCreate()

# We're using pandas with chunking to avoid all the in-memory loading file
# Chunking 
chunk_size = 10000
for chunk in pd.read_excel("large_data.xlsx", chunksize=chunk_size):
    # Chunk2PySpark DF
    spark_df = spark.createDataFrame(chunk)

    # Spark2Pandas DF
    transformed_chunk = spark_df.toPandas()
    
    transformed_chunk.to_excel("transformed_output.xlsx", index=False, mode="a")

spark.stop()
