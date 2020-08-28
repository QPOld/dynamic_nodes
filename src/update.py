def update_state(G):
    r"""
    Calculates the total state for updating each node.
    """
    _change = []
    for node in G.nodes:
        _s = G.nodes[node]['state']
        for edges in G.edges([node]):
            _s += G.nodes[edges[1]]['state']
        _change.append([node, _s])
    return _change
