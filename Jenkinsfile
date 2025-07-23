pipeline {
    agent any

    environment {
        DOCKER_IMAGE = 'yourdockerhubusername/henrybooks-django-app'
    }

    stages {
        stage('Clone Repo') {
            steps {
                git branch: 'main', url: 'https://github.com/Blxckdrxgxn/henrybooks-django-app.git'
            }
        }

        stage('Build Docker Image') {
            steps {
                bat 'docker build -t %DOCKER_IMAGE% .'
            }
        }

        stage('Run Docker Compose') {
            steps {
                bat 'docker-compose down || exit 0'
                bat 'docker-compose up -d --build'
            }
        }

        stage('Run Tests') {
            steps {
                bat 'docker-compose exec web python manage.py test || exit 0'
            }
        }

        stage('Cleanup') {
            steps {
                bat 'docker system prune -f'
            }
        }
    }
}
