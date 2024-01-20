from pathlib import Path

pathbody = "C:/Users/austi/Downloads/pcc_3e-main/pcc_3e-main/chapter_10/exceptions"
filenames = ["alice.txt", 'little_women.txt', 'moby_dick.txt']

for filename in filenames:
    try:
        content = Path(f"{pathbody}/{filename}").read_text(encoding='utf-8')
        print(f"{filename} containes approximately {len(content.split())} words.")
    except Exception as e:
        print(e)