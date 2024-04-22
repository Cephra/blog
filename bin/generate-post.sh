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
You are a robot that either creates or extends blog posts based on user input.
You reply in Markdown.
Output just the extended or created blog post.
Avoid any extraneous text.

The blog post has this content, if any:
"""
$POSTCONTENT
""".

Modify the blog post or create a new one based on these instructions, if any:
"""
$input_text
""".

Include everything that was in the post before, if it isn't a new post.
EOF

read_post

# Generate description
POSTDESCRIPTION=$(ollama run $MODELNAME <<EOF
You are a robot creating summaries for blog posts.
You reply as the author, summarizing a blog post.
Output the summary in this format:
summary = "[summary in here]"
Just one line. No extraneous text.

The blog post has this content, if any:
"""
$POSTCONTENT
""".
EOF
)

write_post_header
write_post