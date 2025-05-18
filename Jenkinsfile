pipeline {
    agent any
    stages {
        stage('Setup Python Env') {
            steps {
                sh '''
                python3 -m venv venv
                . venv/bin/activate
                pip install --upgrade pip
                pip install pylint pytest -r requirements.txt
                '''
            }
        }
        stage('Lint') {
            steps {
                sh '''
                . venv/bin/activate
                pylint app.py
                '''
            }
        }
        stage('Unit Test') {
            steps {
                sh '''
                . venv/bin/activate
                pytest tests/test_unit.py
                '''
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
                sh '''
                . venv/bin/activate
                pytest tests/test_selenium.py
                '''
            }
        }
    }
}
