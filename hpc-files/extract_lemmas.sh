#!/bin/bash


#SBATCH --partition main
#SBATCH --nodes 2
#SBATCH --ntasks 8
#SBATCH --cpus-per-task 2
#SBATCH --ntasks-per-node 4
#SBATCH --time 8-00:00:00
#SBATCH --mem 40000

srun --multi-prog extract_lemmas.config
