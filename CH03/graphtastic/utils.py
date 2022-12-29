import igraph

def read_csv(csv_path):
    ''''
    Import a csv file.
 
    :param csv_path: Path to the csv to import.
    :return: A list of lists read from the csv.
    '''
 
    import csv
    import os
 
    assert os.path.exists(csv_path), \
        f'File could not be found at {csv_path}.'
 
    with open(csv_path, 'r', encoding='utf-8') as csv_file:
        reader = csv.reader(csv_file)
        data = [row for row in reader]
 
    return data


def add_nodes(g, nodes, attributes):
    '''
    Add nodes to the graph.
 
    :param g: An igraph Graph() object.
    :param nodes: A list of lists containing nodes and node attributes, with a header. The first
                  element of each list in nodes should be the node ID.
    :param attributes: A list of attributes corresponding to the header (index 0) of the nodes list.
                       The names of attributes in this list will be added to the graph.
    '''
 
    assert nodes[0][0] == 'id', \
        f'The first column in the imported csv should be the ID header, "id". Instead, it '\
        f'is {nodes[0][0]}.'
 
    node_ids = [int(row[0]) for row in nodes[1:]]
    assert node_ids == list(range(len(node_ids))), \
        f'Node IDs should increase sequentially in the imported csv, from 0 to the number of'\
        f' nodes-1, {len(node_ids)}.'
 
    assert isinstance(attributes, list), \
        f'Attributes to add to the graph should be a list. Instead attributes is of type'\
        f' {type(attributes)}.'
 
    g.add_vertices(len(node_ids))
 
    headers = nodes[0]
    for attribute in attributes:
        attr_index = headers.index(attribute)
        g.vs[attribute] = [row[attr_index] for row in nodes[1:]]
 
    return g

def add_edges(g, edges):
    '''
    Add edges to the graph, where nodes are already present.
 
    :param g: An igraph Graph() object.
    :param edges: A list of lists containing edges, with a header.
    '''
    
    assert len(edges[0]) == 2, \
        f'Each element in the imported edges csv should be of length 2, representing an edge'\
        f' between two linked nodes. Instead, the first element is of length {len(edges)[0]}.'
 
    edges_to_add = [[int(row[0]), int(row[1])] for row in edges[1:]]
    g.add_edges(edges_to_add)
 
    return g


def graph_from_attributes_and_edgelist(node_attr_csv, edgelist_csv, attributes):
    
    g = igraph.Graph(directed=False)
 
    nodes = read_csv(node_attr_csv)
    edges = read_csv(edgelist_csv)
 
    g = add_nodes(g, nodes, attributes)
    g = add_edges(g, edges)
 
    return g