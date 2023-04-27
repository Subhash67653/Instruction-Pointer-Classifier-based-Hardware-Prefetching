# Instruction-Pointer-Classifier-based-Hardware-Prefetching
prefetchers play an important role in hiding long data access latency

This project is done as part of course cs230 instructed by [Prof. Biswa]
we attempted to categorically evaluate the existing prefetchers in champsim and added some enhancements
to this paper https://dpc3.compas.cs.stonybrook.edu/pdfs/Bouquet.pdf 

Code for all prefetchers are in /prefetchers folder
The simulation results for all the prefetchers are in /resulst_30M folder

### Group Members 

| __Name__ |  __Roll__ |
|-------------|------------|------------|
| Subhash |  210050046 |
|Preetham | 210050108  |
|Rahul Deepak| 210050090|



## Brief Build Instructions
* Install `champsim` repository
``` bash
 > cd scripts
 > ./install-champsim.sh
```

* Install traces from below links 
https://utexas.app.box.com/s/2k54kp8zvrqdfaa8cdhfquvcxwh7yn85/folder/132804598561
https://dpc3.compas.cs.stonybrook.edu/champsim-traces/speccpu/
https://www.dropbox.com/sh/xs2t9y4cuqlgrlp/AACpzGOj6BcSB-BUolGaBjbta?dl=0

For ruuning code for each enhancement 
go to /Enhancements/(select one folder)/code/
run ./build_champsim.sh [branch_pred] [l1i_pref] [l1d_pref] [l2c_pref] [llc_pref] [llc_repl] [num_core]
run ./run_champsim.sh [BINARY] [N_WARM] [N_SIM] [TRACE] [OPTION]
