pipeline {
    agent { docker { image 'python:3.6.4' } }
    stages {
        stage('build') {
            steps {
                cmd 'python --version'
            }
        }
    }
}