from neo4j import GraphDatabase

class Neo4jConnect:
    def __init__(self, uri, user, password):
        self.driver = GraphDatabase.driver(uri, auth=(user, password))
        self.user = user
        self.uri = uri
    def close(self):
        self.driver.close()
        
    def query(self, query):
        session = self.driver.session()
        result = session.run(query)
        return result

    def __str__(self):
        return f'Connection successful for user: {self.user}.\nConnected to Neo4J database uri: {self.uri}'