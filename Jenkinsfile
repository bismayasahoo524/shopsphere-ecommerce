pipeline {

    agent any

    environment {
        PYTHON = 'C:\\Users\\rudra\\AppData\\Local\\Python\\bin\\python.exe'
        DOCKER = 'C:\\Users\\rudra\\AppData\\Local\\Programs\\DockerDesktop\\resources\\bin\\docker.exe'
    }

    stages {

        stage('Check Environment') {
            steps {
                echo 'Checking Python, pip and Docker...'

                bat '''
                    "%PYTHON%" --version
                    "%PYTHON%" -m pip --version
                    "%DOCKER%" --version
                '''
            }
        }

        stage('Install Dependencies') {
            steps {
                echo 'Installing Product Service dependencies...'

                bat '''
                    cd product-service
                    "%PYTHON%" -m pip install --upgrade pip
                    "%PYTHON%" -m pip install -r requirements.txt
                '''
            }
        }

        stage('Run Python Tests') {
            steps {
                echo 'Running Product Service tests...'

                bat '''
                    cd product-service
                    "%PYTHON%" -m pytest -v
                '''
            }
        }

        stage('Build Docker Image') {
            steps {
                echo 'Building Product Service Docker image...'

                bat '''
                    cd product-service
                    "%DOCKER%" build -t shopsphere-product-service:%BUILD_NUMBER% .
                '''
            }
        }

        stage('Run Docker Container') {
            steps {
                echo 'Starting Product Service Docker container...'

                bat '''
                    "%DOCKER%" run -d ^
                        --name shopsphere-product-test-%BUILD_NUMBER% ^
                        -p 8002:8000 ^
                        shopsphere-product-service:%BUILD_NUMBER%
                '''
            }
        }

        stage('Test Docker Container') {
            steps {
                echo 'Testing Product Service Docker container...'

                bat '''
                    timeout /t 10 /nobreak
                    curl --fail http://localhost:8002/
                '''
            }
        }

        stage('Docker Cleanup') {
            steps {
                echo 'Stopping and removing Docker test container...'

                bat '''
                    "%DOCKER%" stop shopsphere-product-test-%BUILD_NUMBER%
                    "%DOCKER%" rm shopsphere-product-test-%BUILD_NUMBER%
                '''
            }
        }
    }

    post {

        success {
            echo '========================================='
            echo ' Docker Pipeline SUCCESS'
            echo ' Python tests passed'
            echo ' Docker image built'
            echo ' Docker container tested'
            echo '========================================='
        }

        failure {
            echo '========================================='
            echo ' Docker Pipeline FAILED'
            echo ' Check the Jenkins Console Output'
            echo '========================================='
        }

        always {
            echo 'Docker pipeline execution completed.'
        }
    }
}