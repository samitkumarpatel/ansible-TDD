# Follow below step to start with this project
````
ansible-galaxy init systemd
mkvirtual env <<name>>
pip install molecule ansible docker-py
pip freeze > requirement.txt
molecule init scenario -r systemd
molecule test
````
