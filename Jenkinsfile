pipeline {
    agent any
    stages {
        stage('Setup Virtual Environment') {
            steps {
                sh 'python3 -m venv venv'
                sh 'venv/bin/pip install --upgrade pip'
            }
        }
        stage('Lint') {
            steps {
                sh 'venv/bin/pip install pylint'
                sh 'venv/bin/pylint app.py'
            }
        }
        stage('Build') {
            steps {
                sh 'venv/bin/pip install -r requirements.txt'
            }
        }
        stage('Unit Test') {    
            steps {
                sh 'venv/bin/pip install pytest'
                sh 'venv/bin/pytest tests/test_unit.py'
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
                sh 'venv/bin/pytest tests/test_selenium.py'
            }
        }
    }
}