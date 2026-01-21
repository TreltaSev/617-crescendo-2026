

# Installs requirements and uploads code to the robot and executes it immediately
[working-directory: './packages/robot']
deploy:
    robotpy deploy

# Similar to the deploy command but skips tests
[working-directory: './packages/robot']
deploy-unsafe:
    robotpy deploy --skip-tests


# Initializes the project
[working-directory: './']
init:
    cd ./packages/robot && \
    python -m venv venv

    cd ./packages/robot && \
    ./venv/bin/pip3 install -r ./requirements.txt

    echo "Project Initialized"    