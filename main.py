from pathlib import Path

def readfileandfolder():
  path = Path('')
  items = list(path.rglob('*'))
  for i, items in enumerate(items):
    print(f'{i + 1} : {items}')

def createfile():
  readfileandfolder()
  name = input('Specify your file name: ')
  p = Path(name)
  with open (p, 'w') as fs:
    data = input('What you want to write in this file: ')
    fs.write(data)
  print('FILE CRATED SUCCESSFULLY')

print('Press 1 to create a file')
print('Press 2 to read a file')
print('Press 1 to update a file')
print('Press 1 to delete a file')

check = int(input('Give a response: '))

if check == 1:
  createfile()