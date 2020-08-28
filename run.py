from sys import exit
from src.initialize import random_initial_state
from src.update import update_state
from src.evolve import evolve_state
from src.plotting import save_graph, plot_array, plot_hist


if __name__ == "__main__":
    try:
        N = 25
        T = 100
        print("\nRunning...\n", flush=True)
        print("\nN = {} T = {}\n".format(N, T), flush=True)
        G = random_initial_state(N)
        edges = [N]
        save_graph(G, './images/test_'+str(0).zfill(5)+'.png')
        for t in range(T):
            change = update_state(G)
            G = evolve_state(G, change)
            if t % 1 == 0:
                edges.append(G.number_of_edges())
            save_graph(G, './images/test_'+str(t+1).zfill(5)+'.png')
        save_graph(G, './images/test_'+str(T+1).zfill(5)+'.png')
        plot_array(edges)
        plot_hist(edges)
    except KeyboardInterrupt as e:
        raise e
        exit(0)
