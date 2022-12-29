import mysql.connector
def query_mysql(query, password, host='localhost', user='root',database='steam_data'):
    ''''
    Query a MySQL database instance
 
    :param query: a SQL query to run against the MySQL database
    :param password: the MySQL instance password when setting up the solution
    :param host: the host (default=localhost)
    :param user: the user (default=root) for all the MySQL priviledges
    :param database: defaults to `steam_data` but this could be any database of choosing
    :return: SQL query results
    '''
    connection = mysql.connector.connect(
    host=host,
    user=user,
    passwd=password,
    database=database
    )
    cursor = connection.cursor()
    cursor.execute(query)
    result = cursor.fetchall()
    connection.close()
    return result
