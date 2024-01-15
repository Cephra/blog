+++
title = "Bug in Auto Deploy"
date = 2024-07-20 11:30:04+00:00
summary = "I solved a race condition in my auto-deployment script by adding a random number to the directory name each time it runs to prevent conflicts.  If this doesn't work long-term, I'll need to investigate further."
+++
## Race Condition Resolved

A recent hiccup in my auto-deployment script has been resolved!

The culprit? A race condition. Both my webhook (triggered by commits into the main branch on github) and a timer (used to schedule future blog post publications) were calling the deployment script around the same time. This led to conflicts, as both events attempted to use the same working directory.

The solution? A touch of randomness!

Now, a unique random number is appended to the directory name each time the deployment script is invoked. This prevents conflicts and ensures a smooth deployment process, no matter how closely those events occur. If this solution doesn't hold, I'll have to dig deeper into the issue.
