# Docker course
This is ...

<div align="center">
    <img src="https://user-images.githubusercontent.com/30636259/198832914-75556dc1-287d-4eaa-809f-e6e626c2ac8b.png" width="400">
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
    <img src="https://user-images.githubusercontent.com/30636259/198833177-49869123-5771-466e-ae2f-06f841cd6b4b.png" width="400">
</div>

## Installation
In order to install Docker in Ubuntu, you must add the Docker repository to the system and then install the Docker Engine and CLI. To do this, follow the steps below:

```bash
sudo apt-get install docker-ce docker-ce-cli containerd.io docker-compose-plugin
```
Finally to view the details of the installation, run the following commands:

```bash
docker version
docker info
```


