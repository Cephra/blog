+++
title = 'Migrating to Vue 3'
date = 2024-04-28T19:15:09+02:00
summary = "Migrating from Vue 2 to Vue 3 was a smooth experience with improved performance and codebase. Key changes included switching from webpack to Vite for better development experiences, streamlining the codebase with Vue 3's composability features, and using Git for comparing changes."
+++
## A Smooth Experience

Today I successfully [migrated one of my hobby projects from Vue 2 to Vue 3](https://github.com/Cephra/revue/commit/d60a55cf17f56daa3a574f4a94d4a647597491d5), and it was quite an easy and smooth experience. Vue 3 offers improved performance and a more lightweight codebase compared to its predecessor.

One of the key changes during this migration process was moving from webpack to Vite for my project's build tool. This change brought about better development experiences as Vite offers a faster hot module replacement system, which makes it much easier to see the effects of code changes immediately.

Additionally, by migrating to Vue 3, I noticed that my codebase actually became more streamlined and compact. This is largely due to Vue 3's improved composability and reusability features, which allowed me to remove some unnecessary code and further optimize my application.

The reason for switching from Vue 2 was a no-brainer - the framework has reached its end-of-life milestone on December 31st, 2023. As of that date, Vue 2 is no longer receiving new features, updates, or fixes. With Vue 3 being actively maintained and receiving new features, it was a straightforward decision to make the switch.

Using Git was an instrumental tool during this process as it allowed me to easily compare the differences between the Vue 2 and Vue 3 codebases. This made it much easier to spot any issues or areas that needed attention during the migration process.

In conclusion, migrating from Vue 2 to Vue 3 was relatively seamless, thanks in part to Vite and the use of Git for comparing changes. While making the switch, I also changed from yarn to npm - that decision was purely based on my personal preference. In conclusion, if you're still using Vue 2, I would highly recommend migrating to Vue 3 as it has improved my development workflow and overall performance.
