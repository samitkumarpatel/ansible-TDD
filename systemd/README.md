# Follow below step to start with this project
````
ansible-galaxy init systemd
mkvirtual env <<name>>
pip install molecule ansible docker-py
pip freeze > requirement.txt
molecule init scenario -r systemd
````
* implement your role
* for testing use below command
````
molecule test --destroy never

docker ps - from this command you can get the docker container id or name(copy that for debug purpose)
docker exec -it <<containerid or name>> bash
````
* check your expected systemd has been created and working or not
* please note that there will be a molecule test to ensure the things we did was working expected or not
