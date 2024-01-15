+++
title = 'New Posts via GitHub'
date = 2024-01-17T10:33:41Z
+++

I've just added a new GitHub Workflow allowing me to quickly create
new posts by creating a new branch within the "posts/" directory.

Once that branch is created, the workflow runs a hugo command adding a new content file template.
All I have to do after that is edit the file in the branch and then I can commit it.

{{< codeinclude "yaml" ".github/workflows/create-post.yml" >}}

When I'm done, all I have to do is push the branch in main and the webhook will take care of publishing the changes.

It's kinda cool!
