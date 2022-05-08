#!/bin/bash

if [ ! "$1" ]
then
    echo "Missing commit message"
    echo "Usage: ./generate_content.sh 'commit message to github'"
    exit 1
fi

if [ ! -d $PWD/__venv__ ]
then
    echo "[INFO] Creating python virtual env..."
    python3 -m venv __venv__
    printf " ✅\n"
fi

if [ ! -d $PWD/output ]
then
    echo "[INFO] Create output dir"
    git clone -b gh-pages git@github.com:nappex/nappex.github.io.git output
fi

source $PWD/__venv__/bin/activate || exit 1
python -m pip install --upgrade pip || exit 1

pip_plugins=$( pip freeze )
needed_pkgs=$( cat $PWD/requirements.txt )

# install requirements, only if not satisfied
for pkg in $needed_pkgs
do
    found=$( echo $pip_plugins | grep -io "${pkg}=" )
    if [ ! $found ]
    then
        printf "[INSTALLING] python package ${pkg}..."
        python -m pip install $pkg 1>/dev/null || exit 1
        printf " ✅\n"
    else
        echo "[INFO] python package ${pkg} is already installed"
    fi
done

python learn_overview/make_html.py || exit 1

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
    found=$( echo $pip_plugins | grep -io $plugin )
    if [ ! $found ]
    then
        printf "[INSTALLING] pelican-plugin ${plugin}..."
        python -m pip install $plugin 1>/dev/null || exit 1
        printf " ✅\n"
    else
        echo "[INFO] pelican-plugin ${plugin} is already installed"
    fi
done


if [ ! -d "pelican-themes/elegant" ]
then
    mkdir -p pelican-themes/elegant
    src="https://github.com/Pelican-Elegant/elegant/"
    dst="pelican-themes/elegant"
    git clone --recursive $src $dst 1>/dev/null || exit 1
    echo "[INFO] dir pelican-themes/elegant created"
    sleep 0.5
fi

if [ ! $( pelican-themes -l | grep elegant ) ]
then
    printf "[INSTALLING] pelican-themes/elegant..."
    pelican-themes -i pelican-themes/elegant || exit 1
    printf " ✅\n"
fi

printf "[INFO] Generating output files...\n" # this is not write to stdout it is very strange behaviour

pelican || exit 1
printf " ✅\n"

# push changes to github
printf "[INFO] Pushing changes to master...\n"
git add .
git commit -m "$1"
git push origin master || printf "[INFO] Changes not pushed to master ❌\n"
sleep 0.5
printf "[INFO] Changes pushed to master ✅\n"

printf "[INFO] Pushing changes to gh-pages...\n"
cd output/
git add .
git commit -m "$1"
git push origin gh-pages || printf "[INFO] Changes not pushed in gh-pages ❌\n"
sleep 0.5
printf "[INFO] Changes pushed to gh-pages ✅\n"

echo Process completed
