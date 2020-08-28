from networkx import Graph
from random import randint, choice, random


def random_edge(N):
    r"""
    Returns two unique integers between 1 and N.
    """
    a = randint(1, N)
    b = randint(1, N)
    while a == b:
        b = randint(1, N)
    return a, b


def roll():
    r"""
    Random number between 0 and 1
    """
    return random()


def define_state():
    r"""
    Random choice between of each potential state.
    """
    return choice([2, 1, -1, -2])


def create_node(G, node, N):
    r"""
    Assigns state variables to a node.
    """
    G.add_node(
        node,
        state=define_state(),
        starvation=G.number_of_edges(),
        emerging=roll(),
        extinction=roll(),
        dormancy=roll(),
        decline=roll(),
        evolve=roll(),
        perturbation=roll(),
        progress=roll()
    )
    return G


def random_initial_state(N):
    r"""
    Creates a randomly generated initial state graph where the number of edges
    will be less than N.
    """
    G = Graph()
    a, b = random_edge(N)
    while G.number_of_edges() < N:
        G = create_node(G, a, N)
        G = create_node(G, b, N)
        G.add_edge(a, b)
        a, b = random_edge(N)
    return G
