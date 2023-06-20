from nim_gain_engine import best_move


class Nim:
    def __init__(self, init_state: int):
        self._init_state = init_state

    def start(self):
        state = self._init_state
        print(f"Take one to three chip from a pile contains {state} chips...")
        while True:
            n = int(input(f"How many chip you would like to take from pile {state}: "))
            if n > 3 or n <= 0 or n > state:
                print("Invalide input, try again...")
                continue
            state -= n
            if state == 0:
                print("You Lose -_-")
                break
            old_state = state
            _, state = best_move(state)
            if state == 0:
                print("You Win :)")
                break
            else:
                print(f"AI took {old_state - state} chips. Your turn.")


if __name__ == '__main__':
    Nim(6).start()
