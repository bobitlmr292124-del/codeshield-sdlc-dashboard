
pipeline {
    agent any

    stages {

        stage('Checkout') {
            steps {
                git branch: 'main',
                url: 'https://github.com/bobitlmr292124-del/codeshield-sdlc-dashboard.git'
            }
        }

        stage('Install Dependencies') {
            steps {
                bat 'python -m pip install -r requirements.txt'
            }
        }

        stage('Django System Check') {
            steps {
                bat 'python manage.py check'
            }
        }

        stage('Run Unit Tests') {
            steps {
                bat 'python manage.py test'
            }
        }
    }
}
