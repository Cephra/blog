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
CONTENTPROMPT="\
    Write a blog post based on the following text, \
    but ignore everything between the first two occurences of \"+++\". \
    This is the text: \
    $(cat $POSTFILE) $input_text \
"
echo $CONTENTPROMPT
ollama run gemma "$CONTENTPROMPT" >> content/posts/$1.md

DESCRPROMPT="Generate a short description of the following blog post.
Keep it short and concise. Here's the post: \"$(cat $POSTFILE)\""
echo $DESCRPROMPT
DESCRIPTION=$(
    ollama run gemma "$DESCRPROMPT"
)
sed -i "s/+++$/summary = $DESCRIPTION&/" $POSTFILE
