import sys
import re
import click
from bs4 import BeautifulSoup

# launch different file depending on the argument
name = 'fiction'


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




# read file into memory as a string
with open(f'data/{name}.html') as f:
  contents:str = f.read()
  titles:list[str]=process_string(contents)
  print(titles)

# save into output