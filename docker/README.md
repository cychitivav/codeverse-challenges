# Docker course
This is ...

<div align="center">
    <img src="https://user-images.githubusercontent.com/30636259/198832914-75556dc1-287d-4eaa-809f-e6e626c2ac8b.png" width="700">
</div>

## Why Docker?
### Problems when building:
* Development dependencies (packages)
* Runtime versions
* Equivalence of development environments (code sharing)
* Equivalence of production environments(go to production)
* Versions / compatibility(integration of other services e.g.: databases)

### Problems when distributing:
* Different build generations
* Access to production servers
* Native vs. distributed execution
* Serverless

### Problems when executing:
* Application dependencies
* Operating System Compatibility
* Availability of external services
* Hardware Resources

### Docker allows:
Build, distribute and run your code anywhere without worrying.

<div align="center">
    <img src="https://user-images.githubusercontent.com/30636259/198833177-49869123-5771-466e-ae2f-06f841cd6b4b.png" width="500">
</div>

## Installation
In order to install Docker in Ubuntu (you also can use [Play with Docker platform](https://labs.play-with-docker.com/)), you must add the Docker repository to the system and then install the Docker Engine and CLI. To do this, follow the steps below:

```bash
sudo apt-get install docker-ce docker-ce-cli containerd.io docker-compose-plugin
```
Finally to view the details of the installation, run the following commands:

```bash
docker version
docker info
```


## Docker architecture

<div align="center">
    <img src="https://user-images.githubusercontent.com/30636259/198833654-dc1c5d8b-c8e6-4141-8f0b-c471a84a488b.png" width="500">
</div>

Components INSIDE the Docker circle:

* __Docker daemon__: It is the center of docker, the heart that thanks to it, we can communicate with docker services.
* __REST API__: Like any other API, it is the one that allows us to visualize docker in a "graphical" way.
* __Docker Client__: Thanks to this component, we can communicate with the heart of Docker (Docker Daemon) which by default is the command line.

Within the Docker architecture we find:

* __Containers__: It is the reason for the Docker creation, it is where we can encapsulate our images to take them to another computer, server, etc. It's like a lightweight virtual machine.

* __Images__: They are the encapsulations of x container. We can run our Java application through an image, we can use Ubuntu to run our project, etc.
* __Data volumes__: We can securely access the file system of our machine.

* __Networks__: These are the ones that allow communication between containers or external devices.


## Docker commands

### Containers

| __Command__ | __Description__ |
| :---------- | :-------------- |
| `docker run <image> <command>` | Run a container from an image. |
| ^^ | With the flag `--name <name>` we can name the container. |
| ^^ | The flag `-d` allows us to run the container in the background (*detach mode*) |
| ^^ | In order to run the container in the foreground, we must use the flag `-it` |
| ^^ | The flag `-p <hostPort>:<containerPort>` allows us to map the container port to the host port. This way we can access the container from the outside. |
| ^^ | The flag `-v <hostPath>:/<containerPath>` allows us to map the container path to the host path. This way we can access the container from the outside. |
| ^^ | The flag `-e <key>=<value>` allows us to set environment variables. |
| `docker stop <containerID/name>` | Stop one or more running containers. |
| `docker start <containerID/name>` | Start one or more stopped containers. |
| `docker ps` | Lists all the running containers. |
| ^^ | The flag `-a` list all containers. |
| `docker inspect <containerID>` | Display detailed information on one or more containers. |
| ^^ | With the flag format `-f '<string>'` we can filter the information. |
|`docker rename <currentName> <newName>` | Rename a container. |
| `docker rm <containerID/name>` | Remove one or more containers. |
| `docker container prune` | Remove all stopped containers. |
| `docker exec -it <containerID/name> <command>` | Run a command in a running container and in the integrated terminal. |
| `docker logs <containerID/name>` | Fetch the logs of a container. |
| ^^ | With the flag `-n <number>` you can see the last *\<number\>* lines in the container log. |
| ^^ | With the flag `-f` you can follow the log output until press <kbd>Ctrl</kbd>+<kbd>c</kbd> or stop the process. |

### Volumes
<div align="center">
    <img src="https://user-images.githubusercontent.com/30636259/198846381-c32fd987-bdb5-4972-9cb7-78622a224dd7.png" width="500">
</div>

| __Command__ | __Description__ |
| :---------- | :-------------- |
| `docker volume ls` | List all volumes. |
| `docker volume create <name>` | Create a volume. | 
| `docker volume rm <volume>` | Remove one or more volumes. |       
| `docker run --mount src=<volumen>,dst=<containerPath> <image>` | Run a container with a volume mounted in the container path. | 
| `docker cp <file> <containerID>:<containerPath>` | Copy a file from the host to the container. |
| `docker cp <containerID>:<containerFile> <hostPath>` | Copy a file from the container to the host. |
