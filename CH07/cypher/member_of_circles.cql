MATCH (u:User)-[:MEMBER_OF]->(c:Circle {circleID: '5'})
RETURN u, c
