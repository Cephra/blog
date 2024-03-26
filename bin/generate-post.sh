#!/usr/bin/env bash

# change working dir
cd $(dirname $0)/..

POST=posts/$1.md
POSTFILE=content/$POST

# Read post
function read_post()  {
    POSTHEADER=$(pcregrep -M '^\+\+\+$(\n|.)*^\+\+\+$' $POSTFILE)
    POSTHEADER_STRIPPED=$(echo "$POSTHEADER" | sed '1d;$d')
    POSTHEADER_LINES=$(echo $(echo "$POSTHEADER" | wc -l)+1 | bc)
    POSTCONTENT=$(cat "$POSTFILE" | tail -n +$POSTHEADER_LINES)
}

# Read input text from the user
read input_text

# Create a new posts based on the first parameter
hugo new content $POST

read_post

# Pipe the input text to ollama run gemma command and append it to blog post
ollama run gemma <<EOF >> $POSTFILE
Either create or extend a blog post based on input.
The blog post currently has the following content:
"$POSTCONTENT"
Continue the blog post based on the following input:
"$input_text"
Include everything that was in the post before.
EOF

read_post

# Generate description
POSTDESCRIPTION=$(ollama run gemma <<EOF
In first person, write a summary, as short as possible, about this blog post:
"$POSTCONTENT"
Output the summary like this:
summary = "[summary sentences here]"
EOF
)

# Reassemble the post
cat <<EOF > $POSTFILE
+++
$POSTHEADER_STRIPPED
$POSTDESCRIPTION
+++
$POSTCONTENT
EOF