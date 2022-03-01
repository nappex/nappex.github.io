#!/bin/bash

if [ ! "$1" ]
then
    echo "Missing commit message"
    echo "Usage: ./generate_content.sh 'commit message to github'"
    exit 1
fi

if [ ! -d $PWD/__venv__ ]
then
    echo "Creating python virtual env..."
    sleep 1
    python3 -m venv __venv__
fi

if [ ! -d $PWD/output ]
then
    echo "[INFO] Create output dir"
    git clone -b gh-pages git@github.com:nappex/nappex.github.io.git output
fi

source $PWD/__venv__/bin/activate || exit 1
python -m pip install --upgrade pip || exit 1

# install requirements, only if not satisfied


python learn_overview/make_html.py || exit 1


pelican_plugins=(
    "pelican-search"
    "pelican-series"
    "pelican-share-post"
    "pelican-render-math"
    "pelican-related-posts"
    "pelican-neighbors"
)
pip_plugins=$(pip freeze)

for plugin in "${pelican_plugins[@]}"
do
    if [ ! $(echo $pip_plugins | grep $plugin) ]
    then
        python -m pip install $plugin 1>/dev/null || exit 1
        echo "[INSTALLING] pelican-plugin ${plugin}..."
        sleep 1
    else
        echo "[INFO] pelican-plugin ${plugin} is already installed"
    fi
done


if [ ! $(pelican-themes -l | grep elegant) ]
then
    mkdir -p pelican-themes/elegant
    src="https://github.com/Pelican-Elegant/elegant/"
    dst="pelican-themes/elegant"
    git clone --recursive $src $dst 1>/dev/null || exit 1
    pelican-themes -i pelican-themes/elegant || exit 1
    echo "[INFO] pelican-themes created"
fi

pelican || exit 1
git add .
git commit -m "$1"
git push origin master
sleep 1

cd output/
git add .
git commit -m "$1"
git push origin gh-pages

echo Generating completed
