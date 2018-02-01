#!/bin/sh

set -e

setup_git() {
  git config --global user.email "travis@travis-ci.org"
  git config --global user.name "Travis CI"
}

commit_files() {
  git checkout -b master
  git add .
  git commit --allow-empty -m "Travis build: $TRAVIS_BUILD_NUMBER"
}

upload_files() {
  git remote add origin-pages https://${GH_TOKEN}@github.com/c4cs/c4cs.github.io.git > /dev/null 2>&1
  git push --quiet --set-upstream origin-pages master
}

if [ "$TRAVIS_EVENT_TYPE" == "cron" ] do
  then
  setup_git
  commit_files
  upload_files
fi
