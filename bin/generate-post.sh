#!/usr/bin/env bash

# change working dir
cd $(dirname $0)/..

POST=posts/$1.md
POSTFILE=content/$POST

# Read input text from the user
read input_text

# Create a new posts based on the first parameter
hugo new content $POST

# Pipe the input text to ollama run gemma command and append it to blog post
ollama run gemma "\
Write a blog post based on the following text. Add a summary field to the toml header.\
$(cat $POSTFILE) $input_text \
" >> content/posts/$1.md