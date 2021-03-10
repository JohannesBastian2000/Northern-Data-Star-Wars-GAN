# Star-Wars-GAN

This notebook demonstrates how to use state-of-the-art machine learning techniques with AMD compute accelerators and Rocm for training by modifying Nvidia's styleGun2.
Please follow the following instructions

Create a persistent space
Because of the ephemeral nature of Docker containers, once a docker session is closed all the modifications and files stored, will be deleted with the container.

For this reason is useful to create a persistent space in the physical drive for storing files and Jupyter notebooks. The simpler method is to create a folder to initialize with a docker container. To do that issue the command:

```
mkdir /home/$LOGNAME/content
```

Pull the Docker image

```
docker pull northern/starwarsgan
```

Starting Docker
Now, execute the image in a new container session. Simply send the following command:

```
sudo docker run -i -t \
--network=host \
--device=/dev/kfd \
--device=/dev/dri \
--group-add video \
--cap-add=SYS_PTRACE \
--security-opt seccomp=unconfined \
--workdir=/content \
-v $HOME/content:/content northern/starwarsgan /bin/bash
```

now in the Docker container clone Repository:

```
git clone https://github.com/Northern-Data-AG/Northern-Data-Star-Wars-GAN.git
cd Northern-Data-Star-Wars-GAN
```

Start the Jupiter notebook:

```
jupyter notebook --allow-root --port=8889
```

Finally go to the Jupiter notebook and open the StarWarsGAN-3.ipyn

For any questions please email ferdinand.loesch@northerndata.de
