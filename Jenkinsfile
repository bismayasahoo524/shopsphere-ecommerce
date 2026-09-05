pipeline {

    agent any

    stages {

        stage('Checkout') {
            steps {
                checkout scm
            }
        }

        stage('Install Dependencies') {
            steps {
                bat '''
                    cd product-service
                    python -m pip install --upgrade pip
                    pip install -r requirements.txt
                    pip install pytest pytest-cov
                '''
            }
        }

        stage('Run Tests') {
            steps {
                bat '''
                    cd product-service
                    python -m pytest -v
                '''
            }
        }

        stage('Code Coverage') {
            steps {
                bat '''
                    cd product-service
                    python -m pytest --cov=app --cov-report=term
                '''
            }
        }
    }

    post {

        success {
            echo 'ShopSphere pipeline completed successfully!'
        }

        failure {
            echo 'ShopSphere pipeline failed. Check the console output.'
        }
    }
}