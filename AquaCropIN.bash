#!/bin/bash

for i in 21205420;
do
   cat Base.ETo ${i}_ETo.csv > ${i}.ETo
   cat Base.PLU ${i}_PTc.csv > ${i}.PLU
   cat Base.TMP ${i}_TT.csv > ${i}.TMP
done
