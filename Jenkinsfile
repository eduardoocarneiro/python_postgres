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
                sh 'docker compose up -d'
            }
        }
        stage('Deploy') {
            steps {
                echo 'Deploying....'
            }
        }
    }
}