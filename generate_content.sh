#!/bin/sh

if [ ! "$1" ]
then
    echo "Missing commit message"
    echo "Usage: ./generate_content.sh 'commit message to github'"
    exit 1
fi

if [ ! -d $PWD/output ]
then
    echo "[INFO] Create output dir"
    git clone -b gh-pages git@github.com:nappex/nappex.github.io.git output
fi

./learn_overview/make_html.py
source __venv__/bin/activate || exit 1
python -m pip install --upgrade pip || exit 1

if [ ! -d $PWD/pelican-plugins ]
then
    pelican_plugins=(
        "pelican-search"
        "pelican-series"
        "pelican-share-post"
        "pelican-render-math"
        "pelican-related-posts"
        "pelican-neighbors"
    )

    for plugin in "${pelican_plugins[@]}"
    do
        python -m pip install $plugin 1>/dev/null || exit 1
        echo "[INFO] pelican-plugin ${plugin} was created"
        sleep 1
    done
fi

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
