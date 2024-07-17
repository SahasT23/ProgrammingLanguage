import BasicClone

while True:
  text = input('basic > ')
  result, error = BasicClone.run(text)

  if error: print(error.as_string())
  else: print(result)