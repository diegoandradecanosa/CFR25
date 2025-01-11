#/bin/sh
srun --gres=gpu:1 --time=00:59:00 --mem=64G -c 32 --pty bash
