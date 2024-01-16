#/usr/bin/env bash

# ensure project root
cd "$(dirname "$0")"
# clean old
rm -rf /srv/http/blog/*
# fetch new
git pull
# build it
hugo --minify
# copy it
cp -r public/* /srv/http/blog/