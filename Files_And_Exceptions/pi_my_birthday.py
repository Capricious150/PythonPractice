from pathlib import Path

path = Path(f'C:/Users/austi/Downloads/pcc_3e-main/pcc_3e-main/chapter_10/reading_from_a_file/pi_million_digits.txt')
contents = path.read_text()

bday = input("Please enter birthday in format mmddyyyy")

if bday in contents:
    print(contents.find(bday))
else:
    print(f"Not found in {len(contents)} digits of pi")