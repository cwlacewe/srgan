# Builds docker image
sudo nvidia-docker build $DOCKER_PROXY_BUILD_ARGS \
    -t srgan:cpu \
    -f Dockerfile_cpu .
