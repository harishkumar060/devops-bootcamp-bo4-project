pipeline {
    agent any
    environment {
        DOCKERHUB_CREDENTIALS = credentials('docker-hub-credentials-id') 
        APP_NAME = "devops-bootcamp-project"
        DOCKER_USER = "harishdockeremc" 
    }
    stages {
        stage('Checkout') {
            steps { 
                checkout scm 
            }
        }
        stage('Unit Test') {
            steps {
                bat 'python test_app.py'
            }
        }
        stage('SonarQube Analysis') {
            steps {
                script {
                    def scannerHome = tool 'SonarScanner' 
                    withSonarQubeEnv('sonarserver') { 
                        bat "${scannerHome}\\bin\\sonar-scanner.bat -Dsonar.projectKey=devops-bootcamp-project"
                    }
                }
            }
        }
        stage('Docker Build & Push') {
            steps {
                bat "docker build -t %DOCKER_USER%/%APP_NAME%:%BUILD_NUMBER% ."
                bat "echo %DOCKERHUB_CREDENTIALS_PSW% | docker login -u %DOCKERHUB_CREDENTIALS_USR% --password-stdin"
                bat "docker push %DOCKER_USER%/%APP_NAME%:%BUILD_NUMBER%"
            }
        }
    }
}
