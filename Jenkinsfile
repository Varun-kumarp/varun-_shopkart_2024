pipeline {
    agent any

    environment {
        DOCKERHUB_USERNAME = 'varun7560'
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
                sh 'python3 -m venv venv'
                sh 'venv/bin/pip install -r requirements.txt'
                sh 'venv/bin/python manage.py test'
            }
        }

        stage('Docker Build') {
            steps {
                sh "docker build -t ${DOCKERHUB_USERNAME}/${IMAGE_NAME}:v${BUILD_NUMBER} ."
            }
        }

        stage('Docker Push') {
            steps {
                sh "docker push ${DOCKERHUB_USERNAME}/${IMAGE_NAME}:v${BUILD_NUMBER}"
            }
        }

        stage('Deploy to Kubernetes') {
            steps {
                sh "kubectl set image deployment/django-deployment django=${DOCKERHUB_USERNAME}/${IMAGE_NAME}:v${BUILD_NUMBER}"
            }
        }

        stage('Verify Deployment') {
            steps {
                sh 'kubectl rollout status deployment/django-deployment'
                sh 'kubectl get pods'
            }
        }
    }
}