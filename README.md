# Simulator for Numerical Spiking Neural P Systems (NSNP Systems)

Generates Computation graphs of input NSNP systems that solve the Subset Sum problem(SSP).


## Test Data
Assign Test data parameters in const.py

Generate test data by:
```sh
python test_gen_pos.py 
```
For positive instances of SSP and 

```sh
python test_gen_neg.py 
```
for negative instances of SSP

## Simulation
Results of the simulation will be in ./test_data/configuration graphs by running:

```sh
python nsnpsTest.py 
```
Statistics of memory use and runtime can be seen by running:
```sh
python test_show_results.py 
```
which processes the ./test_data/statistics.txt file to summarize results in terminal
