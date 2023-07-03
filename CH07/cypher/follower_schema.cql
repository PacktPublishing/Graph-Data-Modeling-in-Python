MATCH (u:User)
WHERE '5' in u.circle RETURN u
