#!/bin/sh

# simple script to build and push to gh-pages
# designed to be run from master

# make the docs
make html

# copy to other repo (on the gh-pages branch)
cp -R build/html/ ../../IntroPython2016a-ghpages
cd ../../IntroPython2016a-ghpages
git checkout gh-pages
touch .nojekyll  # Make sure the repo has this file in its root, otherwise it will not render on github.io
git add *  # in case there are new files added
git commit -a -m "updating presentation materials"
git pull -s ours
git push
