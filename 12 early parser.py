class EarleyParser:
    def __init__(self, grammar, start_symbol):
        self.grammar = grammar
        self.start_symbol = start_symbol

    def parse(self, input_string):
        chart = [set() for _ in range(len(input_string) + 1)]
        chart[0].add((self.start_symbol, [], self.grammar[self.start_symbol][0], 0))
        
        for i in range(len(input_string) + 1):
            for state in list(chart[i]):
                lhs, seen, unseen, origin = state
                if unseen:  # Incomplete
                    if unseen[0].isupper():  # Non-terminal
                        for prod in self.grammar[unseen[0]]:
                            chart[i].add((unseen[0], [], prod, i))
                    elif i < len(input_string) and unseen[0] == input_string[i]:  # Terminal
                        chart[i + 1].add((lhs, seen + [unseen[0]], unseen[1:], origin))
                else:  # Complete
                    for s in list(chart[origin]):
                        if s[2] and s[2][0] == lhs:
                            chart[i].add((s[0], s[1] + [lhs], s[2][1:], s[3]))

        return (self.start_symbol, self.grammar[self.start_symbol][0], [], 0) in chart[-1]

# Example grammar and test
grammar = {'S': [['A', 'B']], 'A': [['a']], 'B': [['b']]}
parser = EarleyParser(grammar, 'S')
print(parser.parse('ab'))  # Output: True
