# ECommerce

ECommerce app for GAU django final project.


## Local setup
NOTE: project is setup for python 3.9 so It should work fine for 3.9+ versions. If you have any issues with the setup, consider updating your python version.
```sh
# clone the repo
git clone https://github.com/Cine-Pixel/django-ecommerce.git

# create virtual environment with venv or your preffered tool and activate
python -m venv venv
source venv/bin/activate # for linux and mac

# install requirements
pip install .

# apply migrations
cd ecommerce
python manage.py migrate

# run server
python manage.py runserver

# to run tailwind frontend
python manage.py tailwind install
python manage.py tailwind start
```

## Workflow

Tasks can be found on projects page of the repo. You can tackle any task you want or add new ones. 
Once you choose what you wanna work on, follow the instructions below:

- **STEP 0**. Make sure you have project setup on your local machine.
- **STEP 1**. Update you local main branch: 
    ```sh
    # make sure you are on the main branch with
    git checkout main
    # update it
    git pull main
    ```
- **STEP 2**. Create new a branch:
    ```sh
    git checkout -b <your-branch-name>
    ```
- **STEP 3**. Implement the task on your new branch. Make sure to commit often so that you can rollback if something goes wrong and try to make descriptive commit messages. You can also follow the [Conventional Commits](https://www.conventionalcommits.org/en/v1.0.0/) guidlines (totally optional).
- **STEP 4**. Once you are done with the task and commited your code, push it to GitHub:
    ```sh
    git push -u origin <your-branch-name>
    ```
    **NOTE: Make sure you don't push to the main branch**
- **STEP 5**. Open a pull request from GitHub UI and ask someone on telegram to review it.
- **STEP 6**. Once you get an approval from reviewer, merge your pull request with **Squash and merge** option.
