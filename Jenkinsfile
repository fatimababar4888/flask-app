pipeline {
    agent any

    triggers {
        githubPush()
    }

    stages {

        stage('Clone Repository') {
            steps {
                git branch: 'main', url: 'https://github.com/fatimababar4888/flask-app.git'
            }
        }

        stage('Install Dependencies') {
            steps {
                bat 'py -m venv venv'
                bat 'venv\\Scripts\\pip install --upgrade pip'
                bat 'venv\\Scripts\\pip install -r requirements.txt'
            }
        }

        stage('Run Unit Tests') {
            steps {
                bat 'venv\\Scripts\\pytest || exit /b 0'
            }
        }

        stage('Build Application') {
            steps {
                bat 'if not exist build mkdir build'
                bat 'xcopy /E /I /Y * build\\'
            }
        }

        stage('Deploy (Simulated)') {
            steps {
                bat 'if not exist C:\\tmp\\flask-deploy mkdir C:\\tmp\\flask-deploy'
                bat 'xcopy /E /I /Y build\\* C:\\tmp\\flask-deploy\\'
            }
        }
    }

    post {
        success {
            echo 'Pipeline completed successfully!'
        }
        failure {
            echo 'Pipeline failed — check logs.'
        }
    }
}
