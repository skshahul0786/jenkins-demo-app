pipeline {
    agent any

    stages {

        stage('Checkout') {
            steps {
                git branch: 'main',
                    credentialsId: 'github-credentials',
                    url: 'https://github.com/skshahul0786/jenkins-demo-app.git'
            }
        }

        stage('Build') {
            steps {
                sh '''
                    echo "Building application..."
                    python3 --version
                '''
            }
        }

        stage('Test') {
            steps {
                sh '''
                    echo "Running tests..."
                    /tmp/testenv/bin/pytest
                '''
            }
        }

        stage('Package') {
            steps {
                sh '''
                    echo "Creating package..."
                    tar -czf application.tar.gz app/
                '''
            }
        }

        stage('Archive') {
            steps {
                archiveArtifacts artifacts: 'application.tar.gz',
                                   fingerprint: true
            }
        }
    }

    post {
        success {
            echo 'Application CI completed successfully!'
        }

        failure {
            echo 'Application CI failed!'
        }
    }
}
