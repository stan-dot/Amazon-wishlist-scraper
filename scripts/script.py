import sys
import re
import click
from bs4 import BeautifulSoup

def process_string(s:str)->list[str]:
  output_list: list[str] = []
  soup = BeautifulSoup(s, 'html.parser')
  links_list = soup.find_all('a', href=True, title=True)
  for item in links_list:
    test_print = item.string
    if(test_print != None):
      output_list.append(test_print.strip())
  return output_list

def process_file(name:str)->str:
  print(f'processing file {name}')
  path:str= f'output/{name}.txt'
  if FileCheck(name) == 0:
    return "error"
  with open(f'data/{name}.html') as f:
    contents:str = f.read()
    titles:list[str]=process_string(contents)
    print(f'Processing {len(titles)} items')
    print('Writing to file')
    joint_list:str = '\n'.join(titles)
    new_file = open(path, 'w')
    new_file.write(joint_list)
    new_file.close()
  return path

def FileCheck(name:str)->int:
    try:
      open(f'data/{name}.html', "r")
      return 1
    except IOError:
      print("Error: File does not appear to exist.")
      return 0
  
@click.command()
@click.option("--name", prompt="Enter file in data folder", help="The file in data directory to greet.")
def start(name):
  """Program that reads NAME and extracts the item names."""
  location = process_file(name)
  if(location == 'error'):
    click.echo(f"Exiting!")
    exit()
  click.echo(f"Processed file is available at, {location}!")

if __name__ == '__main__':
    start()