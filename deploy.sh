#!/usr/bin/env bash

# use local hugo binary if present
if [ -f ~/.local/bin/hugo ]; then
  alias hugo=~/.local/bin/hugo
fi

# ensure project root
cd "$(dirname "$0")"

# fetch new
git pull
# build it
hugo --minify

# sync public folder
rsync -av --delete public/ /srv/http/blog/