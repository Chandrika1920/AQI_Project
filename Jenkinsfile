pipeline {
    agent any

    stages {
        stage('Clone Repo') {
            steps {
                git 'https://github.com/Chandrika1920/AQI_Project.git'
            }
        }

        stage('Build Docker Image') {
            steps {
                script {
                    docker.build('aqi_app')
                }
            }
        }

        stage('Run Docker Container') {
            steps {
                script {
                    sh 'docker run -d -p 8501:8501 aqi_app'
                }
            }
        }
    }
}
