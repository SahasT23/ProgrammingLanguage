# TOKENS

# Adding variable types

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

  def __repr__(self):  # Makes it look cleaner on the terminal
    if self.value: return f'{self.type}:{self.value}'
    return f'{self.type}' # Just returns type