# Pymongo- TODO:

MongoDB with Vanilla Python
- CRUD with Upsert
- Bulk operation Read/Write/Delete
- Aggregation Pipeline : 
        group,
        order,
        project, 
        match, 
        limit skip
- Working with arrays in MongoDB documents


## Upsert in MongoDB

Used for update, Upsert is a combination of Insert and Update.

If value of this option is set to 'True', and a document(s) is found that matches the specified query, then the update operation will update the doc(s).


If no doc(s) matches the specified doc, then this option will insert a new doc in the collection .

By default, the upset option value is false. 


## Bulk write 



## Aggregation Examples 




## Notes

In MongoDB, aggregation operations process the data records/documents and return computed results. It collects values from various documents and groups them together and then performs different types of operations on that grouped data like sum, average, minimum, maximum, etc to return a computed result


1. A lookup is basically a left outer join

```
$lookup: {
        from: <collection to join>
        localField: <fielf from the input documents>
        foreignField: <field from documents of the "from" collection>
        as: <output array field>
}

```


2. Operator Stages in Aggregation: Stages, Expression and Accumulator

**db.train.aggregate([{$group:{_id:"$id", total:{$sum: "$fare"}}}])**

Here:
- $group is the Stage
- "$id" is the Expression
- $sum is the Accumulator 

**Stages**: Each stage starts from stage operators which are:

- $match: It's used for filtering the documents; can reduce the amount of documents that are
given as input to the next stage..
- $project: It's used to select some specific fields from a collection 
- $group: It's used to group documents based on some value
- $skip: It is used to skip n number of documents and passes the remaining documents
- $limit: It is used to pass first n number of docs thus limiting them 
- $unwind: It is used to unwind documents that are using arrays i.e. it deconstructs an array field in the documents to return documents for each element
- $out: It is used to write resulting documents to a new collection 


**Expressions**:  It refers to the name of field in input docs for e.g. 
{$group: {_id: "$id", total: {$sum:"$fare"}}} 
here $id and $fare are expressions.

**Accumulators**: They are basically used in the group stage

- sum: It sums numeric values for the docs in each group
- count: It counts total number of docs
- avg: It calculates the average of all given values from all docs
- min: It gets min value from all docs
- max: It gets max value from all docs
- first: first document from grouping
- last: last document from grouping

**IMP**:
- $group_id is mandatory
- $out must be last stage in pipeline
- $sum: 1 will count number of docs and $sum:"$fare" will give the sum of total fare generated per id 


3. SON : As python dictionaries dont maintain order you should 