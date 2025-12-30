pipeline {
    agent any

    triggers {
        // Poll GitHub repo every minute (adjust as needed)
        pollSCM('* * * * *')
    }

    environment {
        // Absolute path to Python with quotes to handle spaces
        PYTHON = '"C:\\Program Files\\Python314\\python.exe"'
    }

    stages {

        stage('Clone Repository') {
            steps {
                git url: 'https://github.com/fatimababar4888/flask-app.git', branch: 'main'
            }
        }

        stage('Install Dependencies') {
            steps {
                echo 'Creating virtual environment and installing dependencies...'
                // Create virtual environment
                bat "${env.PYTHON} -m venv venv"
                // Upgrade pip
                bat 'venv\\Scripts\\pip install --upgrade pip'
                // Install requirements
                bat 'venv\\Scripts\\pip install -r requirements.txt'
            }
        }

        stage('Run Unit Tests') {
            steps {
                echo 'Running unit tests with pytest...'
                // Run pytest (assuming tests are in /tests folder)
                bat 'venv\\Scripts\\pytest tests'
            }
        }

        stage('Build Application') {
            steps {
                echo 'Building Flask app (packaging)...'
                // Example: create a zip package of the app
                bat 'powershell Compress-Archive -Path * -DestinationPath flask-app.zip'
            }
        }

        stage('Deploy Application (Simulated)') {
            steps {
                echo 'Deploying Flask app (simulated)...'
                // Example: copy files to a deployment directory
                bat 'xcopy /E /Y * C:\\flask-app-deploy\\'
            }
        }
    }

    post {
        always { echo 'Pipeline finished.' }
        success { echo 'Pipeline completed successfully!' }
        failure { echo 'Pipeline failed — check logs.' }
    }
}
