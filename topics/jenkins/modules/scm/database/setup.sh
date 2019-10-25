#! /usr/bin/env bash
# setup a mysql db in a docker container
curl https://get.docker.com | sudo bash

create_container() {
    sudo docker run -d \
        --name mysql \
        -p 3306:3306 \
        -e MYSQL_DATABASE="bookshelve" \
        -e MYSQL_ROOT_PASSWORD="${MYSQL_ROOT_PASSWORD}" \
        -e MYSQL_USER="bookshelve-api" \
        -e MYSQL_PASSWORD="${MYSQL_PASSWORD}" \
        mysql:5.7
}

run_sql_scripts() {
    docker exec -i mysql mysql bookshelve \
        -ubookshelve-api \
        -p${MYSQL_PASSWORD} < setup.sql 
}

# if the container doesn't exist
if [ -z "$(docker ps -q -f name=mysql)"]; then
    create_container
# if the container is stopped
elif [ -n "$(docker ps -q -f status=stopped name=mysql)"]; then
    docker start mysql
    run_sql_scripts
# the container must be running, so just execute the scripts
else
    run_sql_scripts
fi
