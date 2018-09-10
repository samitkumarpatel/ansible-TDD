# molecule test

molecule test are to test for ansible role in a virtual machie or in docker

tutorial-1 [click](https://zapier.com/engineering/ansible-molecule/)

tutorial-2 [click](https://blog.opsfactory.rocks/testing-ansible-roles-with-molecule-97ceca46736a)

tutorial-3 [click](https://www.digitalocean.com/community/tutorials/how-to-test-ansible-roles-with-molecule)

official site [molecules](https://molecule.readthedocs.io/en/latest/)

# installation
> Best practice
1. create a python virtual environment
2. Install molecules and other necessary dependency on to the virtual env
3. create a ansible role by using molecule command line or even we can add molecule init setup of an existing role - which was created from ansible galaxy
````
virtualenv --no-site-package .venv

source .venv/bin/activate

pip install molecule ansible docker-py

````
# Create a new role
````
molecule init role -r <<role_name>> -d <<driver>>

example:-
molecule init role -r foo -d docker

````
# Testing a new role
````
cd newRoleDirectory
molecule test
````

# Testing an existing role which was created from ansible galaxy or other
````
cd existingRoleDirectory
molecule init scenario -r <<scenarioName>>
````

# docker inside docker
````
docker run --rm -it -v $(pwd):/tmp/$(basename "$(pwd)") imageName:imageVersion molecule init role -r <<roleName>> -d <<driverName>>

after this command you will be inside the docker container to do further.
note that- once you exit the container will be removed and you no longer able to get back to the role you have created it.
````



