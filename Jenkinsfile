pipeline {
    agent any
    stages {
        stage('Checkout') {
            steps { checkout scm }
        }
        stage('Build') {
            steps {
                sh 'docker build -t flask-frontend .'
            }
        }
        stage('Deploy') {
            steps {
                sh 'docker run -d -p 3000:3000 --link flask-backend:backend flask-frontend'
            }
        }
    }
}
