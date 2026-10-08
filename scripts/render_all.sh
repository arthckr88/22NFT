#!/bin/bash
# Final render batch. Runs sequentially; log in renders/batch.log
cd "$(dirname "$0")"
for s in "$@"; do
  python3 render.py "$s" >> ../renders/batch.log 2>&1 || echo "FAILED $s" >> ../renders/batch.log
done
echo ALLDONE >> ../renders/batch.log
