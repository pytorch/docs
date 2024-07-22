#!/bin/bash
# Adds <meta name="robots" content="noindex"> tags to all html files in a
# directory (recursively), excluding the '_modules' subdirectory because
# those files already have the noindex tag.
#
# If we need to remove the _modules limitation, need to replace the script
# below with:
#
# if [ "$1" == "" ]; then
#  echo "Incorrect usage. Correct Usage: add_no_index_tags.sh <directory>"
#  exit 1
# fi
# find $1 -name "*.html" -print0 | xargs -0 sed -i '/<head>/a \ \ <meta name="robots" content="noindex">'
#
# Usage:
# ./add_noindex_tags.sh directory
#
# Example (from the root directory)
# ./scripts/add_no_index_tags.sh 2.4
if [ "$1" == "" ]; then
  echo "Incorrect usage. Correct Usage: add_no_index_tags.sh <directory>"
  exit 1
fi
# Exclude '_modules' directory
find $1 -name "*.html" ! -path "*/_modules/*" -print0 | xargs -0 sed -i '/<head>/a \ \ <meta name="robots" content="noindex">'
