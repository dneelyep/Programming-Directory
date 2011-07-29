#!/bin/sh

## This test just checks that project_root/bin/project_name is lean and mean.  Don't overwhelm the user with boilerplate.

## Arbitrarily choose 75 lines as the cutoff

test $(wc -l "$TEST_SCRIPT_DIR/../project_root/bin/project_name" | cut -d' ' -f1) -le 75 && echo Success
# Success
