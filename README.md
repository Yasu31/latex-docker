# latex-docker
By using a Docker image, latex documents can be compiled in your local environment (Windows, macOS, or Linux) without needing to install latex locally. This repository does not have to be cloned to use the Docker image.

* Dockerhub: https://hub.docker.com/repository/docker/yasu31/latex-docker
* Repository: https://github.com/Yasu31/latex-docker

# setup
## install Docker
Get the GUI version (https://docs.docker.com/get-docker/) or the CLI version, whichever works for you

# usage
## run the docker image
1. Open the terminal and navigate to the directory with the latex source files
    ```bash
    # e.g. on Linux, macOS...
    cd /path/to/your_latex_project
    ```
1. run container
    ```bash
    # on Linux and macOS
    docker run --rm -it -v $(pwd):/workdir yasu31/latex-docker
    # on Windows
    docker run --rm -it -v ${pwd}:/workdir yasu31/latex-docker
    ```
    If it tells you "Docker daemon not running", the "Docker Desktop" application will have to be manually started (happens if not set to auto-launch on boot)
1. once inside the Docker container, compile the latex document
    ```bash
    pdflatex your_main_filename
    ```

---

tip: if your project contains bibtex files, run
```bash
pdflatex your_main_filename
bibtex your_main_filename
pdflatex your_main_filename
pdflatex your_main_filename
```
to make sure the references are correctly resolved.

---

## use latexdiff to compare two versions of a document
1. structure the latex source files as follows:
    ```
    your_project
    |- old/
    |   `- [source files for the old version]
    |- new/
    |   `- [source files for the new version]
    `- diff/
        `- [leave it empty]
    ```
1. go to this directory in the terminal and run Docker
1. generate the diff files
    ```bash
    python3 generate_diff.py
    ```
1. navigate to the diff/ directory and compile the generated latex document as you would a normal latex document