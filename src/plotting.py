import matplotlib.pyplot as plt
from networkx import draw_networkx, spring_layout, circular_layout


def save_graph(G, name):
    r"""
    Save fig to ./images
    """
    plt.figure(figsize=(12, 16))
    n_list = [node for node in G.nodes]
    c_list = []
    for node in G.nodes.data():
        if node[1]['state'] == -2:
            c_list.append('gold')
        elif node[1]['state'] == 1:
            c_list.append('lawngreen')
        elif node[1]['state'] == -1:
            c_list.append('violet')
        else:
            c_list.append('cyan')
    pos = circular_layout(G)
    draw_networkx(G, pos, nodelist=n_list, node_color=c_list)
    plt.scatter(-10, 0, c='gold', label='Dormant')
    plt.scatter(-10, 0, c='violet', label='Declining')
    plt.scatter(-10, 0, c='lawngreen', label='Evolving')
    plt.scatter(-10, 0, c='cyan', label='Thriving')
    plt.xlim((-1.13, 1.13))
    plt.ylim((-1.13, 1.13))
    plt.title("Discrete Dynamical System", fontdict={'fontsize': 64})
    plt.legend(
        loc='upper right',
        prop={'size': 24}
    )
    plt.savefig(name)
    plt.close()


def plot_array(arr):
    _t = [i for i in range(len(arr))]
    plt.plot(_t, arr)
    plt.show()


def plot_hist(arr):
    plt.hist(arr)
    plt.show()
