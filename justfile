

# Installs requirements and uploads code to the robot and executes it immediately
[working-directory: './packages/robot']
deploy:
    robotpy deploy

# Similar to the deploy command but skips tests
[working-directory: './packages/robot']
deploy-unsafe:
    robotpy deploy --skip-tests
    