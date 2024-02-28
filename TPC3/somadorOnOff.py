import re

class FiniteStateAutomaton:
    def __init__(self, states, initial_state, accepting_states):
        self.states = states
        self.current_state = initial_state
        self.initial_state = initial_state
        self.accepting_states = accepting_states

    def reset(self):
        self.current_state = self.initial_state

    def process_input(self, input):
        sum_print = 0
        sum = 0
        for string in input:
            if string.lower() == 'on':
                self.current_state = 'on'
            elif string.lower() == 'off':
                self.current_state = 'off'
            elif string == '=':
                sum_print += 1
                print("Soma no + número " + sum_plus + ": " + sum)
            else:
                if self.current_state == 'on':
                    sum += int(string)
        if self.current_state in self.accepting_states:
            return ("Soma total final: " + str(sum), "Token válido.")
        else:
            return (False, "Erro semântico: o autómato não atingiu um estado final!")

# Example usage:

# Define states, alphabet, transitions, initial state, and accepting states
states = {'on', 'off'}
initial_state = 'on'
accepting_states = {'on', 'off'}

pattern = re.compile(r'on|off|\d+|-\d+|=', re.IGNORECASE)

# Create the Finite State Automaton
fsa = FiniteStateAutomaton(states, initial_state, accepting_states)


while True:
    inputStdin = input("Insira uma string:\n")
    print(fsa.process_input(pattern.findall(inputStdin)))
    print('\n')
    fsa.reset()