#!/bin/bash
mkdir -p tmp
cp ../b64.txt tmp/encoded_data_dec.txt

for i in {1..50}
do
  # variables
  # ((prev = $i - 1))
  base64 --decode tmp/encoded_data_dec.txt > tmp/encoded_data.txt
  rm -f tmp/encoded_data_dec.txt
  mv tmp/encoded_data.txt tmp/encoded_data_dec.txt
done
