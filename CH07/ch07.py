from neo4j import GraphDatabase

class Neo4jConnect:
    
    def __init__(self, uri, user, password):

        self.driver = GraphDatabase.driver(uri, auth=(user, password))
        
    def close(self):
        
        self.driver.close()
        
    def query(self, query):
        
        session = self.driver.session()
        result = session.run(query)
        
        return result
    
import csv

with open('chapter07/data/edges1.csv', 'r') as c:
    reader = csv.reader(c)
    edgelist = [edge for edge in reader]

print(edgelist[:5])


def add_edge_neo4j(n, m, connection):

    cypher = f'MERGE (u1:User {{userID: {n}}}) ' \
             f'MERGE (u2:User {{userID: {m}}}) ' \
              'MERGE (u1)-[:FOLLOWS]->(u2)'

    connection.query(cypher)

'''
connection = Neo4jConnect('bolt://localhost:7687', 'admin', 'testpython')
add_edge_neo4j(edgelist[0][0], edgelist[0][1], connection)
connection.close()


for n, m in edgelist:
    connection = Neo4jConnect('bolt://localhost:7687', 'admin', 'testpython')
    add_edge_neo4j(n, m, connection)
    connection.close()

'''

with open('chapter07/data/circle1.csv', 'r') as c:
    reader = csv.reader(c)
    circles_raw = [row for row in reader]

print(circles_raw)


def get_user_circle_pairs(circles):

    pairs = []
    for circle in circles:
        circle_pairs = [[user, circle[0]] for user in circle][1:]
        [pairs.append(pair) for pair in circle_pairs]

    return pairs

pairs = get_user_circle_pairs(circles_raw)
print(pairs)


def add_circles_neo4j(user_id, circle_id, connection):

    cypher = f'MATCH (u:User {{userID: {user_id}}})' \
             f'SET u.circle = {circle_id}'

    connection.query(cypher)


for user_id, circle_id in pairs:
    
    connection = Neo4jConnect('bolt://localhost:7687', 'admin', 'testpython')
    add_circles_neo4j(user_id, circle_id, connection)
    connection.close()


'''
def add_circles_neo4j_new_schema():

    pass

'''