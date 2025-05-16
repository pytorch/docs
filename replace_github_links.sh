#!/bin/bash
# Replaces GitHub links from v2.7.1 to v2.7.0 in all html files in a directory
#
# Usage:
# ./replace_github_links.sh directory
#
# Example (from the root directory)
# ./replace_github_links.sh 2.7

if [ "$1" == "" ]; then
  echo "Incorrect usage. Correct Usage: replace_github_links.sh <directory>"
  exit 1
fi

find $1 -name "*.html" -print0 | xargs -0 sed -i 's|github.com/pytorch/pytorch/blob/v2.7.1|github.com/pytorch/pytorch/blob/v2.7.0|g'

echo "Replaced v2.7.1 with v2.7.0 in GitHub links in $1 directory"

