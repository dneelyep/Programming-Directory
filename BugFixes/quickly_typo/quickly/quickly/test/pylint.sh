#!/bin/sh

if ! which pylint >/dev/null; then echo 'Please install pylint'; fi

(pylint -E --output-format=parseable --include-ids=y --ignored-classes=Credentials,Launchpad $(find "$ORIGINAL_DIR" -name '*.py' | grep -v "^$ORIGINAL_DIR/debian" | grep -v "^$ORIGINAL_DIR/build") 2>/dev/null)
