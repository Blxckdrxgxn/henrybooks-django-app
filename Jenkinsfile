pipeline {
    agent any

    environment {
        DOCKER_IMAGE = "henrybooks-django-app"
    }

    stages {
        stage('Clone Repo') {
            steps {
                git 'https://github.com/Blxckdrxgxn/henrybooks-django-app.git'
            }
        }

        stage('Build Docker Image') {
            steps {
                script {
                    sh 'docker-compose build'
                }
            }
        }

        stage('Run Docker Compose') {
            steps {
                script {
                    sh 'docker-compose up -d'
                }
            }
        }

        stage('Run Tests') {
            steps {
                script {
                    sh 'docker-compose exec -T web python manage.py test'
                }
            }
        }

        stage('Cleanup') {
            steps {
                script {
                    sh 'docker-compose down'
                }
            }
        }
    }

    post {
        always {
            echo "Pipeline execution complete."
        }
    }
}
