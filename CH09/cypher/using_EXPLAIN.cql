EXPLAIN
MATCH (d:Developer)-[:FOLLOWS]->(d2:Developer)
RETURN d, d2
