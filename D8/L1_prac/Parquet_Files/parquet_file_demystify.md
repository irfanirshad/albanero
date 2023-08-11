## Apache Parquet File: ~50x faster than classic CSV  

##### url: https://towardsdatascience.com/demystifying-the-parquet-file-format-13adb0206705

Have you ever used pd.read_csv() in pandas? Well, that command could have run ~50x faster if you had 
used parquet instead of CSV.


## TLDR;

Apache Parquet provides efficient storage and fast read speed .....
Use a hybrid storage format which squentially stores chunks of columns leading to high performance
in: 
    - selecting data
    - filtering data.
Provides support for strong compressiong algorithm support(gzip , LZO). Has other tricks for reducing file scans and encoding repeat variables...



### Thoughts - I

The best CSV is no CSV

CSV is a bad format. Besides the inefficiency of parsing it, the lack of type data means parsing is always going to be more error-prone and ambiguous than a structured file format with actual column types. So if you can, avoid using CSV and use a better format, for example Parquet.

## Read Speed and Size on Disk

1. Read speed: How fast we can access and decode information from binary files..

2. Size on disk: How much space our file needs when in binary format


Write Speed also matters here but for now we'll just focus on the above two ...



## 87% less space and 34x queries faster( 1 TB of data, S3 storage) -> PARQUET FILES 
CSVs are row-orientated, which means they’re slow to query and difficult to store efficiently. That’s not the case with Parquet, which is a column-orientated storage option. The size difference between those two is enormous for identical datasets, as you’ll see shortly.

Adding insult to injury, anyone can open and modify a CSV file. That’s why you should never use this type of format as a database. There are safer alternatives.

But let’s dial into what’s really important to companies — time and money. You’ll likely store data in the cloud, either as a basis for web applications or machine learning models. Cloud service providers will charge you based on the amount of data scanned or the amount of data stored. Neither looks good for CSVs.


## Why is it faster? Parquet Core Features

### Hybrid Storage Layout

THink about when we convert a 2-Dimensional table to a sequence of 0's and 1's, we must think carefully about an optimal structure....
Traditionally , there are three ways to convert a 2-d dim table down to a 1-D:
    -   Row-based: sequentially store rows(CSV)
    -   Column-based: sequentially store columns (ORC)
    -   Hybrid-base: sequentially store chunks of columns (Parquet)

Eg: Hybrid base (row group size=2) is the secret to faster performance..

### Projection and Predicate 

Projection is the process of selecting columns — you can think of it as the SELECT statement in a SQL query. Projection is best supported by a column-based layout

Predicates is the criteria used to select rows —you can think of it as the WHERE clause in a SQL query.
Predicates are best supported by row-based storage

In both of these scenarios, we are looking to traverse as little of the file as possible.

### Parquet Tricks 101:

Parquet intelligently solves this by storing max and min values for each row group, allowing us to skip entire row groups, as shown in figure 4. But that’s not all
ince parquet often writes many .parquet files to a single directory, we can look at the column metadata for an entire file in and determine whether it should be scanned.


By including some extra data, we are able to skip chunks of our data and dramatically increase query speeds.....

#### url : https://parquet.apache.org/docs/file-format/metadata/



### Parquet File Structure:

Overall, parquet follows the below structure. Let’s take a look at each one in turn…

    Root > Parquet Files > Row Groups > Columns > Data Page

...

### Additional Optimizations 

Features for certain types of data

1. My Data has lots of duplicate values

Solution: Run-Length Encoding(RLE)

Let’s say we have a column with 10,000,000 values, but all the values are 0. To store this information, we just need 2 numbers: 0 and 10,000,000 —the value and the number of times it repeated.

RLE does just that. When many sequential duplicates are found, parquet can encode that information as a tuple corresponding to the value and the count. In our example, that would save us from storing 9,999,998 numbers.


2. My data has very big types

Solution: Dictionary Endoing with Bit-Packing

Let's say we have a column that contains country names, some of which are very long.

Dictionary encoding replaces each value in our column with a small integer and stores the mapping in our data page’s metadata. When on disk, our encoded values are bit-packed to take up the least amount of space possible, but when we read the data we can still convert our column back to its original values.

3. I'm using complex filters on my data 

Solution: Projection and Predicate PushDown

In a spark environment, we can avoid reading an entire table into memory through projection and predicate pushdown. Because spark operations are lazily evaluated, meaning they aren’t executed until we actually query data, spark can pull the least amount of data into memory.

As a quick reminder, predicates subset rows and projection subsets columns. So, if we know we only need a few columns and a subset of the rows, we don’t actually have to read the full table into memory — it’s filtered during the read.


4. I have lots of different data

Solution: DeltaLake

Finally, Deltalake is an open-source “lakehouse” framework that combines the dynamic nature of a data lake with the structure of data warehouse. If you plan on using parquet as the base of your organization’s data warehouse, additional features such as ACID guarantees and transaction logs are really beneficial.