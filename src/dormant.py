def dormancy(dice_roll, G, node):
    r"""
    Dormancy node rule.
    """
    if dice_roll >= G.nodes[node]['extinction']:
        G.nodes[node]['state'] = -2
    else:
        if dice_roll >= G.nodes[node]['emerging']:
            G.nodes[node]['state'] = 1
        else:
            G.nodes[node]['state'] = -1
    return G
