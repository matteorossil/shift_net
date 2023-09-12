#!/bin/bash

#SBATCH --nodes=1
#SBATCH --ntasks-per-node=1
#SBATCH --cpus-per-task=20
#SBATCH --time=0:10:00
#SBATCH --mem=50GB
#SBATCH --gres=gpu:1
#SBATCH --job-name=test_deblur2_saycam
#SBATCH --output=/scratch/mr6744/pytorch/outputs_slurm/%j.out

module purge

singularity exec --nv \
	    --overlay /scratch/mr6744/pytorch/overlay-25GB-500K.ext3:ro \
	    /scratch/work/public/singularity/cuda11.6.124-cudnn8.4.0.27-devel-ubuntu20.04.4.sif \
	    /bin/bash -c "source /ext3/env.sh; python -u /scratch/mr6744/pytorch/Shift-Net/inference/test_deblur.py \
		--default_data SAYCAM --save_image --start_videos 399 --end_videos 400"