## Context
For semester six at Fontys in Eindhoven we are working on a decentralized way to make certain agents or bots collaborate with each other to achieve a certain goal. For this project we will need to do some research about how we are going to store the data being used in this network. In this research I will research what types of database there are and what the most efficient one of those database is to achieve the goal of this project.

## What is a database
A database is a collection of information stored on a machine. Databases can be used to store almost everything from storing some text to storing large amounts of images. Databases allow computers to store essential data in an organized and easily searchable way. Database will be typically accessed by using a database management system (DBSM). This DBMS acts as an interface between the data and the end-user.

**Sources:**
- https://en.wikipedia.org/wiki/Database
- https://www.indeed.com/career-advice/career-development/types-of-databases
- https://www.oracle.com/database/what-is-database/

## Types of databases
There are a lot of existing database types already, but as technology keep advancing, so do the databases. The most commonly used database types are as followed: 
- Centralized database 
- Cloud database 
- Commercial database 
- Distributed database 
- End-user database 
- Graph database 
- NoSQL database 
- Object-oriented database 
- Open-source database 
- Operational database 
- Personal database 
- Relational database

From this list the most commonly used database type is the relational database, which is fine when working with some structured data, but falls off when working with large datasets.

**Sources:**
- https://www.geeksforgeeks.org/types-of-databases/
- https://www.indeed.com/career-advice/career-development/types-of-databases

## Database used in Fediverse
- [Masterdon](https://joinmastodon.org/) - PostgreSQL
- [PixelFed](https://pixelfed.org/) - MariaDB or MySQL
- [PeerTube](https://joinpeertube.org/) - PostgreSQL
- [Lemmy](https://join-lemmy.org/) - PostgreSQL
- [Prismo](https://join-lemmy.org/) - PostgreSQL
- [Pleroma](https://pleroma.social/) - PostgreSQL
- [Diaspora](https://diasporafoundation.org/) - MySQL
- [WriteFreely](https://writefreely.org/) - SQLite or MySQL
- [Friendica](http://friendi.ca/) - MySQL
- [Hubzilla](https://hubzilla.org/) - MySQL, MariaDB or PostgreSQL
- [FunkWhale](https://funkwhale.audio/) - PostgreSQL

From these few examples it is clear that within the Fediverse a lot of relational database get used as almost all of the above examples have relational database. 

Now its clear that PostgreSQL gets used the most within the Fediverse, with a second option MySQL.

**Source:**
- https://www.oracle.com/mysql/what-is-mysql/
- https://aws.amazon.com/compare/the-difference-between-mysql-vs-postgresql/

## What is PostgreSQL
PostgreSQL is also an open source object-relational database management system that offers more features than MySQL. It gives you more flexibility in data types, scalability, concurrency, and data integrity.

**Source:**
- https://www.postgresql.org/
- https://aws.amazon.com/compare/the-difference-between-mysql-vs-postgresql/


## PostgreSQL vs MySQL
While PostgreSQL and MySQL are conceptually similar, there are also many differences to consider before implementing them.

**Similarities:**
- Both the PostgreSQL and MySQL store data in tables that are related to each other via common columns. 
- They both use SQL as a query interface to read an write data. 
- They both are open-sourced and have a strong development community backing them up.

**Differences:**
- PostgreSQL offers more types than MySQL. 
- PostgreSQL work optimal on UNIX-based system, while MySQL works fully cross platform 
- PostgreSQL stores more diverse, includes arrays, hstore. While MySQL only supports standard data types.

**Source:**
- https://kinsta.com/blog/postgresql-vs-mysql/
- https://www.postgresqltutorial.com/postgresql-tutorial/postgresql-vs-mysql/

## Conclusion
As both of these databases have their own strengths and weaknesses, their is one key rule of thumb what should be considered when choosing between these two databases. 
- PostgreSQL performs better for write-heavy workloads. 
- MySQL performs better for read-heave workloads.

So when working with large datasets, complex queries and working on enterprise applications: choose for PostgreSQL. Else choose for MySQL. 

For working in the Fediverse I myself would recommend to use PostgreSQL.

## Next Steps
- Look into how open database are? so you dont have change the tables everytime
- Vector database?