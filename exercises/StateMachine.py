class State(object):
    name = "General State"
    allowed_transitions = []

    def switch(self, new_state):
        if new_state.name in self.allowed_transitions:
            self.__class__ = new_state
            print('Current:', self, ' => switched to new state', new_state.name)
        else:
            print('Current:', self, ' => switching to', new_state.name, 'is not allowed.')

    def __str__(self):
        return self.name


class Inactive(State):
    name = "Inactive"
    allowed_transitions = ['Patrolling']


class Patrolling(State):
    name = "Patrolling"
    allowed_transitions = ['Tracking']


class Tracking(State):
    name = "Tracking"
    allowed_transitions = ['Patrolling', 'Attacking']


class Attacking(State):
    name = "Attacking"
    allowed_transitions = ['Patrolling']


class StateMachine(object):
    def __init__(self):
        self.state = Inactive()

    def change(self, new_state):
        self.state.switch(new_state)


def main():
    enemy_basic_ai = StateMachine()
    enemy_basic_ai.change(Inactive)  # Not allowed
    enemy_basic_ai.change(Patrolling)
    enemy_basic_ai.change(Tracking)
    enemy_basic_ai.change(Attacking)
    enemy_basic_ai.change(Patrolling)
    enemy_basic_ai.change(Tracking)
    enemy_basic_ai.change(Inactive)  # Not allowed


if __name__ == "__main__":
    main()
