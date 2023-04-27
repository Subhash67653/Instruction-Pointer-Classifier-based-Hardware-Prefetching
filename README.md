# Instruction-Pointer-Classifier-based-Hardware-Prefetching

This project is done as part of course cs230 instructed by [Prof. Biswa]
we attempted to categorically evaluate the existing prefetchers in champsim and added some enhancements
to this paper https://dpc3.compas.cs.stonybrook.edu/pdfs/Bouquet.pdf 

Code for all prefetchers are in /prefetcher folder

The simulation results for all the prefetchers are in /resulst_30M folder

We have added code and its result for each enhancement we implemented in ENHANCEMENTS_GRAPHS for graph traces and ENHANCEMENTS_SPEC for spec traces

We have generated plots using python files in /scripts folder

### Group Members 

| __Name__ |  __Roll__ |

| Subhash |  210050046 |

|Preetham | 210050108  |

|Rahul Deepak| 210050090|



## Brief Build Instructions
* Install `champsim` repository
``` bash
 > cd scripts
 > ./install-champsim.sh
```

### Install traces from below links

https://utexas.app.box.com/s/2k54kp8zvrqdfaa8cdhfquvcxwh7yn85/folder/132804598561

https://dpc3.compas.cs.stonybrook.edu/champsim-traces/speccpu/

https://www.dropbox.com/sh/xs2t9y4cuqlgrlp/AACpzGOj6BcSB-BUolGaBjbta?dl=0

### Running  for each enhancement

For graph traces go to /ENHANCEMENTS_GRAPHS/(select one folder)/code/ 

or

For spec traces go to /ENHANCEMENTS_SPEC/(select one folder)/code/

run ./build_champsim.sh [branch_pred] [l1i_pref] [l1d_pref] [l2c_pref] [llc_pref] [llc_repl] [num_core]

run ./run_champsim.sh [BINARY] [N_WARM] [N_SIM] [TRACE] [OPTION]
