# MongoDB

+ Content copied from https://www.w3schools.com +

Mongo is a document DB.

## Show all databases
To see all available databases, in your terminal type `show dbs`.

Notice that any empty database will not be listed; they are essentially non-existent until they have content.

## Change or Create a Database
You can change or create a new database by typing `use` and then the name of the database.

## Creating Collections using mongosh
There are 2 ways to create a collection.

### Method 1
You can create a collection using the createCollection() database method.

Example
`db.createCollection("posts")`

### Method 2
You can also create a collection during the insert process.

Example
We are here assuming the object is a valid JavaScript object containing post data:
`db.posts.insertOne(object)`

## Insert Documents
There are 2 methods to insert documents into a MongoDB database.

`insertOne()`
To insert a single document, use the insertOne() method.

This method inserts a single object into the database.

Note: When typing in the shell, after opening an object with curly braces "{" you can press enter to start a new line in the editor without executing the command. The command will execute when you press enter after closing the braces.

Example
db.posts.insertOne({
  title: "Post Title 1",
  body: "Body of post.",
  category: "News",
  likes: 1,
  tags: ["news", "events"],
  date: Date()
})
Note: If you try to insert documents into a collection that does not exist, MongoDB will create the collection automatically.

`insertMany()`
To insert multiple documents at once, use the insertMany() method.

This method inserts an array of objects into the database.

Example
db.posts.insertMany([  
  {
    title: "Post Title 2",
    body: "Body of post.",
    category: "Event",
    likes: 2,
    tags: ["news", "events"],
    date: Date()
  },
  {
    title: "Post Title 3",
    body: "Body of post.",
    category: "Technology",
    likes: 3,
    tags: ["news", "events"],
    date: Date()
  },
  {
    title: "Post Title 4",
    body: "Body of post.",
    category: "Event",
    likes: 4,
    tags: ["news", "events"],
    date: Date()
  }
])

## Find Data
There are 2 methods to find and select data from a MongoDB collection, find() and findOne().

### find()
To select data from a collection in MongoDB, we can use the find() method.

This method accepts a query object. If left empty, all documents will be returned.

Example
`db.posts.find()`

### findOne()
To select only one document, we can use the `findOne()` method.

This method accepts a query object. If left empty, it will return the first document it finds.

Note: This method only returns the first match it finds.

Example
`db.posts.findOne()`

## Querying Data
To query, or filter, data we can include a query in our `find()` or `findOne()` methods.

Example
`db.posts.find( {category: "News"} )`

## Projection
Both "find" methods accept a second parameter called projection.

This parameter is an object that describes which fields to include in the results.

Note: This parameter is optional. If omitted, all fields will be included in the results.

Example
This example will only display the title and date fields in the results.

`db.posts.find({}, {title: 1, date: 1})`
Notice that the `_id` field is also included. This field is always included unless specifically excluded.

We use a `1` to include a field and `0` to exclude a field.

Example
This time, let's exclude the _id field.

`db.posts.find({}, {_id: 0, title: 1, date: 1})`
Note: You cannot use both 0 and 1 in the same object. The only exception is the _id field. You should either specify the fields you would like to include or the fields you would like to exclude.

Let's exclude the date category field. All other fields will be included in the results.

Example
`db.posts.find({}, {category: 0})`
We will get an error if we try to specify both 0 and 1 in the same object.

Example
`db.posts.find({}, {title: 1, date: 0})`

## Update Document
To update an existing document we can use the `updateOne()` or `updateMany()` methods.

The first parameter is a query object to define which document or documents should be updated.

The second parameter is an object defining the updated data.

### updateOne()
The `updateOne()` method will update the first document that is found matching the provided query.

Let's see what the "like" count for the post with the title of "Post Title 1":

Example
`db.posts.find( { title: "Post Title 1" } ) `
Now let's update the "likes" on this post to 2. To do this, we need to use the $set operator.

Example
`db.posts.updateOne( { title: "Post Title 1" }, { $set: { likes: 2 } } ) `
Check the document again and you'll see that the "like" have been updated.

Example
`db.posts.find( { title: "Post Title 1" } )` 

### Insert if not found
If you would like to insert the document if it is not found, you can use the `upsert` option.

Example
Update the document, but if not found insert it:

db.posts.updateOne( 
  { title: "Post Title 5" }, 
  {
    $set: 
      {
        title: "Post Title 5",
        body: "Body of post.",
        category: "Event",
        likes: 5,
        tags: ["news", "events"],
        date: Date()
      }
  }, 
  { upsert: true }
)

### updateMany()
The `updateMany()` method will update all documents that match the provided query.

Example
Update likes on all documents by 1. For this we will use the `$inc` (increment) operator:

`db.posts.updateMany({}, { $inc: { likes: 1 } })`
Now check the likes in all of the documents and you will see that they have all been incremented by 1.

## Delete Documents
We can delete documents by using the methods `deleteOne()` or `deleteMany()`.

These methods accept a query object. The matching documents will be deleted.

### deleteOne()
The `deleteOne()` method will delete the first document that matches the query provided.

Example
`db.posts.deleteOne({ title: "Post Title 5" })`

### deleteMany()
The `deleteMany()` method will delete all documents that match the query provided.

Example
`db.posts.deleteMany({ category: "Technology" })`

## MongoDB Query Operators
There are many query operators that can be used to compare and reference document fields.

### Comparison
The following operators can be used in queries to compare values:

`$eq:` Values are equal
`$ne:` Values are not equal
`$gt:` Value is greater than another value
`$gte:` Value is greater than or equal to another value
`$lt:` Value is less than another value
`$lte:` Value is less than or equal to another value
`$in:` Value is matched within an array
Logical

The following operators can logically compare multiple queries.

`$and:` Returns documents where both queries match
`$or:` Returns documents where either query matches
`$nor:` Returns documents where both queries fail to match
`$not:` Returns documents where the query does not match

### Evaluation
The following operators assist in evaluating documents.

`$regex:` Allows the use of regular expressions when evaluating field values
`$text:` Performs a text search
`$where:` Uses a JavaScript expression to match documents

## MongoDB Update Operators
There are many update operators that can be used during document updates.

### Fields
The following operators can be used to update fields:

`$currentDate:` Sets the field value to the current date
`$inc:` Increments the field value
`$rename:` Renames the field
`$set:` Sets the value of a field
`$unset:` Removes the field from the document

### Array
The following operators assist with updating arrays.

`$addToSet:` Adds distinct elements to an array
`$pop:` Removes the first or last element of an array
`$pull:` Removes all elements from an array that match the query
`$push:` Adds an element to an array

## Aggregation Pipelines
Aggregation operations allow you to group, sort, perform calculations, analyze data, and much more.

Aggregation pipelines can have one or more "stages". The order of these stages are important. Each stage acts upon the results of the previous stage.

Example
db.posts.aggregate([
  // Stage 1: Only find documents that have more than 1 like
  {
    $match: { likes: { $gt: 1 } }
  },
  // Stage 2: Group documents by category and sum each categories likes
  {
    $group: { _id: "$category", totalLikes: { $sum: "$likes" } }
  }
])

