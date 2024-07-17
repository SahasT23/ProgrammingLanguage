####################
# CONSTANTS
####################

DIGITS = '0123456789'

####################
# ERRORS
####################

class Error:
    def __init__(self, error_name, pos_start, pos_end, details):
        self.error_name = error_name
        self.pos_start = pos_start
        self.pos_end = pos_end
        self.details = details

    def as_string(self):
        result = f'{self.error_name}: {self.details}\n'
        result += f'FILE {self.pos_start.fn}, LINE {self.pos_start.ln + 1}'
        return result

class IllegalCharError(Error):
    def __init__(self, details, pos_start, pos_end):
        super().__init__('Unknown/Illegal Character Used', pos_start, pos_end, details)

####################
# POSITION
####################

class Position:
    def __init__(self, idx, ln, col, fn, ftxt): # index, line, column, file name, file text
        self.idx = idx
        self.ln = ln
        self.col = col
        self.fn = fn
        self.ftxt = ftxt

    def advance(self, current_char):
        self.idx += 1
        self.col += 1

        if current_char == '\n':
            self.ln += 1
            self.col = 0

        return self
  
    def copy(self):
        return Position(self.idx, self.ln, self.col, self.fn, self.ftxt)

####################
# TOKENS
####################

ST_INT = 'INT'
ST_FLOAT = 'FLOAT'
ST_PLUS = 'PLUS'
ST_MINUS = 'MINUS'
ST_MUL = 'MUL'
ST_DIV = 'DIV'
ST_LPAREN = 'LPAREN'
ST_RPAREN = 'RPAREN'

class Token:
    def __init__(self, type_, value=None):
        self.type = type_
        self.value = value

    def __repr__(self):
        if self.value:
            return f'{self.type}:{self.value}'
        return f'{self.type}'

####################
# LEXER
####################

class Lexer:
    def __init__(self, fn, text):
        self.fn = fn
        self.text = text
        self.pos = Position(-1, 0, -1, fn, text)
        self.current_char = None
        self.advance()

    def advance(self):
        self.pos.advance(self.current_char)
        self.current_char = self.text[self.pos.idx] if self.pos.idx < len(self.text) else None

    def make_tokens(self):
        tokens = []

        while self.current_char is not None:
            if self.current_char in ' \t':
                self.advance()
            elif self.current_char in DIGITS:
                tokens.append(self.make_number())
            elif self.current_char == '+':
                tokens.append(Token(ST_PLUS))
                self.advance()
            elif self.current_char == '-':
                tokens.append(Token(ST_MINUS))
                self.advance()
            elif self.current_char == '*':
                tokens.append(Token(ST_MUL))
                self.advance()
            elif self.current_char == '/':
                tokens.append(Token(ST_DIV))
                self.advance()
            elif self.current_char == '(':
                tokens.append(Token(ST_LPAREN))
                self.advance()
            elif self.current_char == ')':
                tokens.append(Token(ST_RPAREN))
                self.advance()
            else:
                pos_start = self.pos.copy()
                char = self.current_char
                self.advance()
                return [], IllegalCharError("'" + char + "'", pos_start, self.pos)

        return tokens, None

    def make_number(self):
        num_str = ''
        dot_count = 0

        while self.current_char is not None and self.current_char in DIGITS + '.':
            if self.current_char == '.':
                if dot_count == 1:
                    break
                dot_count += 1
                num_str += '.'
            else:
                num_str += self.current_char
            self.advance()

        if dot_count == 0:
            return Token(ST_INT, int(num_str))
        else:
            return Token(ST_FLOAT, float(num_str))

####################
# RUN FUNCTION
####################

def run(fn, text):
    lexer = Lexer(fn, text)
    tokens, error = lexer.make_tokens()
    return tokens, error
