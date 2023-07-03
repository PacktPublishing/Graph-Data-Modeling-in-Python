EXPLAIN 
LOAD CSV WITH HEADERS FROM 'file:///musae_git_edges.csv' AS row
MERGE (d1:Developer {githubId:row.id_1})
MERGE (d2:Developer {githubId:row.id_2})
CREATE (d1)-[:FOLLOWS]->(d2)
RETURN d1, d2
