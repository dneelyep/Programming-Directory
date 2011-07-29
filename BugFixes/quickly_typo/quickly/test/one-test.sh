#!/bin/bash
# -*- Mode: sh; coding: utf-8; indent-tabs-mode: nil; tab-width: 4 -*-

LANG=C
PATH=$(pwd)/bin:$PATH

if [ ! -e $(pwd)/bin ]; then
    echo "You must run this script from the top level of the quickly source"
    exit 1
fi

if [ -z "$1" ]; then
    echo "You must provide a test as an argument to this script"
    exit 1
fi

exit_status() {
    if [ $1 -eq 0 ]; then
        echo -e '\e[32mPASSED\e[0m'
    else
        rm -f "$LOGFILE"
        echo -e '\e[31mFAILED\e[0m'
    fi
    exit $1
}

ORIGINAL_DIR=$(pwd)

SCRIPT=$1
CATEGORY=${2:-test}
SCRIPT_NAME=$(basename "$SCRIPT")
LOGFILE="$ORIGINAL_DIR/results.log"

rm -f "$LOGFILE"

echo -n "Running $CATEGORY $SCRIPT_NAME... "

if [ -d "$SCRIPT" ]; then
    if [ -e "$SCRIPT/$SCRIPT_NAME.py" ]; then
        SCRIPT_NAME="$SCRIPT_NAME.py"
    else
        SCRIPT_NAME="$SCRIPT_NAME.sh"
    fi
    SCRIPT="$SCRIPT/$SCRIPT_NAME"
fi

if echo "$SCRIPT_NAME" | grep "\.py$" > /dev/null; then
    # this is actually a python unit test
    python "$SCRIPT" &> "$LOGFILE"
    rv=$?
    if [ $rv -ne 0 ]; then
        echo
        cat "$LOGFILE"
    fi
    exit_status $rv
fi

TEMP_SCRIPT_DIR=$(dirname "$SCRIPT")
SCRIPT_DIR=$(cd "$TEMP_SCRIPT_DIR"; pwd)
CMD="$ORIGINAL_DIR/next-cmd.sh"
CMD_OUTPUT="$ORIGINAL_DIR/output.log"
DISPLAY="" # to avoid popup projects when creating them
export EDITOR="$(pwd)/test/editor"

head -n1 "$SCRIPT" >> "$LOGFILE"
egrep -v '(^#[^#]|^\s*$)' "$SCRIPT" | while read -r line; do
    echo >> "$LOGFILE"
    echo "$line" >> "$LOGFILE";
    if echo "$line" | grep '^##' > /dev/null; then
        continue
    fi
    echo "#!/bin/sh" > $CMD;
    echo "export TEST_SCRIPT_DIR=$SCRIPT_DIR" >> $CMD;
    # Piping this line will cause a separate subprocess to execute
    echo "$line &> \"$CMD_OUTPUT\"" >> $CMD;
    source $CMD
    cat "$CMD_OUTPUT" | awk '{print "# " $0}' >> "$LOGFILE";
done

cd "$ORIGINAL_DIR"
rm -f "$CMD"
rm -f "$CMD_OUTPUT"
if [[ -n $(diff -q "$SCRIPT" "$LOGFILE") ]]; then
    echo # The "Running BLAH BLAH... " didn't have a trailing newline
    echo "********************************"
    diff -Nu "$SCRIPT" "$LOGFILE"
    echo "********************************"
    exit_status 1
else
    exit_status 0
fi
