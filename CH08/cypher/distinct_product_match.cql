MATCH (c:Customer {customerID:10010})-[:PURCHASED]->(p:Product)
MATCH (p)-[:HAS_TYPE]->(st:Type)
MATCH (p)-[:HAS_BRAND]->(b:Brand)
MATCH (b)<-[:HAS_BRAND]-(r:Product)
WHERE NOT (c)-[:PURCHASED]->(r) AND (r)-[:HAS_TYPE]->(st)
RETURN DISTINCT r
