pipeline {
    agent any
    environment {
        DOCKERHUB_CREDENTIALS = credentials('docker-hub-credentials-id') 
        APP_NAME = "devops-bootcamp-project"
        DOCKER_USER = "harishdockeremc" 
    }
    stages {
        stage('Checkout') {
            steps { checkout scm }
        }
        stage('Unit Test') {
            steps {
                sh 'python3 test_app.py'
            }
        }
        stage('SonarQube Analysis') {
            steps {
                script {
                    def scannerHome = tool 'SonarScanner' 
                    withSonarQubeEnv('SonarQubeServer') { 
                        sh "${scannerHome}/bin/sonar-scanner -Dsonar.projectKey=${APP_NAME}"
                    }
                }
            }
        }
        stage('Docker Build & Push') {
            steps {
                sh "docker build -t ${DOCKER_USER}/${APP_NAME}:${BUILD_NUMBER} ."
                sh "echo $DOCKERHUB_CREDENTIALS_PSW | docker login -u $DOCKERHUB_CREDENTIALS_USR --password-stdin"
                sh "docker push ${DOCKER_USER}/${APP_NAME}:${BUILD_NUMBER}"
            }
        }
    }
}
