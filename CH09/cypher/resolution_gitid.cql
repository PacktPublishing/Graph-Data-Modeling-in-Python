MERGE (d:Developer {githubId: '1'})
MERGE (d2:Developer {githubId: '2'})
MERGE (d1)-[:FOLLOWS]->(d2)
