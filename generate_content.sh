#!/bin/sh

if [ ! "$1" ]
then
    echo "Missing commit message"
    echo "Usage: ./generate_content.sh 'commit message to github'"
    exit 1
fi

if ! [ -d $PWD/output ]
then
    echo "[INFO] Create output dir"
    git clone -b gh-pages git@github.com:nappex/nappex.github.io.git output
fi

./learn_overview/make_html.py
source __venv__/bin/activate

if ! [ $(pelican-themes -l | grep elegant) ]
then
    mkdir -p pelican-themes/elegant
    git clone --recursive https://github.com/Pelican-Elegant/elegant pelican-themes/elegant
    pelican-themes -i pelican-themes/elegant
fi

pelican
git add .
git commit -m "$1"
git push origin master
sleep 1

cd output/
git add .
git commit -m "$1"
git push origin gh-pages

echo Generating completed