pipeline {
    agent any
    environment {
        VENV = 'venv'
    }
    stages {
        stage('Setup Python venv') {
            steps {
                sh '''
                    python3 -m venv $VENV
                    . $VENV/bin/activate
                    pip install --upgrade pip
                '''
            }
        }
        stage('Lint') {
            steps {
                sh '''
                    . $VENV/bin/activate
                    pip install pylint
                    $VENV/bin/pylint app.py
                '''
            }
        }
        stage('Build') {
            steps {
                sh '''
                    . $VENV/bin/activate
                    pip install -r requirements.txt
                '''
            }
        }
        stage('Unit Test') {
            steps {
                sh '''
                    . $VENV/bin/activate
                    $VENV/bin/pytest tests/test_unit.py
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
                    . $VENV/bin/activate
                    $VENV/bin/pytest tests/test_selenium.py
                '''
            }
        }
    }
}
