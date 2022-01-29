# docker build . --file Dockerfile --tag stgobain-casestudy:latest # This one is to be used to build the container

# This one runs the container, launching a Jupiter Notebook hub at /
sudo service docker start
docker run -v $PWD:/Work -p 8888:8888 -it stgobain-casestudy
