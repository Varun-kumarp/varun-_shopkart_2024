pipeline {
    agent any

    environment {
        IMAGE_NAME = 'v_mart-devops-app'
    }

    stages {

        stage('Checkout') {
            steps {
                checkout scm
            }
        }

        stage('Test') {
            steps {
                sh 'python3 --version'
                sh 'pip --version'
                sh 'pip install -r requirements.txt'
                sh 'python3 manage.py test'
            }
        }

        stage('Docker Build') {
            steps {
                sh "docker build -t ${IMAGE_NAME}:v${BUILD_NUMBER} ."
            }
        }
    }
}