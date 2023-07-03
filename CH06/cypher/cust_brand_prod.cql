MATCH (c:Customer {customerID:10010})-[:PURCHASED]->(p:Product)
MATCH (p)-[:HAS_BRAND]->(b:Brand)
MATCH (b)<-[:HAS_BRAND]-(r:Product)
WHERE NOT (c)-[:PURCHASED]->(r)
RETURN c, p, b, r
