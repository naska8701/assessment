# Deploying an API server framework using FastAPI
## This application is run using python for jumble word (defined during execution), it also retun last 10 API calls and the payload given.
# Based of the assessment, questions not repeated here; steps followed are as follows;

1. Get raw/code for jumble API, test it out source of the code used, tested in VScode (in a virtual environment (.env), python interpreter was specified and all dependecies will be deployed.
    (python -m venv .env)
    subsequent activation of the virtual environment needs to be done by running .env\scripts\activate.bat 

    Source >>>>> https://docs.python.org/3/tutorial/venv.html
2. Get FastAPI framework from (https://fastapi.tiangolo.com/) and created main.py template this include the Audit of the last 10 made to it.
3. The code is just include a GET operation. The following commands were run
4. FastAPI was installed using "pip install fastapi" / "python -m pip install fastapi"
5. An ASGI server (Asynchronous Server Gateway Interface) is required and Uvicorn is recommended by FastAPI using "pip install "uvicorn[standard]"
6. Upon completion of installation the application contained in main.py can be deployed using "uvicorn main:app --reload" the flag --reload makes the application reloaded onces an update is done to it.
7. Test application with 

# Dockerization of the application

1. Create a dockerfile with all the instructions (Commands and Arguements)
2. The requirements.txt is gotten using "pip freeze > requirements. txt", this will write a list of all the installed Python packages and their versions to the file
3. Deploy the list of docker commandlets (Docker build -t "app:tag", docker push).
4. The application can be updated by accessing the main.py template, make changes to requirement.txt as required and Dockerfile if required.
5. Image can then be called form Dockerhub public repo for deployment in Minikube using Helm package manager.


# Deploying Solution to Minikube

1. Create folder for the deployment (Helm-deployment)
2. Run the command to create helm chart using "helm create api-server"
3. This will create a new directory with the same name as the chart, and generate the necessary files and directories for a new chart.
4. The values.yaml template can then adjusted with images available on dockerhub for deployment
5. Port/Services/Tags and other required configurations can then be adjusted as required.


