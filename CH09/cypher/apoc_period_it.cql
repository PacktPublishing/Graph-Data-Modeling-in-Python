CALL apoc.periodic.iterate("
    MATCH (d:Developer) RETURN d",
    "DETACH DELETE d", 
    {batchSize:1000, parallel:false}
)
