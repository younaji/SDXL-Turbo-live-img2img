# Stable Diffusion Turbo live img2img

This repository provides simple socket communication based live img2img video streaming service.

### Install 
- server dependency - huggingface diffuser 
```shell
pip install diffusers transformers accelerate --upgrade
```
- client dependency
```shell
pip install -r requirements.txt
```
### Run
Before start, please set the specific address and port for socket communication between server and client.
1. run server
```shell
python socket_server_random_seed.py
# if you want to fix generator seed(this makes performance slow)
python socket_server_fixed_seed.py
```
2. run client(should set webcam for streaming)
```shell
python socket_client.py
```

### Demo
Tested on NVIDIA L40 GPU for server
- random seed server(about 30fps)

![random_demo.gif](readme_src/random_demo.gif)
- fixed seed server(about 15fps)

![fixed_demo.gif](readme_src%2Ffixed_demo.gif)
