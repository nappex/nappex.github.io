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
source __venv__/bin/activate

if [ ! -d $PWD/pelican-plugins ]
then
    plugins=(
        "extract_toc"
        "neighbors"
        "related_posts"
        "render_math"
        "series"
        "share_post"
    )

    for plugin in "${plugins[@]}"
    do
        mkdir -p pelican-plugins/$plugin
        src="https://github.com/getpelican/pelican-plugins/${plugin}"
        dst="pelican-plugins/${plugin}"
        git clone --recursive $src $dst 1>/dev/null
        echo "[INFO] pelican-plugin ${plugin} was created"
        sleep 0.5
    done

    mkdir -p pelican-plugins/search
    git clone --recursive https://github.com/pelican-plugins/search pelican-plugins/search 1>/dev/null
    echo "[INFO] pelican-plugin search was created"
    sleep 0.5
fi

if [ ! $(pelican-themes -l | grep elegant) ]
then
    mkdir -p pelican-themes/elegant
    src="https://github.com/Pelican-Elegant/elegant/"
    git clone --recursive https://github.com/Pelican-Elegant/elegant pelican-themes/elegant
    pelican-themes -i pelican-themes/elegant
    echo "[INFO] pelican-themes created"
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
