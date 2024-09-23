from pathlib import Path
path = Path('ply.txt')
print(path.read_text().strip())