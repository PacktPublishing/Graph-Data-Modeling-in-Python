MATCH (d:Developer)-[:FOLLOWS]-(d2:Developer)
WITH size(collect(d2)) as degree, d
WHERE degree >= 10
RETURN d.githubId, degree ORDER BY degree DESC
