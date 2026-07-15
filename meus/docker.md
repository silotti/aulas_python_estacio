docker images
>mostra imagens no docker local

docker run hello-word
>se não tiver o local traz do docker-hub

docker run debian date
>roda o debian e traz a data

docker run -it debian /bin/bash
>abre terminal deban
    pwd >> mostra pasta atual no debian
    ls -l >> lista arquivos debian
    top >> mostra todos os processos dentro do debian
    exit >> sai do terminal debian

ctrl + p + q
>sai do container

docker run -d debian sleep infinity
>mantem rodando o debian

docker run -d -it debian bash
>roda o terminal do container

docker run -d --name web -p 8080:80 nginx
>roda o nginx na porta 8080:80 como o nome web

docker run -it ubuntu
>permite ficar dentro do container

docker run -d ubuntu
>executar o container e sai p/ o docker

docker container attch ba...
>parecido com -it, permanece dentro

docker exec ba... date
>entra no container e executa a data

docker exec -it <id_do_container> bash
>entra no container

docker stop -it ba... bash
>para o container

docker stop web
>para o web que é o nginx

docker start web
>inicia o web que é o nginx

docker container start ba...
>inicia o container

docker ps
>mostra o que tem iniciado

docker container ls
>lista os containers

docker container ls -a
>lista os containers em uso

docker stats
>mostra o uso dos recursos em tempo real

docker logs ba...
>mostra os logs

docker pause ba...
>pausa o container

docker unpause ba...
>despausa o container

clear
>limpa tela

history
>mostra o histórico de comandos docker
