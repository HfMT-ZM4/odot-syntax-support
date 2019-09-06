# pl2tml

import sys
import shlex
import re

PLISTHEADER = """\
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple Computer//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
"""
indentsize = 2
current_indent = indentsize

def incr_indent():
  global current_indent
  current_indent += indentsize

def decr_indent():
  global current_indent
  current_indent -= indentsize

def indent():
  global current_indent
  return current_indent*' '

def writeln (text):
  print '%s%s' % (indent(), text)

key_mode = True
quote = re.compile ('&quot', re.IGNORECASE)

def handle_token (token):
  global key_mode
  if token == '{':
    writeln ('<dict>')
    incr_indent()
    key_mode = True
  elif token == '}':
    decr_indent()
    writeln ('</dict>')
  elif token == '(':
    writeln ('<array>')
    incr_indent()
    key_mode = False
  elif token == ')':
    decr_indent()
    writeln ('</array>')
  elif token == ';':
    key_mode = True
  elif token == ',':
    pass
  elif token == '=':
    key_mode = False
  else:
    if key_mode:
      writeln ('<key>%s</key>' % token)
    else:
      not_string_token = quote.sub ("'", token [1:-1])
      writeln ('<string>%s</string>' % not_string_token)

def pretty_print (lexer):
  count = 0
  lexer.commenters = '//'
  while True :
    token = lexer.get_token()
    if token == '': return
    count += 1
    handle_token (token)

def main ():
  for filename in sys.argv [1:]:
    print PLISTHEADER
    print '<plist version=\"1.0\">'
    pretty_print (shlex.shlex (open (filename)))
    print '</plist>'

if __name__ == "__main__":
  main ()