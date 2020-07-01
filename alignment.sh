#!/bin/bash
  
git pull
python3 alignment.py
aws s3 cp records.txt s3://generated-alignments-samp/
python3 tweet.py