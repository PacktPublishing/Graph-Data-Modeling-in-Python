MATCH (c:Customer)-[purchase:PURCHASED]->(p:Product) 
RETURN c.name, p.name, purchase.datetime
