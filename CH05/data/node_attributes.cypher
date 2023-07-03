LOAD CSV WITH HEADERS from 'file:///reachability-meta.csv' as row
CREATE (city:City {
    node_id: toInteger(row.node_id),
    name: row.name,
    population: toInteger(row.metro_pop),
    latitude: toFloat(row.latitude),
    longitude: toFloat(row.longitude)
})
