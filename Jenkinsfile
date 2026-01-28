pipeline {
    agent any
    environment {
        // Must match the ID in your Jenkins credentials dropdown
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
                // This already worked in your last run! (image_960ea5.png)
                bat 'python test_app.py'
            }
        }
        stage('SonarQube Analysis') {
            steps {
                script {
                    def scannerHome = tool 'SonarScanner' 
                    // Matches the 'Name' in your System settings (image_95fb23.png)
                    withSonarQubeEnv('sonarserver') { 
                        bat "${scannerHome}\\bin\\sonar-scanner.bat -Dsonar.projectKey=devops-bootcamp-project"
                    }
                }
            }
        }
        stage('Docker Build & Push') {
            steps {
                // Use Windows %VAR% syntax for batch commands
                bat "docker build -t %DOCKER_USER%/%APP_NAME%:%BUILD_NUMBER% ."
                bat "echo %DOCKERHUB_CREDENTIALS_PSW% | docker login -u %DOCKER_USER% --password-stdin"
                bat "docker push %DOCKER_USER%/%APP_NAME%:%BUILD_NUMBER%"
            }
        }
    }
}
