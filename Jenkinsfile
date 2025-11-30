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
                    docker.build("pam-fitness-backend")
                    """
                }
            }
        }

        // stage('Login to ECR') {
        //     steps {
        //         script {
        //             sh """
        //             aws ecr get-login-password --region $AWS_REGION | docker login --username AWS --password-stdin $BACKEND_ECR
        //             """
        //         }
        //     }
        // }

        // stage('Tag & Push Images') {
        //     steps {
        //         script {
        //             sh """
        //             docker tag pam-fitness-backend:latest $BACKEND_ECR:latest

        //             docker push $BACKEND_ECR:latest
        //             """
        //         }
        //     }
        // }

        // stage('Deploy to EC2') {
        //     steps {
        //         script {
        //             withCredentials([sshUserPrivateKey(credentialsId: 'ec2-ssh-key', keyFileVariable: 'KEY')]) {

        //                 // BACKEND DEPLOY (via Bastion)
        //                 sh """
        //                 ssh -o StrictHostKeyChecking=no -i $KEY -A $BASTION_EC2 '
        //                     ssh -o StrictHostKeyChecking=no ec2-user@$BACKEND_EC2 "
        //                         sudo docker pull $BACKEND_ECR:latest &&
        //                         sudo docker stop backend || true &&
        //                         sudo docker rm backend || true &&
        //                         sudo docker run -d --name backend -p 8000:8000 $BACKEND_ECR:latest
        //                     "
        //                 '
        //                 """
        //             }
        //         }
        //     }
        // }
    }
}
