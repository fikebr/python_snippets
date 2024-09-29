# pprint is a builtin module
import pprint
from pprint import pp

data = {"name": "John Doe", "age": 30, "city": "New York"}

pprint.pprint(data)
pprint.pp(data) # the same as above
pp(data)
