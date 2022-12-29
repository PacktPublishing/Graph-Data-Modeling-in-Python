def create_igraph_ids(nodes, from_index=0):
	igraph_ids = {internal_id: igraph_id for igraph_id, internal_id
              	in enumerate(nodes, from_index)}
	return igraph_ids
