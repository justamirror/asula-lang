from lexer import Lexer, LexerError

class defaults():
  def print(i, text):
    return print(text)
  def input(i, prompt=''):
    return input(prompt)
  def onerror(i, e):
    return i.exit(f"{e.name}: {e.reason}")
  
class asulaInterpreter():
  def __init__(self, print=defaults.print, input=defaults.input, onerror=defaults.onerror):
    self.print,self.input,self.onerror = print, input, onerror
    rules = [
        ('\d+',             'NUMBER'),
        ('[a-zA-Z_]\w+',    'IDENTIFIER'),
        ('\+',              'PLUS'),
        ('\-',              'MINUS'),
        ('\*',              'MULTIPLY'),
        ('\/',              'DIVIDE'),
        ('\(',              'LP'),
        ('\)',              'RP'),
        ('=',               'EQUALS'),
    ]
    self.lexer =  Lexer(rules, skip_whitespace=True)
    
i = asulaInterpreter()
i.lexer.input('erw = _abc + 12*(R4-623902)  ')
try:
        for tok in i.lexer.tokens():
            print(tok)
except LexerError as err:
        print('LexerError at position %s' % err.pos)

