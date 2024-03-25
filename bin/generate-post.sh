#!/usr/bin/env bash

# change working dir
cd $(dirname $0)/..

POST=posts/$1.md
POSTFILE=content/$POST

# Read input text from the user
read input_text

# Create a new posts based on the first parameter
hugo new content $POST

POSTCONTENT=$(cat $POSTFILE)

# Pipe the input text to ollama run gemma command and append it to blog post
ollama run gemma <<EOF | cat <(echo) - >> $POSTFILE
You are supposed to write a blog post based on input.
The file currently has the following content:
"$POSTCONTENT"
Ignore everything inbetween the +++
Please continue the blog post based on the following input:
"$input_text"
EOF

POSTCONTENT=$(cat $POSTFILE)
ollama run gemma <<EOF
Write a short description of a blog post.
The blog post currently has the following content:
"$POSTCONTENT"
Ignore everything inbetween the +++.
EOF

#
#DESCRPROMPT="Generate a short description of the following blog post.
#Keep it short and concise. Here's the post: \"$(cat $POSTFILE)\""
#echo $DESCRPROMPT
#DESCRIPTION=$(
#    ollama run gemma "$DESCRPROMPT"
#)
#echo $DESCRIPTION
##sed -i "s/+++$/summary = $DESCRIPTION&/" $POSTFILE
#