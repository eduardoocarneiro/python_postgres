# Choose documentation version:

* [English](#people-registration-app)
* [PTBR](#cadastro-de-pessoas-app)

# People Registration App
Kubernetes version of the People Registration application.

## Requirements

* Kubernetes cluster
* Helm

## Provisioned Resources
After successfully executing this guide, the following resources will be provisioned in the Kubernetes cluster:

* ```App Deployment:``` Application deployment
* ```DB Deployment:``` Database deployment
* ```pvc:``` Volume for database data storage
* ```App Service:``` Application service
* ```DB Service:``` Database service

## Installation
Clone the project:

```
https://github.com/eduardoocarneiro/python_postgres.git
cd python_postgres/
```

Install the chart. This document installs it in the ```cadastro-pessoas``` namespace. You can change this as you prefer.

```
helm install cadastro-pessoas ./helm_chart/ -n cadastro-pessoas --create-namespace
```

Run the command below to view the provisioned pods and services:

```
kubectl get pod,svc -n cadastro-pessoas

NAME                                    READY   STATUS    RESTARTS   AGE
pod/cadastro-pessoas-7585d6dc4f-vbvsj   1/1     Running   0          48s
pod/postgres-7bb585b768-m29c6           1/1     Running   0          48s

NAME                       TYPE        CLUSTER-IP       EXTERNAL-IP   PORT(S)          AGE
service/cadastro-pessoas   NodePort    10.111.219.74    <none>        8000:32656/TCP   48s
service/postgres           ClusterIP   10.107.174.179   <none>        5432/TCP         48s
```

As we can see, the ```cadastro-pessoas``` service is a ```NodePort```. This allows external access to the application on port ```30777```. If you wish, you can configure an ingress controller or Gateway API in your cluster and modify this setup to create a URL for your application.

# Cadastro de Pessoas App
Versão kubernetes da aplicação cadastro de pessoas.

## Requisitos

* Cluster kubernetes
* Helm

## Recursos provisionados
Após a execução desse manual com sucesso, os seguintes recursos serão provisionados no cluster Kubernetes:

* ```App Deployment:``` Deployment da aplicação
* ```DB Deployment:``` Deployment do banco de dados
* ```pvc:``` Volume para armazenamento dos dados do banco
* ```App Service:``` Serviço da aplicação
* ```DB Service:``` Serviço do banco de dados

## Instalação
Clone o projeto:

```
https://github.com/eduardoocarneiro/python_postgres.git
cd python_postgres/
```

Instale o chart. Esse documento instala no namespace ```cadastro-pessoas```. Isso pode ser alterado conforme sua escolha.

```
helm install cadastro-pessoas ./helm_chart/ -n cadastro-pessoas --create-namespace
```

Execute o comando abaixo para visualizar os pods e serviços provisionados:

```
kubectl get pod,svc -n cadastro-pessoas

NAME                                    READY   STATUS    RESTARTS   AGE
pod/cadastro-pessoas-7585d6dc4f-vbvsj   1/1     Running   0          48s
pod/postgres-7bb585b768-m29c6           1/1     Running   0          48s

NAME                       TYPE        CLUSTER-IP       EXTERNAL-IP   PORT(S)          AGE
service/cadastro-pessoas   NodePort    10.111.219.74    <none>        8000:32656/TCP   48s
service/postgres           ClusterIP   10.107.174.179   <none>        5432/TCP         48s
```

Como podemos observar, o serviço ```cadastro-pessoas``` é do tipo ```NodePort```. Isso possibilita o acesso externo à aplicação na porta ```30777```. Caso queira, você pode configurar um ingress controller ou gateway API no seu cluster e alterar esse código para criar uma URL para sua aplicação.
