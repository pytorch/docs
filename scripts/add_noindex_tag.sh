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

# Define the meta tag to insert
META_TAG='  <meta name="robots" content="noindex">'

# Exclude '_modules' directory and add noindex tag after <head>
# Using substitute command for cross-platform compatibility (macOS + Linux)
if [[ "$OSTYPE" == "darwin"* ]]; then
  # macOS (BSD sed): requires -i '' and different newline handling
  find "$1" -name "*.html" ! -path "*/_modules/*" -exec sed -i '' "s|<head>|<head>\\
$META_TAG|" {} \;
else
  # Linux (GNU sed)
  find "$1" -name "*.html" ! -path "*/_modules/*" -exec sed -i "s|<head>|<head>\n$META_TAG|" {} \;
fi
