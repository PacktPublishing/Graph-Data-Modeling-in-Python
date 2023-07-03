CREATE CONSTRAINT githubId_constraint
FOR (d:Developer)
REQUIRE d.githubId IS UNIQUE
