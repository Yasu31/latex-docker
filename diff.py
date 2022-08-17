import os

"""
a convenience script to easily generate latexdiffs for projects with multiple tex files

how to use:
1. copy the old version to old/, and the new version to new/
2. install latex, or use the docker image to enter latex-enabled environment
  `docker run --rm -it -v $(pwd):/workdir yasu31/jsk-latex-docker /bin/bash`
3. run this script
4. go to the diff/ folder, and compile PDF:
```
pdflatex main
bibtex main
pdflatex main
pdflatex main
```
"""

# first copy everything in new/ to /diff (since materials like images can't be diff'ed)
os.system("cp -r new/ diff/")

# find files that end in .tex in the old/ directory
tex_files = [f for f in os.listdir('old/') if f.endswith('.tex')]

for tex_file in tex_files:
    # run bash command to generate diff file
    print(f"diffing {tex_file}...")
    os.system(f'latexdiff old/{tex_file} new/{tex_file} > diff/{tex_file}')