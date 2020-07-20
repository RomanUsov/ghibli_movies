# ghibli_movies

## Docker install

### Mac

<https://docs.docker.com/docker-for-mac/install/#what-to-know-before-you-install>

### Windows

<https://docs.docker.com/docker-for-windows/install/>

### Linux

Docker:

`wget -qO- https://get.docker.com/ | sh`

docker-compose:

```Download docker-compose
curl -L https://github.com/docker/compose/releases/download/1.25.1/docker-compose-`uname -s`-`uname -m` -o /usr/local/bin/docker-compose

chmod +x /usr/local/bin/docker-compose
```

( it is the latest version for now <https://github.com/docker/compose/releases> )

## Run server

`docker-compose up`

## Run tests

`docker-compose exec server-flask pytest`

