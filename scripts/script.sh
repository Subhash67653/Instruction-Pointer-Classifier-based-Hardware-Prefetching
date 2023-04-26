#!/bin/bash

path_to_traces="champsim/traces"
path_to_results="champsim/ChampSim/results_30M"
binary="bimodal-no-ipcp-ipcpnl-ipcp-lru-1core"

for file in "$path_to_traces"/*
do
  cd champsim/ChampSim/
  file="${file#$path_to_traces/}"
  echo "$file"
./run_champsim.sh $binary 30 30 $file 
  #mv champsim/Champsim/results_30M/
  cd ..
  cd .. 
done
