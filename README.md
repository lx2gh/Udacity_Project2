[![Actions status](https://github.com/lx2gh/Udacity_Project2/workflows/Python%20application%20test%20with%20Github%20Actions/badge.svg)](https://github.com/lx2gh/Udacity_Project2/actions)

# Overview

This is a Machine Learning Microservice which features a REST-API to predict house prices. It is trained with the Boston housing prices dataset, is implemented im Python and runs on an Azure App Service.
This project makes use of Continuous Integration (CI) via Github Actions and Continious Dellivery (CD) via azure pipelines

## Project Plan

The project spreadsheet can be found under [/plan/spreadsheet.xlsx](/plan/spreadsheet.xlsx) and here is a link to the [Trello Board](https://trello.com/b/yWGD7Lut/mlmicroservice)

## Instructions

Architectural Diagram of project: 
![architecture](doc/architecture.jpg "Architecture of CI/CD")

* Get an Azure account and log into [azure portal](https://portal.azure.com)

* Open cloud shell

* Generate ssh key by using following command:

```bash
user@Azure:~$ ssh-keygen -t rsa
```

* Copy ssh key and add it to your github account 

* Clone this repo into Azure Cloud Shell. Output should look like this:
![clone](doc/Clone_2_Cloud_Shell.JPG "cloning repo")

* Set up Python virtual environment by executing: 
```bash
make setup
```
* Activate virtual environment:
```bash
source ~/.udacity-devops/bin/activate
```
* Install requirements and test project setup:
```bash
make all
```
Expected output:
![make all](doc/passing_all_tests.JPG "passing all tests")

* To conduct a test run hosted in the Azure Cloud Shell type the following commands:
```bash
export FLASK_APP=app.py
flask run
```
Expected output:<br>
![test run](doc/test_run.JPG "test run")

* Output of a test run

* Successful deploy of the project in Azure Pipelines.  [Note the official documentation should be referred to and double checked as you setup CI/CD](https://docs.microsoft.com/en-us/azure/devops/pipelines/ecosystems/python-webapp?view=azure-devops).

* Running Azure App Service from Azure Pipelines automatic deployment

* Successful prediction from deployed flask app in Azure Cloud Shell.  [Use this file as a template for the deployed prediction](https://github.com/udacity/nd082-Azure-Cloud-DevOps-Starter-Code/blob/master/C2-AgileDevelopmentwithAzure/project/starter_files/flask-sklearn/make_predict_azure_app.sh).
The output should look similar to this:

```bash
udacity@Azure:~$ ./make_predict_azure_app.sh
Port: 443
{"prediction":[20.35373177134412]}
```

* Output of streamed log files from deployed application

> 

## Enhancements

<TODO: A short description of how to improve the project in the future>

## Demo 

<TODO: Add link Screencast on YouTube>


