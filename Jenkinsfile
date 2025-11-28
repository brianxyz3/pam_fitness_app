pipeline {
    agent any

    environment {
        AWS_REGION = 'eu-west-1'
        BACKEND_ECR  = '849349795052.dkr.ecr.eu-west-1.amazonaws.com/pam_fitness_app_backend' // to be editted
        BASTION_EC2 = 'ec2-user@FRONTEND-EC2-PUBLIC-IP' // to be editted
        BACKEND_EC2  = 'ec2-user@10.0.3.0/24'
    }

    stages {

        stage('Checkout Code') {
            steps {
                git branch: 'main', url: 'https://github.com/brianxyz3/pam_fitness_app.git'
            }
        }

        stage('Build Backend') {
            steps {
                script {
                    sh """
                    cd backend
                    docker build -t pam-fitness-backend .
                    """
                }
            }
        }

        
    }
}
