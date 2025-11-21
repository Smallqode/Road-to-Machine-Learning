from pathlib import Path
import os

def readfileandfolder():
  path = Path('')
  items = list(path.rglob('*'))
  for i, items in enumerate(items):
    print(f'{i + 1} : {items}')

def createfile():
  try:
    readfileandfolder()
    name = input('Specify your file name: ')
    p = Path(name)
    if not p.exists() and p.is_file():
      with open (p, 'w') as fs:
        data = input('What you want to write in this file: ')
        fs.write(data)
      print('FILE CREATED SUCCESSFULLY')
    else:
      print('This file already exists')

  except Exception as err:
    print(f'An error has occured as {err}')

def readfile():
  try:
    readfileandfolder()
    name = input('Specify your file name to write: ')
    p = Path(name)
    if p.exists() and p.is_file():
      with open (p, 'r') as fs:
        data = fs.read()
        print(data)
      print('FILE HAS BEEN READ SUCCESSFULLY')
    else:
      print('This file does not exist')
  except Exception as err:
    print(f'An error has occured as {err}')

def updatefile():
  try:
    readfileandfolder()
    name = input('Specify your file name to update: ')
    p = Path(name)
    if p.exists() and p.is_file():
      print('Press 1 to change the file name')
      print('Press 2 to overwrite the data in your file')
      print('Press 3 to append something in your file')

      response = int(input('Tell your response: '))
      
      if response == 1:
        with open(p, 'w') as fs:
          name2 = input('Write your new file name: ')
          p2 = Path(name2)
          p.rename(p2)

      if response == 2:
        with open(p, 'w') as fs:
          data = input('Tell what you want to overwrite')
          fs.write(data)

      if response == 3:
        with open(p, 'a') as fs:
          data = input('Tell what you want to add')
          fs.write('' + data)
  
  except Exception as err:
    print(f'An error has occured as {err}')

def deletefile():
  try:
    readfileandfolder()
    name = input('Which file you want to delete: ')
    p = Path(name)

    if p.exists() and p.is_file():
      os.remove(name)
      print('File removed successfully.')
    else:
      print('No such file exists')
  
  except Exception as err:
    print(f'An error has occured as {err}')


print('Press 1 to create a file')
print('Press 2 to read a file')
print('Press 3 to update a file')
print('Press 4 to delete a file')

check = int(input('Give a response: '))

if check == 1:
  createfile()

if check == 2:
  readfile()

if check == 3:
  updatefile()

if check == 4:
  deletefile()