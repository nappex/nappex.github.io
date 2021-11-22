#!/bin/sh

if [ ! "$1" ]
then
    echo "Missing commit message\n"
    echo "Usage: ./generate_content.sh 'commit message to github'\n"
    exit 1
fi

pelican
git add .
git commit -m "$1"
git push origin master

cd output/
git add .
git commit -m "$1"
git push origin gh-pages

echo Generating completed