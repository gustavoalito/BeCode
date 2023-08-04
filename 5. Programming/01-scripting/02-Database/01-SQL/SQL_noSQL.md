# SQL and NoSQL

**Group presentation: Alejandro, Cédric, Gustavo, Nicolay**

In the world of database management systems, two main contenders stand out: SQL and NoSQL. Each type offers unique features and benefits, making them suitable for different use cases. Let's explore the main points of each to help you understand their strengths and differences:


## Relational Database (SQL):

![image](https://github.com/gustavoalito/BeCode/assets/133368766/f51d1fd4-fb03-479d-805f-64b7d40a60ff =250x250)


| Aspect                  | Description                                       |
|-------------------------|---------------------------------------------------|
| Data Storage            | Tables with predefined schema                    |
| Use Cases               | Structured data and complex queries              |
| Data Consistency        | Strong consistency and supports transactions     |
| Scalability             | Vertical scaling                                 |
| Examples                | MySQL, PostgreSQL, Oracle Database, SQL Server   |

## NoSQL Database:

![image](https://github.com/gustavoalito/BeCode/assets/133368766/61ac3f12-0983-478b-969a-5b7be7ccb00b)


| Aspect                  | Description                                       |
|-------------------------|---------------------------------------------------|
| Data Storage            | No predefined schema, flexible data models       |
| Use Cases               | Unstructured or rapidly changing data            |
| Data Consistency        | Eventual consistency, trade-off for write speed  |
| Scalability             | Horizontal scaling                               |
| Examples                | MongoDB, Cassandra, Redis, HBase, Neo4j          |

## Important topic: SECURITY

| Security Threats       | NoSQL Databases                                       | SQL Databases                                       |
|------------------------|-------------------------------------------------------|-----------------------------------------------------|
| Injection Attacks      | NoSQL injection attacks targeting query languages   | SQL injection attacks                               |
| Weak Authentication    | Simpler authentication and authorization mechanisms  | Robust authentication and authorization mechanisms |
| Schemaless Design      | Flexibility can lead to data integrity issues        | Rigid schema provides better data validation        |
| Denial of Service      | Vulnerable to DoS attacks                            | Vulnerable to DoS attacks                           |
| Insecure Configurations| Insecure default settings might expose the system   | Insecure default settings might expose the system   |
| Lateral Movement       | Compromising web apps can lead to DB access         | Compromising web apps can lead to DB access         |
| Limited Auditing       | Logging and auditing might be limited                | Better logging and auditing capabilities            |
| Data Privacy Concerns  | Increased risk of mishandling sensitive data         | Similar data privacy concerns                       |
| Scalability Challenges | Complex security setup in distributed environments   | More centralized security setup                     |

Summary:
NoSQL databases are susceptible to NoSQL injection attacks, have weaker authentication mechanisms, and face challenges due to their schemaless design. They are vulnerable to DoS attacks, might come with insecure defaults, and could have limited auditing capabilities. Additionally, handling data privacy and securing distributed environments can be challenging. SQL databases, on the other hand, are prone to SQL injection attacks but generally have stronger authentication and authorization mechanisms. They benefit from rigid schemas that improve data validation and have more robust auditing features. Both database types share concerns regarding data privacy and are vulnerable to DoS attacks.

## When to Choose NoSQL:

| Use Case                                     |
|----------------------------------------------|
| Real-time data processing applications       |
| Need for horizontal scalability              |
| Storing large amounts of unstructured data   |
| Applications requiring quick and easy scaling|
| Web and mobile applications                  |
| Applications with flexible schema requirements|

## When to Choose SQL:

| Use Case                                     |
|----------------------------------------------|
| Applications requiring transactions          |
| Complex queries and data analysis apps       |
| Data warehousing and business intelligence   |
| Well-structured and predictable data         |
| Need for robust security features            |
| Applications with critical support and integration requirements|

## NoSQL Database Types:

| Type               | Description                                          |
|--------------------|------------------------------------------------------|
| Key-value          | Flexible storage with no restrictions on data format |
| Document           | Stores semi-structured data in documents             |
| Graph              | Represents data as nodes and relationships          |
| Wide column        | Organizes data in tables with rows and columns      |


## Examples:

### SQL Databases:
- MySQL: Open-source, easy to use, and widely used.
- PostgreSQL: Open-source, robust, and performance-oriented.
- Oracle Database: Commercial, enterprise-grade database.
- Microsoft SQL Server: Commercial, widely used in enterprises.
- IBM DB2: Commercial, used for mission-critical applications.

### NoSQL Databases:
- MongoDB: Document-oriented, used for web applications.
- Cassandra: Column-oriented, scalable for big data apps.
- Redis: Key-value store, often used as a cache or message broker.
- HBase: Column-oriented, widely used in Big Data applications.
- Neo4j: Graph database, suited for data represented as a graph.

## In summary

![image](https://github.com/gustavoalito/BeCode/assets/133368766/0e73b453-fd60-45fc-807c-97db5c0b055e)


| Aspect                   | SQL Database                                     | NoSQL Database                                  |
|--------------------------|--------------------------------------------------|-------------------------------------------------|
| Data Model               | Relational tables with predefined schema        | Flexible schema, can store various data formats |
| Query Complexity         | Complex queries and joins                        | Simpler queries, better with single-table data  |
| Data Consistency         | Strong consistency, supports transactions        | Eventual consistency, may sacrifice consistency|
| Write Performance        | Atomic, consistent, and durable writes          | High write performance, may sacrifice consistency|
| Scalability              | Less scalable, vertical scaling                 | Highly scalable, horizontal scaling             |
| Schema Flexibility       | Less flexible, schema must be defined upfront   | Flexible schema, can adapt as application evolves|
| Hardware Requirements    | Often requires expensive, specialized hardware   | Can run on cheaper, general-purpose hardware    |
| Workload Volume          | Well-suited for large-scale data processing      | Better for handling large amounts of data       |
| Use Cases                | Complex applications with structured data       | Real-time applications, unstructured data       |
| Security                 | Provide better security features     | Typically have weaker security features       |


Please note that the choice between SQL and NoSQL databases depends on your specific application requirements and data characteristics. Consider factors such as data structure, query complexity, scalability needs, and consistency requirements when making your decision. In some cases, a combination of both database types may offer the best solution.

## References
- https://www.oracle.com/be/database/nosql/what-is-nosql/
- https://www.boltic.io/blog/relational-databases-vs-nosql (content as well as images)
- https://www.youtube.com/watch?v=BW3cdr5MjEE
