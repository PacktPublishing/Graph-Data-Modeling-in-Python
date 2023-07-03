LOAD CSV WITH HEADERS FROM 'file:///products.csv' AS row
MERGE (p:Product {productID: toInteger(row.productID), name: row.name})
MERGE (b:Brand {brandName: row.brand})
MERGE (m:Type {typeName: row.mainType})
MERGE (s:Type {typeName: row.subType})
MERGE (p)-[:HAS_BRAND]->(b)
MERGE (p)-[:HAS_TYPE]->(s)
MERGE (s)-[:HAS_TYPE]->(m)
