from functools import lru_cache
from typing import Tuple


@lru_cache(maxsize=1024)
def minimax(state: int, is_max: bool) -> int:
    if state == 0:
        return 1 if is_max else -1

    possible_new_states = [state - take for take in (1, 2, 3) if take <= state]
    return (max if is_max else min)([minimax(new_state, not is_max) for new_state in possible_new_states])


def best_move(state: int) -> Tuple[int, int]:
    score, new_state = 0, 0
    for take in (1, 2, 3):
        if take > state:
            break
        new_state = state - take
        score = minimax(new_state, is_max=False)
        if score > 0:
            break
    return score, new_state


if __name__ == '__main__':
    print(best_move(1))
