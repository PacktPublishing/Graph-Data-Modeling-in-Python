def add_customer(c, connection):
    query = f'MERGE (:Customer {{customerID: toInteger({c.customerID}), ' \
    		f'name: "{c.name}", ' \
    		f'address: "{c.address}"}})'
    connection.query(query)

def add_purchase(c, productID, time, connection):
	query = f'MATCH (c:Customer {{customerID: toInteger({c.customerID})}}) ' \
			f'MATCH (p:Product {{productID: toInteger({productID})}}) ' \
			f'MERGE (c)-[:PURCHASED {{datetime:"{time}"}}]->(p)'
	connection.query(query)

def get_product_ids(connection):
	query = 'MATCH (p:Product) RETURN p.productID as productID'
	result = connection.query(query).data()
	result = [product['productID'] for product in result]
	return result

def rec_by_brand(c, connection):
    query = f'MATCH (c:Customer {{customerID: toInteger({c.customerID})}})' \
            '-[:PURCHASED]->(p:Product)' \
            'MATCH (p)-[:HAS_BRAND]->(b:Brand)' \
            'MATCH (b)<-[:HAS_BRAND]-(r:Product)' \
            'WHERE NOT (c)-[:PURCHASED]->(r)' \
            'RETURN DISTINCT r.productID as productID'
    
    result = connection.query(query).data()
    result = [product['productID'] for product in result]
    return result

def rec_by_copurchase(c, connection):
    query = f'MATCH (c:Customer {{customerID: toInteger({c.customerID})}})' \
            '-[:PURCHASED]->(p:Product)' \
            'MATCH (p)<-[:PURCHASED]-(c2:Customer)' \
            'WHERE c2 <> c ' \
            'MATCH (c2)-[:PURCHASED]->(r:Product)' \
            'WHERE p <> r ' \
            'RETURN DISTINCT r.productID as productID'
    result = connection.query(query).data()
    result = [product['productID'] for product in result]
    return result

def get_customer_purchases(c_id, connection):
    query = f'MATCH (c:Customer {{customerID: toInteger({c_id})}})' \
            '-[:PURCHASED]->(p:Product)' \
            'RETURN DISTINCT p.productID as productID'
    result = connection.query(query).data()
    result = [product['productID'] for product in result]
    return result

def add_purchase_id(c_id, productID, time, connection):
	query = f'MATCH (c:Customer {{customerID: toInteger({c_id})}}) ' \
			f'MATCH (p:Product {{productID: toInteger({productID})}}) ' \
			f'MERGE (c)-[:PURCHASED {{datetime:"{time}"}}]->(p)'
	connection.query(query)

def jaccard_similarity(list1, list2):
    set1 = set(list1)
    set2 = set(list2)
    intersection = set1.intersection(set2)
    union = set1.union(set2)
    jaccard = len(intersection) / len(union)
    return jaccard

def rec_by_similarity(c1, c2, threshold, connection):
    p1 = get_customer_purchases(c1, connection)
    p2 = get_customer_purchases(c2, connection)
    similarity = jaccard_similarity(p1, p2)
    if similarity >= threshold and similarity != 1:
        p1_recs = [p for p in p2 if p not in p1]
        p2_recs = [p for p in p1 if p not in p2]
        for p in p1_recs:
            add_purchase_id(c1, p, datetime.now(), connection)
        for p in p2_recs:
            add_purchase_id(c2, p, datetime.now(), connection)