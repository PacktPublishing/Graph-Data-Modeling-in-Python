MATCH (c:Customer {customerID:10010})-[:PURCHASED]-(p:Product)
RETURN DISTINCT p.productID as productID
