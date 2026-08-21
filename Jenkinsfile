pipeline {
    agent any

    stages {

        stage('Checkout') {
            steps {
                checkout scm
            }
        }

        stage('Test') {
            steps {
                sh 'python --version'
                sh 'pip --version'
            }
        }

        stage('Docker Build') {
            steps {
                sh 'docker build -t v_mart-devops-app:v1 .'
            }
        }
    }
}