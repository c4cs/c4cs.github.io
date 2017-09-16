#!/bin/bash
set -e #Exit on error instead of continuing

build_pdfs() {
    pwd
    pushd .
    cd ./static/raw
    ls
    ./seed_hw.py
    popd

    pushd .
    cd ./static/f17/hw/
    ls
    echo "Building homework PDFs"
    text_to_pdf
    clean_up

    popd
    cd ./static/f17/advanced/
    ls
    echo "Building advanced homework PDFs"
    text_to_pdf
    clean_up
}

clean_up() {
    rm *.aux *.log *.out
}

text_to_pdf() {
    for file in *.tex; do
        bundle exec pdflatex $file > /dev/null 2>&1
    done
}

build_pdfs
