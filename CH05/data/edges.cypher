LOAD CSV from 'file:///reachability.csv' as row
MATCH (from:City {node_id: toInteger(row[0])})
MATCH (to:City {node_id: toInteger(row[1])})
MERGE (from)-[:AIR_TRAVEL {travel_time: toInteger(row[2])}]-(to)
