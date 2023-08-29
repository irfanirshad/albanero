# TESTED -> WORKING
"""Write a DataFrame into a JSON file and read it back.
"""
import tempfile
from pyspark.sql import SparkSession

spark = SparkSession.builder.appName("CSVTransformation").getOrCreate()

with tempfile.TemporaryDirectory() as d:
    # Write a DataFrame into a JSON file
    spark.createDataFrame(
        [{"age": 100, "name": "Hyukjin Kwon"}]
    ).write.mode("overwrite").format("json").save(d)

    # Read the JSON file as a DataFrame.
    spark.read.format('json').load(d).show()



"""
        +---+------------+
        |age|        name|
        +---+------------+
        |100|Hyukjin Kwon|
        +---+------------+
"""