#!/bin/sh
# -*- Mode: sh; coding: utf-8; indent-tabs-mode: nil; tab-width: 4 -*-

if [ ! -e $(pwd)/bin ]; then
    echo "You must run this script from the top level of the quickly source"
    exit 1
fi

rv=0

run_tests() {
    testdir=$1
    category=$2
    for test in "$testdir"/*; do
        if ! test/one-test.sh "$test" "$category"; then
            rv=2
        fi
    done
}

run_tests "quickly/test" "quickly"

for template in data/templates/*; do
    if [ -d "$template/test" ]; then
        run_tests "$template/test" $(basename "$template")
    fi
done

exit $rv
