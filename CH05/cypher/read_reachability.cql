LOAD CSV WITH HEADERS from 'file:///reachability-meta.csv' as row
CREATE (city:City {
    node_id: row.node_id,
    name: row.name,
    population: row.metro_pop,
    latitude: row.latitude,
    longitude: row.longitude
})
