# jsk-latex-docker
Dockerを使ってJSKのlatexテンプレートを使った文章をコンパイルできます。latexを直接インストールしなくてもコンパイルできるようになります。(ci-thesisでのみ確認)

* Dockerhub: https://hub.docker.com/repository/docker/yasu31/jsk-latex-docker
* Repository: https://github.com/Yasu31/jsk-latex-docker

# ローカルPC上での使い方
`docker run ...`時にDockerhubからプルしてくれるので、このレポジトリをcloneする必要はないです
```bash
cd /path/to/your-thesis
# on Linux
docker run --rm -it -v $(pwd):/workdir yasu31/jsk-latex-docker
# on Windows
docker run --rm -it -v ${pwd}:/workdir yasu31/jsk-latex-docker
```
デフォルトでは`make`を実行しますが、コマンドの最後に`make clean`、`pdfcrop hogehoge.pdf`(PDFの余白をクロップしてくれる)とかを追加すればそっちが実行されます。もっと凝ったコマンドを送りたければコマンドの最後に`/bin/bash -c "cd robomech; ls -l"`とすればbashコマンドが送れます。
# GitLab CI上での使い方
以下の内容でレポジトリのrootに`.gitlab-ci.yml`というファイルを作成します。CIが通ったら、"Download artifacts"で、コンパイルされた結果のPDFをダウンロードすることができます。
```yaml
image: yasu31/jsk-latex-docker
compile-latex:
  script:
    - make
  artifacts:
    paths:  
      - main.pdf
```

# GitHub Actions上での使い方
GitHubにpushされるたびにGitHub Actions上でコンパイルされ、出力されたPDFをダウンロードすることができます。GitHub Actionsの無料枠には制限があるので注意。無料枠は毎月3000分ですが、自分の場合ci-thesisだと全体の処理に2分程度かかりました。

レポジトリのrootに`.github/workflows/compile_pdf.yml`というファイルを作成し、以下をコピペしてpushすれば動いてくれるはずです
```yaml
on: [push]

jobs:
  compile-pdf:
    runs-on: ubuntu-latest
    container:
      image: yasu31/jsk-latex-docker
    steps:
    - name: Set up Git repository
      uses: actions/checkout@v1
    - name: Compile LaTeX document
      run: make
    - name: Upload PDF to workflow tab
      uses: actions/upload-artifact@v2
      with:
        name: PDF
        path: main.pdf
```
