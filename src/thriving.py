def thrive(dice_roll, G, node):
    r"""
    Thriving node rule.
    """
    if len(G.edges([node])) >= G.nodes[node]['starvation']:
        G.nodes[node]['state'] = -1
    else:
        if dice_roll >= G.nodes[node]['progress']:
            G.nodes[node]['state'] = 2
        else:
            G.nodes[node]['state'] = 1
    return G
