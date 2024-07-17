####################
# CONSTANTS
####################


DIGITS = '0123456789'


####################
# ERRORS
####################


class Error:
  def __init__(self, error_name, details):
    self.error_name = error_name
    self.details = details

  def as_string(self):
    result = f'{self.error_name}: {self.details}'
    return result
  
class IllegalCharError(Error):
  def __init__(self, details):
    super().__init__('Unknown/Illegal Character Used')


####################
# TOKENS
####################


ST_INT = 'ST_INT'
ST_FLOAT = 'FLOAT' 
ST_PLUS = 'PLUS'
ST_MINUS = 'MINUS'
ST_MUL = 'MUL'
ST_DIV = 'DIV'
ST_LPAREN = 'LPAREN'
ST_RPAREN = 'RPAREN'

class Token:
  def __init__(self, type_, value):
    self.type = type
    self.value = value

  def __repr__(self):
    if self.value: return f'{self.type}:{self.value}'
    return f'{self.type}' 


####################
# LEXER
####################


class Lexer:
  def __init__(self, text):
    self.text = text
    self.pos = -1
    self.current_char = None
    self.advance()

  def advance(self):
    self.pos += 1
    self.current_char = self.text[pos] if self.pos < len(self.text) else None

  def make_tokens(self):
    tokens = []

    while self.current_char != None:
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
        # return errors
    
    return tokens
  
  def make_number(self):
    num_str = ''
    dot_count = 0

    while self.current_char != None and self.current_char in DIGITS + '.':
      if self.current_char == '.':
        if dot_count == 1: break
        dot_count += 1
        num_str += '.' 
      else:
        num_str += self.current_char

    if dot_count == 0:
      return Token(ST_INT, int(num_str))
    else:
      return Token(ST_FLOAT, float(num_str))     
      

