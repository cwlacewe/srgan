home_dir="$HOME"

# Runs docker image and attaching parent directory
sudo nvidia-docker run $DOCKER_PROXY_RUN_ARGS \
-v $home_dir:$home_dir \
-p 8890:8888 \
-p 6061:6006 \
--shm-size 35G \
-it srgan:gpu \
bash

