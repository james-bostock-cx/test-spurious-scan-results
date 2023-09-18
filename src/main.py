# Password: even_more_secret
import base64
import os
import sys

if __name__ == '__main__':
  for arg in sys.argv[1:]:
    if arg.startswith('./'):
      os.remove(base64.b64encode(arg))
