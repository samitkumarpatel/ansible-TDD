#!/bin/bash
x=1
while true
do
  echo "Welcome $x times" > /poc/poc.log
  x=$(( $x + 1 ))
done