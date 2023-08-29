
'''Write a DataFrame into a Parquet file in a partitioned manner, and read it back.'''

import tempfile
import os
with tempfile.TemporaryDirectory() as d:
    # Write a DataFrame into a Parquet file in a partitioned manner.
    spark.createDataFrame(
        [{"age": 100, "name": "Hyukjin Kwon"}, {"age": 120, "name": "Ruifeng Zheng"}]
    ).write.partitionBy("name").mode("overwrite").format("parquet").save(d)

    # Read the Parquet file as a DataFrame.
    spark.read.parquet(d).sort("age").show()

    # Read one partition as a DataFrame.
    spark.read.parquet(f"{d}{os.path.sep}name=Hyukjin Kwon").show()

"""+---+-------------+
|age|         name|
+---+-------------+
|100| Hyukjin Kwon|
|120|Ruifeng Zheng|
+---+-------------+
+---+
|age|
+---+
|100|
+---+"""