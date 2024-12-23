#!/bin/bash

cd /mnt/c/Users/joshu/Documents/codeandcypher

rsync -avz -e 'ssh -i ~/.ssh/bluehost' public/ dasmhrmy@50.6.154.89:~/public_html/

