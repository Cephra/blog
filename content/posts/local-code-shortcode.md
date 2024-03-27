+++
title = 'Local Code Shortcode'
date = 2024-01-17T13:17:56+01:00
summary = 'Short post about how I solved showing codefiles from the project root'
+++

I've created a HUGO Shortcode to be able to include code files from this project.

{{< codeinclude "go-html-template" "layouts/shortcodes/codeinclude.html" >}}

I use it in this post like so:

{{< codeinclude "text" "content/posts/local-code-shortcode.md" >}}