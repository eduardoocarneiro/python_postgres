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
                sshCommand remote: 'ssh', command: 'docker compose up -d', failOnError: true
            }
        }
        stage('Undeploy') {
            steps {
                echo 'Undeploying...'
                // sh 'docker compose down'
            }
        }
    }
}