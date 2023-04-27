#!/bin/bash
touch out.txt
path="results_30M"
path1="-bimodal-no-ipcp-ipcp-ipcp-lru-1core.txt"
str="CPU 0 cumulative IPC: "
for file in $path/* 
do
var=$(sed -n '28p' < $file) 
var=${var#$str}

file1=${file#$path/}
echo ${file1%$path1} $var >> out.txt


done
