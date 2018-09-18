## Super Resolution Examples


We run this script under [TensorFlow](https://www.tensorflow.org) 1.7.0-gpu-py3 and the [TensorLayer](https://github.com/tensorlayer/tensorlayer) 1.8.0+.
A docker is available in the docker directory.  The Dockerfile assumes the use of environmental variables $DOCKER_PROXY_RUN_ARGS and $DOCKER_PROXY_BUILD_ARGS defined as:
```
ENV DOCKER_PROXY_RUN_ARGS="\
    --env HTTPS_PROXY=$HTTPS_PROXY \
    --env https_proxy=$https_proxy \
    --env HTTP_PROXY=$HTTP_PROXY \
    --env http_proxy=$http_proxy \
    --env NO_PROXY=$NO_PROXY \
    --env no_proxy=$no_proxy \
    --dns <dns ip>"

ENV DOCKER_PROXY_BUILD_ARGS="\
    --build-arg HTTPS_PROXY=$HTTPS_PROXY \
    --build-arg https_proxy=$https_proxy \
    --build-arg HTTP_PROXY=$HTTP_PROXY \
    --build-arg http_proxy=$http_proxy \
    --build-arg NO_PROXY=$NO_PROXY \
    --build-arg no_proxy=$no_proxy"
```

This minimizes the command to:
```

sudo nvidia-docker build $DOCKER_PROXY_BUILD_ARGS -t srgan:gpu -f Dockerfile_gpu .

```
or use:
```
./build_docker_gpu.sh
```


# Run
Use the following to run the docker:
```
./run_docker_gpu.sh
```

### Docker example run
The docker allows access to your $HOME directory to allow saving to your system.  Please keep this in mind but you can change the binding in run_docker_gpu.sh.

The following example upscales myImages/test_SRGAN_img_108x192.png from /path/to/this/repo.  The myImages directory is used for the test method.  You can also use resize_save_test_img.py to resize images for test cases.
 
```
python3 main.py --mode=test --test_file=test_SRGAN_img_108x192.png
```

### SRGAN Architecture

TensorFlow Implementation of ["Photo-Realistic Single Image Super-Resolution Using a Generative Adversarial Network"](https://arxiv.org/abs/1609.04802)

<a href="http://tensorlayer.readthedocs.io">
<div align="center">
	<img src="img/model.jpeg" width="80%" height="10%"/>
</div>
</a>


### Results

<a href="http://tensorlayer.readthedocs.io">
<div align="center">
	<img src="img/SRGAN_Result2.png" width="80%" height="50%"/>
</div>
</a>

<a href="http://tensorlayer.readthedocs.io">
<div align="center">
	<img src="img/SRGAN_Result3.png" width="80%" height="50%"/>
</div>
</a>

### Prepare Data and Pre-trained VGG

- 1. You need to download the pretrained VGG19 model in [here](https://mega.nz/#!xZ8glS6J!MAnE91ND_WyfZ_8mvkuSa2YcA7q-1ehfSm-Q1fxOvvs) as [tutorial_vgg19.py](https://github.com/zsdonghao/tensorlayer/blob/master/example/tutorial_vgg19.py) show.
- 2. You need to have the high resolution images for training.
  -  In this experiment, I used images from [DIV2K - bicubic downscaling x4 competition](http://www.vision.ee.ethz.ch/ntire17/), so the hyper-paremeters in `config.py` (like number of epochs) are seleted basic on that dataset, if you change a larger dataset you can reduce the number of epochs. 
  -  If you dont want to use DIV2K dataset, you can also use [Yahoo MirFlickr25k](http://press.liacs.nl/mirflickr/mirdownload.html), just simply download it using `train_hr_imgs = tl.files.load_flickr25k_dataset(tag=None)` in `main.py`. 
  -  If you want to use your own images, you can set the path to your image folder via `config.TRAIN.hr_img_path` in `config.py`.



### Run
- Set your image folder in `config.py`, if you download [DIV2K - bicubic downscaling x4 competition](http://www.vision.ee.ethz.ch/ntire17/) dataset, you don't need to change it. 
- Other links for DIV2K, in case you can't find it : [test\_LR\_bicubic_X4](https://data.vision.ee.ethz.ch/cvl/DIV2K/validation_release/DIV2K_test_LR_bicubic_X4.zip), [train_HR](https://data.vision.ee.ethz.ch/cvl/DIV2K/DIV2K_train_HR.zip), [train\_LR\_bicubic_X4](https://data.vision.ee.ethz.ch/cvl/DIV2K/DIV2K_train_LR_bicubic_X4.zip), [valid_HR](https://data.vision.ee.ethz.ch/cvl/DIV2K/validation_release/DIV2K_valid_HR.zip), [valid\_LR\_bicubic_X4](https://data.vision.ee.ethz.ch/cvl/DIV2K/DIV2K_valid_LR_bicubic_X4.zip).

```python
config.TRAIN.img_path = "your_image_folder/"
```

- Start training.

```bash
python main.py
```

- Start evaluation. ([pretrained model](https://github.com/tensorlayer/srgan/releases/tag/1.2.0) for DIV2K)

```bash
python main.py --mode=evaluate 
```

- Test a single image.

```bash
python main.py --mode=test --test_file=test_SRGAN_img_540x960.png
```


### Reference
* [1] [Photo-Realistic Single Image Super-Resolution Using a Generative Adversarial Network](https://arxiv.org/abs/1609.04802)
* [2] [Is the deconvolution layer the same as a convolutional layer ?](https://arxiv.org/abs/1609.07009)

### Author
- [zsdonghao](https://github.com/zsdonghao)

### License

- For academic and non-commercial use only.
- For commercial use, please contact tensorlayer@gmail.com.
