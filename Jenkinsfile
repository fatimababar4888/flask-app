pipeline {
    agent any

    triggers {
        // Trigger pipeline on GitHub push (optional if you also use webhooks)
        pollSCM('* * * * *') 
    }

    environment {
        // Absolute path to the system-wide Python
        PYTHON = "C:\\Program Files\\Python314\\python.exe"
    }

    stages {

        stage('Clone Repository') {
            steps {
                git url: 'https://github.com/fatimababar4888/flask-app.git', branch: 'main'
            }
        }

        stage('Install Dependencies') {
            steps {
                // Create virtual environment
                bat "${env.PYTHON} -m venv venv"
                // Upgrade pip
                bat "venv\\Scripts\\pip install --upgrade pip"
                // Install dependencies from requirements.txt
                bat "venv\\Scripts\\pip install -r requirements.txt"
            }
        }

        stage('Run Unit Tests') {
            steps {
                // Run pytest (assuming tests are in /tests folder)
                bat "venv\\Scripts\\pytest tests"
            }
        }

        stage('Build Application') {
            steps {
                echo 'Building Flask app...'
                // Example: create a zip package of the app
                bat "powershell Compress-Archive -Path * -DestinationPath flask-app.zip"
            }
        }

        stage('Deploy Application (Simulated)') {
            steps {
                echo 'Deploying Flask app (simulated)...'
                // Example: copy files to a deployment directory
                bat "xcopy /E /Y * C:\\flask-app-deploy\\"
            }
        }
    }

    post {
        always { echo 'Pipeline finished.' }
        success { echo 'Pipeline completed successfully!' }
        failure { echo 'Pipeline failed — check logs.' }
    }
}
