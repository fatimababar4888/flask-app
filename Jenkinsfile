pipeline {
    agent any

    triggers {
        // Trigger pipeline on GitHub push (if webhook is configured)
        pollSCM('* * * * *') // optional, otherwise use GitHub webhook
    }

    stages {
        stage('Clone Repository') {
            steps {
                // Clone your Flask app from GitHub
                git url: 'https://github.com/fatimababar4888/flask-app.git', branch: 'main'
            }
        }

        stage('Install Dependencies') {
            steps {
                // Create virtual environment
                bat 'python -m venv venv'
                
                // Upgrade pip and install dependencies
                bat 'venv\\Scripts\\pip install --upgrade pip'
                bat 'venv\\Scripts\\pip install -r requirements.txt'
            }
        }

        stage('Run Unit Tests') {
            steps {
                // Run tests using pytest
                bat 'venv\\Scripts\\pytest tests'
            }
        }

        stage('Build Application') {
            steps {
                echo 'Building Flask app...'
                // Optional: zip the app folder for deployment
                bat 'powershell Compress-Archive -Path * -DestinationPath flask-app.zip'
            }
        }

        stage('Deploy Application (Simulated)') {
            steps {
                echo 'Deploying Flask app (simulated)...'
                // Copy files to a target folder to simulate deployment
                bat 'xcopy /E /Y * C:\\flask-app-deploy\\'
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
