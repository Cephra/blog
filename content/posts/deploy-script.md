+++
title = 'Deploy Script'
date = 2024-01-16T22:05:00+01:00
draft = true
+++

In case you're wondering how I set up the deploy.sh:
```bash
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
```

I'm building first, then I'm cleaning and redeploying the site. That way I **should** have zero downtime of the blog.

Not that it'd matter if the blog was offline though. ^^