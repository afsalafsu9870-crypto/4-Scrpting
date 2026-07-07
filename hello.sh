#!/bin/bash

if [ $# -eq 0 ]; then
    echo "Usage: ./hello.sh <name>"
    exit 1
fi

echo "Hello $1, right now the time is $(date)"
