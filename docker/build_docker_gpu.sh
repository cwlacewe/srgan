# Builds docker image
sudo nvidia-docker build $DOCKER_PROXY_BUILD_ARGS \
    -t srgan:gpu \
    -f Dockerfile_gpu .
