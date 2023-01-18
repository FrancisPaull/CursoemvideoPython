def not_string(frase):
  if frase[0:2] == 'not':
     return True
  else:
      frase = "not " + frase
      return frase



print(not_string('not quql'))

print(not_string('x'))

print(not_string('not é ruim'))

print(not_string('ruim'))

print(not_string('not'))

print(not_string('not é'))

print(not_string('not'))