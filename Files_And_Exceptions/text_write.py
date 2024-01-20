from pathlib import Path

path = Path('sample.txt')

# Only the third write_text() below will matter
path.write_text("This is sample text")
path.write_text("\nThis is multiline sample text.\nLook at how many lines I am!\nThree! Or Four, depending on if you count the first line, which wasn't multiline, but has become multiline by virtue of these following lines!")
path.write_text("path.write_text(str) completely overwrites the previous value")