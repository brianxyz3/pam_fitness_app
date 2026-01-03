pipeline {
    agent any

    environment {
        AWS_REGION = 'eu-west-1'
        BACKEND_ECR  = '849349795052.dkr.ecr.eu-west-1.amazonaws.com/pam_fitness_app_backend'
        BASTION_EC2 = 'ec2-user@54.246.223.128'
        BACKEND_EC2  = 'ec2-user@10.0.3.90'
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
                    docker build -t pam-fitness-backend .
                    """
                }
            }
        }

        stage('Login to ECR') {
            steps {
                withCredentials([
                    string(credentialsId: 'AWS_ACCESS_KEY_ID', variable: 'AWS_ACCESS_KEY_ID'),
                    string(credentialsId: 'AWS_SECRET_ACCESS_KEY', variable: 'AWS_SECRET_ACCESS_KEY')
                ]) {

                    sh """
                        aws configure set aws_access_key_id $AWS_ACCESS_KEY_ID
                        aws configure set aws_secret_access_key $AWS_SECRET_ACCESS_KEY
                        aws configure set default.region $AWS_REGION

                        aws ecr get-login-password --region $AWS_REGION \
                        | docker login --username AWS --password-stdin $BACKEND_ECR
                    """
                }
            }
        }

        stage('Tag & Push Images') {
            steps {
                script {
                    sh """
                    docker tag pam-fitness-backend:latest $BACKEND_ECR:latest

                    docker push $BACKEND_ECR:latest
                    """
                }
            }
        }

        stage('Deploy to EC2') {
            steps {
                script {
                    withCredentials([sshUserPrivateKey(credentialsId: 'ec2-ssh-key', keyFileVariable: 'KEY')]) {

                        // BACKEND DEPLOY (via Bastion)
                        sh """
                        ssh -o StrictHostKeyChecking=no -i $KEY -A $BASTION_EC2 '
                            ssh -o StrictHostKeyChecking=no ec2-user@$BACKEND_EC2 "
                                sudo docker pull $BACKEND_ECR:latest &&
                                sudo docker stop backend || true &&
                                sudo docker rm backend || true &&
                                sudo docker run -d --name backend -p 8000:8000 $BACKEND_ECR:latest
                            "
                        '
                        """
                    }
                }
            }
        }
    }
}
