from pathlib import Path

path = Path('pi_digits.txt')
contents = path.read_text()
print(contents.strip())

path2 = Path('sub_folder/song_name.txt')
contents2 = path2.read_text()
print(contents2.strip())


# I couldn't figure out a way to easily go to the parent folder, and had to use Absolute paths here
path3 = Path('C:\Coding\Python\Basic Concepts\lorem.txt')
contents3 = path3.read_text()
print(contents3.strip())

lined_up = contents.splitlines()
lined_up_and_stripped = []
for index in range(len(lined_up)):
    lined_up_and_stripped.append(lined_up[index].strip())

print(lined_up_and_stripped)
