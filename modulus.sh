#!/bin/bash

for i in `seq 1 10000`
do
  openssl rsa -modulus -pubin -in "keys/rsa-4096-$i.pub" -text -noout -out "keys/rsa-4096-$i.pub.modulus"
  openssl rsa -modulus -in "keys/rsa-4096-$i.pem" -text -noout -out "keys/rsa-4096-$i.pem.modulus"
  echo $i
done
