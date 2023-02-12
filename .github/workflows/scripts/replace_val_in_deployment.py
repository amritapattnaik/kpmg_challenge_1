import os
import sys
import yaml


GITHUB_WORKSPACE = os.environ['GITHUB_WORKSPACE']
POSTGRES_DB = os.environ['POSTGRES_DB']
DB_USERNAME = os.environ['DB_USERNAME']
DB_PASSWORD = os.environ['DB_PASSWORD']
POSTGRES_HOST = os.environ['POSTGRES_HOST']
DATABASE_URL = os.environ['DATABASE_URL']


#file_deployment = "/home/yyadav/atos/craft-tool-k8s-deployment/manifests/base/deployment.yaml"
file_deployment = GITHUB_WORKSPACE + "/manifests/base/deployment.yaml"

print("file_deployment", file_deployment)

with open(file_deployment, 'r') as file:
    try:
        loaded_kustomize = yaml.safe_load(file)
        for index in loaded_kustomize['spec']['template']['spec']['containers']:
            envs = index['env']         
            
    except yaml.YAMLError as exc:
        print(exc)
for var in index['env']:

    if var['value'] == "POSTGRES_DB":
       var['value'] = POSTGRES_DB
        
    if var['value'] == "DB_USERNAME":
       var['value'] = DB_USERNAME

    if var['value'] == "DB_PASSWORD":
       var['value'] = DB_PASSWORD

    if var['value'] == "DATABASE_URL":
       var['value'] = DATABASE_URL
    

with open(file_deployment, 'w') as f:
    loaded_kustomize = yaml.dump(loaded_kustomize, stream=f,
                       default_flow_style=False, sort_keys=False)

with open(file_deployment) as f:
    loaded_kustomize = yaml.load(f, Loader=yaml.FullLoader)
    for index in loaded_kustomize['spec']['template']['spec']['containers']:
            print(index['env'])