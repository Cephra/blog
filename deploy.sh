#!/usr/bin/env bash

# ensure project root
cd "$(dirname "$0")"

# fetch new
git pull
# build it
hugo --minify

# sync public folder
rsync -av --delete public/ /srv/http/blog/