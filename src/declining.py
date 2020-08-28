from random import choice


def decline(dice_roll, G, node):
    r"""
    Declining node rule.
    """
    if dice_roll >= G.nodes[node]['decline']:
        G.nodes[node]['state'] = -1
        try:
            _node = list(choice(list(G.edges([node]))))[1]
            G.remove_edge(node, _node)
        except IndexError:
            if dice_roll > G.nodes[node]['dormancy']:
                G.nodes[node]['state'] = -2
    else:
        G.nodes[node]['state'] = 1
    return G
