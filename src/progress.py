from random import choice, uniform


def progressing(dice_roll, G, node):
    r"""
    progressing node rule.
    """
    G.nodes[node]['state'] = 1
    if dice_roll >= G.nodes[node]['evolve']:
        _node = choice(list(G.nodes()))
        while node == _node:
            _node = choice(list(G.nodes()))
        G.add_edge(node, _node)
        G = adapt(G, node)
    else:
        G.nodes[node]['state'] = -2
    return G


def adapt(G, node):
    r"""
    Allows a node to adapt to the edge nodes during an evolution phase.
    """
    _unallowed_states = [
        'state',
        'perturbation',
        'starvation'
    ]
    weight = G.nodes[node]['perturbation']
    for data in G.nodes[node]:
        if data in _unallowed_states:
            continue
        _s = G.nodes[node][data]
        _c = 1
        _l = 1
        _h = 0
        for edges in G.edges([node]):
            dat = G.nodes[edges[1]][data]
            _s += dat
            _c += 1
            if dat < _l:
                _l = dat
            if dat > _h:
                _h = dat
        average_change = _s/_c
        random_change = uniform(_l, _h)
        perturb = (1-weight)*average_change + weight*random_change
        G.nodes[node][data] = perturb
    return G
