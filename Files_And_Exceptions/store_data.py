# Examples of storing data in JSON format

from pathlib import Path
import json

numbers = [2, 4, 5, 6, 7, 8, 10, 12, 14, 15, 20, 211, 245, 414, 1006]

path = Path('numbers.json')
contents = json.dumps(numbers)
path.write_text(contents)

# The lines above, as written, will simply store the array "numbers" as a string with no key in a .json file
# It does not, itself, create valid JSON

contents = path.read_text()
print(contents)