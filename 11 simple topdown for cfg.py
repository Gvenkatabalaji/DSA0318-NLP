class TopDownParser:
    def __init__(self, grammar, start_symbol):
        self.grammar = grammar
        self.start_symbol = start_symbol

    def parse(self, input_string):
        self.input_string, self.position = input_string, 0
        return self._parse_symbol(self.start_symbol) and self.position == len(self.input_string)

    def _parse_symbol(self, symbol):
        if symbol.islower():  
            if self.position < len(self.input_string) and self.input_string[self.position] == symbol:
                self.position += 1
                return True
            return False
        return any(self._try_production(prod) for prod in self.grammar.get(symbol, []))

    def _try_production(self, production):
        old_pos = self.position
        if all(self._parse_symbol(sym) for sym in production):
            return True
        self.position = old_pos
        return False
grammar = {'S': [['A', 'B']], 'A': [['a']], 'B': [['b']]}
parser = TopDownParser(grammar, 'S')
print(parser.parse('ab'))  
