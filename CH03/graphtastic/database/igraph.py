import igraph as ig
from graphtastic.database.mysql import query_mysql
from graphtastic.igraph.helper import create_igraph_ids

def mysql_to_graph(table, source, target, weights, password):
    sql_query = f'SELECT {source}, {target}, {weights} FROM {table}'
    data = query_mysql(sql_query, password=password)
    source_nodes = sorted(list(set([source for source, _, _ in data])))
    target_nodes = sorted(list(set([target for _, target, _ in data])))
    source_igraph_ids = create_igraph_ids(source_nodes)
    target_igraph_ids = create_igraph_ids(target_nodes, len(source_igraph_ids))
    edges = [(source_igraph_ids[source], target_igraph_ids[target])
         	for source, target, _ in data]
    weights = [weight for _, _, weight in data]
    g = ig.Graph(directed=True)
    g.add_vertices(len(source_nodes + target_nodes))
    g.vs['internal_id'] = list(source_igraph_ids.keys()) + list(target_igraph_ids.keys())
    g.vs['type'] = ['source' for _ in source_nodes] + ['target' for _ in target_nodes]
    g.add_edges(edges)
    g.es['weight'] = weights
    return g
