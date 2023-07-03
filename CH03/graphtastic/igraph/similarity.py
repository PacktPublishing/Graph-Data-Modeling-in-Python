def prune_graph(g, min_hours):
	edges_to_remove = g.es.select(weight_lt=min_hours)
	g.delete_edges(edges_to_remove)
	return g

def make_recommendations(g, user, min_hours):
    user_node = g.vs.select(internal_id_eq=user)
    user_node = user_node[0].index
    g = prune_graph(g, min_hours)
    other_user_nodes = g.vs.select(type_eq='source')
    pairs = [[user_node, other_user.index] for other_user in other_user_nodes if other_user.index != user_node]
    similarities = g.similarity_jaccard(pairs=pairs, mode='out')
    node_similarity = [[pair[1], similarity] for pair, similarity in zip(pairs, similarities)]
    node_similarity = sorted(node_similarity, key=lambda x: x[1], reverse=True)
    most_similar_node = node_similarity[0][0]
    game_recommendations = g.vs[g.neighbors(most_similar_node)]['internal_id']
    owned_games = g.vs[g.neighbors(user_node)]['internal_id']
    new_games = [game for game in game_recommendations if game not in owned_games]
    return new_games
