#!/bin/sh

set -e

if [ "$1" = 'reciever' ]; then
  python -u reciever.py
elif [ "$1" = 'sender' ]; then
  python -u sender.py $2
else
  echo "Use 'reciever' or 'sender <n>'"
fi
