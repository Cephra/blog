#!/usr/bin/env bash

# ensure project root
cd "$(dirname "$0")"

# fetch new
git pull
# build it
hugo --minify

# clean old
rm -rf /srv/http/blog/*
# copy it
cp -r public/* /srv/http/blog/