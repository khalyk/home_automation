pipeline {
    agent none
    
    options {
        ansiColor('xterm')
    }
    
    stages {
        stage ('Cleanup') {
            agent any
            steps {
                echo "Cleaning up ${WORKSPACE}..."
                sh 'rm -rf *'
            }
        }
        
        stage ('Checkout - khalyk/home_automation') {
            agent any
            steps {
                checkout([$class: 'GitSCM', 
                    branches: [[name: '*/master']], 
                    doGenerateSubmoduleConfigurations: false, 
                    submoduleCfg: [], 
                    userRemoteConfigs: [[url: 'https://github.com/khalyk/home_automation.git']]])
            }
        }
        
        stage ('Fetch/extract DHT22 python module') {
            agent any
            steps {
                dir ('home_automation') {
		    sh "wget http://abyz.me.uk/rpi/pigpio/code/DHT22_py.zip"
		    sh "unzip DHT22_py.zip"
		}  
	    }
        }
        
        stage ('Build') {
            agent any
            steps {
                dir ('home_automation') {
                    sh "docker build -t khalyk/homeauto:latest ."
                }
            }
        }
        
        stage('Publish') {
            agent any
            steps {
                withDockerRegistry([ credentialsId: "docker", url: "" ]) {
                    sh 'docker push khalyk/homeauto:latest'
                }
            }
        }
    }
}
