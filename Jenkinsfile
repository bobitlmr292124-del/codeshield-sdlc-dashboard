
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
                bat '"C:\\Users\\Sarah\'s\\AppData\\Local\\Programs\\Python\\Python314\\python.exe" -m pip install -r requirements.txt'
            }
        }

        stage('Django System Check') {
            steps {
                bat '"C:\\Users\\Sarah\'s\\AppData\\Local\\Programs\\Python\\Python314\\python.exe" manage.py check'
            }
        }

        stage('Run Unit Tests') {
            steps {
                bat '"C:\\Users\\Sarah\'s\\AppData\\Local\\Programs\\Python\\Python314\\python.exe" manage.py test'
            }
        }
    }
}
