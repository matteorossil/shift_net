#!/bin/bash

#SBATCH --nodes=1
#SBATCH --ntasks-per-node=1
#SBATCH --cpus-per-task=8
#SBATCH --time=10:00:00
#SBATCH --mem=20GB
#SBATCH --job-name=crop_imgs
#SBATCH --output=/scratch/mr6744/pytorch/outputs_slurm/%j.out

module purge

singularity exec --nv \
	    --overlay /scratch/mr6744/pytorch/overlay-25GB-500K.ext3:ro \
	    /scratch/work/public/singularity/cuda11.6.124-cudnn8.4.0.27-devel-ubuntu20.04.4.sif \
	    /bin/bash -c "source /ext3/env.sh; python -u /scratch/mr6744/pytorch/Shift-Net/crop_imgs.py \
		--data /vast/mr6744/SAYCAM_large_deblur/ --save-dir /vast/mr6744/SAYCAM_deblur_new"