pipeline {
    agent any

    environment {
        VENV_DIR = 'venv'
        PYTHON = "${VENV_DIR}\\Scripts\\python"
        PIP = "${VENV_DIR}\\Scripts\\pip"
        DEPLOY_DIR = "C:\\FlaskAppDeploy"  // Deployment folder
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
                // For Flask, build can be packaging or preparing app folder
                bat "echo 'No specific build steps for Flask, just verifying workspace.'"
            }
        }

        stage('Deploy Application (Simulated)') {
            steps {
                echo 'Simulating deployment...'
                // Create deployment folder if it doesn't exist
                bat "if not exist %DEPLOY_DIR% mkdir %DEPLOY_DIR%"
                // Copy all app files to deployment folder
                bat "xcopy /E /I /Y %WORKSPACE%\\* %DEPLOY_DIR%\\"
                echo "Files deployed to %DEPLOY_DIR%"
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
