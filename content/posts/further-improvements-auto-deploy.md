+++
title = "Further Improvements for Auto Deploy"
date = 2024-07-26 13:30:04+20:00
summary = "I share a enhanced deployment script that resolves race condition issues by appending a unique random number and Unix timestamp to the directory name."
+++
## Enhanced Deployment Solution

Building on the success of my [previous solution](/posts/bug-in-auto-deploy) to the race condition issue, I've further improved the deployment script.

As mentioned before, a unique random number is appended to the directory name each time the deployment script is invoked. However, to prevent edge cases where two events might still occur around the same time with the same random number, I've added an additional check: verifying if the directory already exists before creating it.

Furthermore, I now also append a Unix timestamp to the directory name, ensuring that each invocation results in a uniquely named directory.

```bash
#!/usr/bin/env bash

# go home
cd ~

# generate random deployment dir name (prevents race conditions)
function get_deployment_dir {
        DEPLOYMENT_DIR=deploy_$(date +%s)_$RANDOM
}
while
        get_deployment_dir
        [[ -d "$DEPLOYMENT_DIR" ]]
do true; done

# clone git 
git clone --depth 1 "$1" $DEPLOYMENT_DIR

cd $DEPLOYMENT_DIR

./deploy.sh

cd ..

rm -rf $DEPLOYMENT_DIR
```

This enhancement has proven effective in preventing conflicts and ensuring smooth deployments, even when triggered by closely spaced events.
