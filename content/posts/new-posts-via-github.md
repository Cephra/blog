+++
title = 'New Posts via GitHub'
date = 2024-01-17T10:33:41Z
+++

I've just added a new GitHub Workflow allowing me to quickly create
new posts by creating a new branch within the "posts/" directory.

Once that branch is created, the workflow runs a hugo command adding a new content file template.
All I have to do after that is edit the file in the branch and then I can commit it.

```yaml
name: Auto-create new posts for branches in posts/

on:
    push:
        branches:
        - 'posts/**'

permissions: 
    contents: write
    
jobs:
    create-tag:
        if: github.event.created
        runs-on: ubuntu-latest
        steps:
            -
                name: Checkout repository
                uses: actions/checkout@v4
            -
                name: Extract branch name
                id: extract_branch
                run: echo "::set-output name=branch::$(echo ${GITHUB_REF#refs/heads/posts/})"
            -   
                name: Setup Hugo
                uses: peaceiris/actions-hugo@v2
            -
                name: Create post
                run: hugo new content posts/${{ steps.extract_branch.outputs.branch }}.md
            - 
                name: Commit new post file
                run: |
                    git config --local user.email "github-actions[bot]@users.noreply.github.com"
                    git config --local user.name "github-actions[bot]"
                    git add .
                    git commit -m "added new post"
            -
                name: Push changes
                uses: ad-m/github-push-action@master
                with:
                    github_token: ${{ secrets.GITHUB_TOKEN }}
                    branch: ${{ github.ref }}
```

When I'm done, all I have to do is push the branch in main and the webhook will take care of publishing the changes.
