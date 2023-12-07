pipeline {
    agent any

    stages {
        stage('Build') {
            steps {
                script {
                    env.VERSION = '0.1.1'
                }
                sh 'buildah  --security-opt seccomp=unconfined build-using-dockerfile -f Dockerfile --tag dazzler-tt:${VERSION} .'
            }
        }
        stage('Release') {
            steps {
                sh 'cosmos-release ecs-service --backend podman dazzler-tt ${VERSION} myAppImage=dazzler-tt:${VERSION}'
            }
        }
        stage('Deploy') {
            steps {
                echo 'Deploying....'
                sh 'cosmos deploy -r ${VERSION} dazzler-tt test'
            }
        }
    }
}
