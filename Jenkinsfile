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
                sh 'python manage.py test'
            }
        }

        stage('Docker Build') {
            steps {
                sh "docker build -t ${IMAGE_NAME}:v${BUILD_NUMBER} ."
            }
        }
    }
}