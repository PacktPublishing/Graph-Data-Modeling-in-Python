LOAD CSV from 'file:///reachability.csv' as row
MATCH (from:City {node_id: row[0]})
MATCH (to:City {node_id: row[1]})
MERGE (from)-[:AIR_TRAVEL {distance: row[2]}]-(to)
