# Pyspark 


## What is Spark?

A general purpose distributed system with a nice API
Successor to MapReduce/Hadoop

## Different pieces of Spark

Apache Spark: Outer-most component
    - SQL & DataFrames
        - Spark ML
    - Streaming
    - Language APIs
        - Scala, Java, Python, R
    - Graph Tools
        - bagel & Grah X
    - MLLib
    - Community Packages

## RDDs: Spark's Primary abstraction

RDD (Resilient Distributed Dataset)

- Recomputed on node failure
- Distributed across the cluster
- Lazily evaluated (transformations & actions)



## DataFrames

DataFrames are a fundamental abstraction in PySpark that allow you to work with structured data in a distributed and efficient manner. 

- Useful for structured data
- support schema inference on JSON
- Many operations done without pickling
- Intergrated into ML
- Accessed through SQLContext
- Not the same feature set as Panda's or R DataFrames
- Has built-in save-formats such as JSON, Parquet etc.

### DataFrames are not as lazy

- Keeps track of schema information
- Loading JSON data involves looking at data


### DataFrames to RDD's & vice-versa

- Map lets us work per-row
    - df.map(lambda row: row.text)
- Converting back 
    - infer_schema
    - specify schema


### UDF (User-defined functions)

```python3 
def function(x):
    # Some magic
sqlContext.registerFunction("name", function, IntegerType())
```



## Hands-on:

See .py files for hands-on code snippets taken from docs..


## Q & A

```
PySpark:
	- Dataframes
	- Why is Pyspark needed?
	- Pyspark vs Pandas
	- CSV files in Pyspark(read, write, transform)
		- Play around with this
```

1. **DataFrames**

- DFs offer a structured and efficient way to work with large datasets in parallel by allowing you to perform various data
manipulation tasks such as filtering, transforming, aggregating and joining.


2. **Why is Pyspark Needed?**

- It's needed for handling & processing large-scale datasets that are too big to be processes using traditional tools like Pandas, especially when data doesn't fit into memory. 

- PySpark distributes data across cluster of computers enabling parallel processing...

3. **Pyspark vs Pandas**

- PySpark: 
    - Designed for big data processing which doesn't fit inside memory . 
    - Good for large-scale data processing, ML & Data streaming.
- Pandas: 
    - Suitable for smaller datasets that can fit into memory on a single machine. 
    - Excellent for EDA, data cleaning & data manipulation

4. **CSV Files in PySpark**

- Read CSV Files:
    - You can reads CSV files using ```spark.read.csv()``` method. Options like 'header' and 'inferSchema' allow you to specify whether first row contains column names and whether the schema should be inferred. 

- Write CSV Files:
    - To write DFs as CSV files, you can use ```DataFrame.write.csv()``` method. You can also specify various options such as file format, compression and more.

- Transforming CSV Data...
    - Pyspark's DFs support various transformation operations like filtering, selecting, aggregating and joining which can be applied to CSV data just like any other DataFrame. 
