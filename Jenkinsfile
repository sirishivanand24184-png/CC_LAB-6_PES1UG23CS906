pipeline {
    agent any

    stages {

        stage('Build Backend') {
            steps {
                echo 'Building backend Docker image...'
                sh 'docker build -t backend-image ./backend'
            }
        }

        stage('Run Backend Container') {
            steps {
                echo 'Running backend container...'
                sh 'docker run --name backend-container backend-image'
            }
        }

        stage('Build NGINX Image') {
            steps {
                echo 'Pulling nginx image...'
                sh 'docker pull nginx'
            }
        }

        stage('Success') {
            steps {
                echo 'CI/CD Pipeline completed successfully for PES1UG23CS906'
            }
        }
    }
}
