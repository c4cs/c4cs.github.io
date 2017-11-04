#!/bin/sh
set -e # exit with non-zero code if an error occurs

SOURCE_BRANCH="master"

check_push_conditions() {
    # If there are no changes to the compiled out
    if git diff --quiet; then
        echo "No changes to the output on this push; exiting."
        exit 0
    fi

    # Pull requests and commits to other branches shouldn't try to deploy, just build to verify
    if [ "$TRAVIS_PULL_REQUEST" != "false" -o "$TRAVIS_BRANCH" != "$SOURCE_BRANCH" ]; then
        echo "Skipping deploy for this commit (probably a pull request or non-master branch)"
        exit 0
    fi
}

setup_git() {
    git config --global user.email "travis@travis-ci.org"
    git config --global user.name "Travis CI"
}

commit_pdfs() {
    git checkout ${SOURCE_BRANCH}
    git add ./static/f17/hw/*.pdf ./static/f17/advanced/*.pdf
    git commit --message "Travis building PDFs: $TRAVIS_BUILD_NUMBER"
}

upload_files() {
    echo "Pushing PDF changes to master"
    git remote add origin https://${GH_TOKEN}@github.com/c4cs/c4cs.github.io.git > /dev/null 2>&1
    git push --quiet --set-upstream origin master
}

check_push_conditions
setup_git
commit_pdfs
upload_files
