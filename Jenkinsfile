@Library("shared") _
pipeline{
    agent { label 'bk'}
    
    stages{
        stage("Code clone"){
            steps{
                sh "whoami"
            clone("https://github.com/bhavesh-kumawat/flask-app-ecs.git","main")
            }
        }
        stage("Code Build"){
            steps{
            docker_build("flask-app","latest")
            }
        }
        stage("Push to DockerHub"){
            steps{
                docker_push("flask-app", "latest", "DockerHubCred")
            }
        }
        stage("Deploy"){
            steps{
                echo "This is deploying th code"
                sh "docker compose up -d"
            }
        }

    }
}
