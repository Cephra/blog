#!/usr/bin/env bash

# change working dir
cd "$(dirname "$0")/.."

POST=posts/$1.md
POSTFILE=content/$POST
MODELNAME=llama3

# Read post
function read_post()  {
    POSTHEADER=$(pcregrep -M '^\+\+\+$(\n|.)*^\+\+\+$' $POSTFILE)
    POSTHEADER_STRIPPED=$(echo "$POSTHEADER" | sed '1d;$d')
    POSTHEADER_LINES=$(echo $(echo "$POSTHEADER" | wc -l)+1 | bc)
    POSTCONTENT=$(cat "$POSTFILE" | tail -n +$POSTHEADER_LINES)
}

function write_post_header() {
    cat <<EOF > $POSTFILE
+++
$POSTHEADER_STRIPPED
$POSTDESCRIPTION
+++

EOF
}

function write_post() {
    cat <<EOF >> $POSTFILE
$POSTCONTENT
EOF
}

echo -n "Enter the keywords to generate or extend the post with: "
# Read input text from the user
read input_text

# Create a new posts based on the first parameter
hugo new content $POST

# Read the created post
read_post

# Write header
write_post_header

# Pipe the input text to ollama run command and append it to blog post
ollama run $MODELNAME <<EOF >> $POSTFILE
You are a program either creating or extending a blog post based on user input.
You reply with the Markdown formatted blog post.
Output just the extended or created blog post, no extraneous text.

The blog post currently has the following content:
"$POSTCONTENT".

Now modify the blog post or create a new one based on the following input:
"$input_text".

Include everything that was in the post before, if it isn't a new post.
EOF

read_post

# Generate description
POSTDESCRIPTION=$(ollama run $MODELNAME <<EOF
In first person, write a summary, as short as possible, about this blog post:
"$POSTCONTENT"

Output the summary in this format, just one line:

summary = "[summary in here]"

EOF
)

write_post_header
write_post