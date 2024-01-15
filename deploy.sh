#!/usr/bin/env bash

# use local hugo binary if present
if [ -f ~/.local/bin/hugo ]; then
  hugo=~/.local/bin/hugo
else
  hugo=hugo
fi

# ensure project root
cd "$(dirname "$0")"

# clean it
rm -rf public

# build it
$hugo --minify

# sync public folder
rsync -av --delete public/ /srv/http/blog/