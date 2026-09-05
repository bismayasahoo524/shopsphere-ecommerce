pipeline {

    agent any

    environment {
        PYTHON = 'C:\\Users\\rudra\\AppData\\Local\\Python\\bin\\python.exe'
    }

    stages {

        stage('Check Environment') {
            steps {
                echo 'Checking Python and Docker...'

                bat '''
                    "%PYTHON%" --version
                    "%PYTHON%" -m pip --version
                    docker --version
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
                    docker build -t shopsphere-product-service:%BUILD_NUMBER% .
                '''
            }
        }

        stage('Run Docker Container') {
            steps {
                echo 'Starting Docker container...'

                bat '''
                    docker run -d ^
                        --name shopsphere-product-test-%BUILD_NUMBER% ^
                        -p 8002:8000 ^
                        shopsphere-product-service:%BUILD_NUMBER%
                '''
            }
        }

        stage('Test Docker Container') {
            steps {
                echo 'Testing Docker container...'

                bat '''
                    timeout /t 10 /nobreak
                    curl --fail http://localhost:8002/
                '''
            }
        }

        stage('Docker Cleanup') {
            steps {
                echo 'Stopping and removing test container...'

                bat '''
                    docker stop shopsphere-product-test-%BUILD_NUMBER%
                    docker rm shopsphere-product-test-%BUILD_NUMBER%
                '''
            }
        }
    }

    post {

        success {
            echo '========================================='
            echo ' Docker Pipeline SUCCESS'
            echo ' Docker image built and tested successfully'
            echo '========================================='
        }

        failure {
            echo '========================================='
            echo ' Docker Pipeline FAILED'
            echo ' Check the Jenkins console output'
            echo '========================================='
        }

        always {
            echo 'Docker pipeline execution completed.'
        }
    }
}
