import sys
import re
import click
from bs4 import BeautifulSoup

# launch different file depending on the argument


# process the whole string 
def process_string(s:str)->(list[str]):
  output_list: list[str] = []
  soup = BeautifulSoup(s, 'html.parser')
  links_list = soup.find_all('a', href=True, title=True)
  for item in links_list:
    test_print = item.string
    if(test_print != None):
      output_list.append(test_print.strip())
  return output_list

def process_file(name:str)-> None:
  print('processing file{name}')
  with open(f'data/{name}.html') as f:
    contents:str = f.read()
    titles:list[str]=process_string(contents)
    print(titles)
    joint_list:str = '\n'.join(titles)
    new_file = open(f'output/{name}.txt', 'w')
    new_file.write(joint_list)
    new_file.close()

# save into output

name = 'fiction'
process_file(name)
print('exiting...')