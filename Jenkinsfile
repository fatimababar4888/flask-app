pipeline {
    agent any

    stages {
        stage('Declarative: Checkout SCM') {
            steps {
                checkout scm
            }
        }

        stage('Clone Repository') {
            steps {
                git url: 'https://github.com/fatimababar4888/flask-app.git', branch: 'main'
            }
        }

        stage('Install Dependencies') {
            steps {
                // Use full path to python.exe to create virtual environment
                bat 'C:\\Users\\sanaz\\AppData\\Local\\Microsoft\\WindowsApps\\python.exe -m venv venv'
                bat 'venv\\Scripts\\pip install --upgrade pip'
                bat 'venv\\Scripts\\pip install -r requirements.txt'
            }
        }

        stage('Run Unit Tests') {
            steps {
                bat 'venv\\Scripts\\pytest tests'
            }
        }

        stage('Build Application') {
            steps {
                echo 'Building application...'
            }
        }

        stage('Deploy (Simulated)') {
            steps {
                echo 'Deploying application (simulated)...'
            }
        }
    }

    post {
        always {
            echo 'Pipeline finished.'
        }
        success {
            echo 'Pipeline completed successfully!'
        }
        failure {
            echo 'Pipeline failed — check logs.'
        }
    }
}
