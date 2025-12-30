pipeline {
    agent any

    environment {
        VENV_DIR = 'venv'
        PYTHON = "${VENV_DIR}\\Scripts\\python"
        PIP = "${VENV_DIR}\\Scripts\\pip"
    }

    stages {
        stage('Checkout SCM') {
            steps {
                echo 'Checking out code from Git...'
                checkout scm
            }
        }

        stage('Install Dependencies') {
            steps {
                echo 'Creating virtual environment and installing dependencies...'
                bat "\"C:\\Program Files\\Python314\\python.exe\" -m venv %VENV_DIR%"
                bat "%PIP% install --upgrade pip"
                bat "%PIP% install -r requirements.txt"
            }
        }

        stage('Run Unit Tests') {
            steps {
                echo 'Running unit tests with pytest...'
                // Ensure tests are run from project root so 'app.py' is visible
                bat "cd %WORKSPACE% && %PYTHON% -m pytest tests"
            }
        }

        stage('Build Application') {
            steps {
                echo 'Building application... (optional step)'
                // Add your build steps here if needed
            }
        }

        stage('Deploy Application (Simulated)') {
            steps {
                echo 'Deploying application (simulated)...'
                // Add deployment steps here if you want
            }
        }
    }

    post {
        always {
            echo 'Pipeline finished.'
        }
        success {
            echo 'Pipeline succeeded!'
        }
        failure {
            echo 'Pipeline failed — check logs.'
        }
    }
}
