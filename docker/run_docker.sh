#! /bin/bash
docker build -t {{package}} .
docker stop {{package}}
docker rm {{package}}
docker run -v $(pwd):/{{package}} --name {[package}} -dt {{package}} bash
docker exec -it {{package}} bash
