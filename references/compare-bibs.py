# Read the content of File 1
with open('bibliography.bib', 'r') as file:
    file1_content = file.read()

# Read the content of File 2
with open('bib-new.bib', 'r') as file:
    file2_content = file.read()

# Extract titles from File 1
file1_titles = set()
for line in file1_content.split('\n'):
    if line.strip().startswith('title = {'):
        title = line.strip()[9:-1]
        file1_titles.add(title)

# Extract titles from File 2
file2_titles = set()
for line in file2_content.split('\n'):
    if line.strip().startswith('title = {'):
        title = line.strip()[9:-1]
        file2_titles.add(title)

# Check if all titles from File 1 are present in File 2
missing_titles = file1_titles - file2_titles
if missing_titles:
    print("The following titles from File 1 are missing in File 2:")
    for title in missing_titles:
        print("- ", title)
else:
    print("All titles from File 1 are present in File 2.")

