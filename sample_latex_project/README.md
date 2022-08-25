sample project to try out with latex-docker

for Linux / macOS...
```bash
cd /path/to/sample_latex_project
docker run --rm -it -v $(pwd):/workdir yasu31/latex-docker
# then, once inside the docker image...
pdflatex main
```

template used from https://github.com/bamos/latex-templates/tree/master/latex-templates/hw