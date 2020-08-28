from src.initialize import roll
from src.dormant import dormancy
from src.declining import decline
from src.thriving import thrive
from src.progress import progressing


def evolve_state(G, change):
    r"""
    Evolve the current state to the next state.
    """
    dice_roll = roll()
    for c in change:
        total = c[1]
        check = total % 2
        node = c[0]
        if total < 0:
            if check == 0:
                G = dormancy(dice_roll, G, node)
            else:
                G = decline(dice_roll, G, node)
        elif total > 0:
            if check == 0:
                G = thrive(dice_roll, G, node)
            else:
                G = progressing(dice_roll, G, node)
        else:
            pass
    return G
