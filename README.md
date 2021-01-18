# yamdb_final
yamdb_final - это мини блог для написание постов
* Вы можете создавать посты
  * Коментировать посты
* Делать подписки на авторов
* Создавать группы

### Требования

[Python](https://www.python.org/downloads/) v3.7 +  для запуска.
[Docker](https://www.docker.com/)
Установите зависимости.

```sh
$ sudo apt update
$ sudo apt install apt-transport-https ca-certificates curl gnupg-agent software-properties-common -y
$ curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo apt-key add -
$ sudo add-apt-repository \
$ "deb [arch=amd64] https://download.docker.com/linux/ubuntu \
$ (lsb_release -cs) \
$ stable"
$ sudo apt update
$ sudo apt install docker-ce -y
```

После установки docker выполнить команду в командной строке:
```sh
$ docker-compose up
```

После сборки образа:
```sh
$ sudo docker exec -it <CONTAINER ID> python manage.py collectstatic --no-input
$ sudo docker exec -it <CONTAINER ID> python manage.py makemigrations
$ sudo docker exec -it <CONTAINER ID> python manage.py migrate
$ sudo docker exec -it <CONTAINER ID> python manage.py createsuperuser
$ sudo docker exec -it <CONTAINER ID> python manage.py loaddata fixtures.json
```

https://github.com/RustamIR/yamdb_final/workflows/yamdb_final/badge.svg