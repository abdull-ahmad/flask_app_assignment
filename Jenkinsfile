pipeline {
    agent any
    stages {
        stage('Lint') {
            steps {
                sh 'python3-pip install pylint'
                sh 'pylint app.py'
            }
        }
        stage('Build') {
            steps {
                sh 'pip install -r requirements.txt'
            }
        }
        stage('Unit Test') {
            steps {
                sh 'pytest tests/test_unit.py'
            }
        }
        stage('Docker Build & Run') {
            steps {
                sh 'docker build -t flaskapp .'
                sh 'docker run -d -p 5000:5000 flaskapp'
            }
        }
        stage('Selenium Test') {
            steps {
                sh 'pytest tests/test_selenium.py'
            }
        }
    }
}