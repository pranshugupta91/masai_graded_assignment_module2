# NoSQL Database Analysis – FlexiMart
## A. Why Relational Databases Don’t Work Well
Relational databases are great when data is clean and predictable, but they struggle with FlexiMart’s wide range of products. Every product has to fit the same table structure, which doesn’t make sense when laptops and shoes have completely different details. This usually ends up with lots of empty columns or messy table designs.

On top of that, adding new product types means changing the database schema, which is slow and risky. Reviews also need separate tables and joins, making product queries heavier and slower. Overall, relational databases reduce flexibility as the business grows.

## B. Why MongoDB Makes Sense
MongoDB is much more flexible. Each product can store exactly the fields it needs, without worrying about unused columns. New product types can be added easily without touching existing data.

Reviews can be stored directly inside product documents, so fetching a product with its reviews is fast and simple. MongoDB also scales easily across multiple servers, which helps handle growing users and traffic.

## C. Downsides of MongoDB
MongoDB does come with trade-offs. It’s not great for complex transactions or heavy joins. Also, since there’s no strict schema, developers need to be careful to keep the data clean and consistent. It’s powerful, but only if designed properly.
