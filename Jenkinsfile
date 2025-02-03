pipeline {
    agent any
    stages {
        stage('Docker Build') {
            steps {
                sh 'docker compose build --no-cache'
            }
        }
        stage('Docker compose') {
            steps {
                echo 'Deploy ok'
            }
        }
        stage('Undeploy') {
            steps {
                sh 'docker compose down'
            }
        }
    }
}