pipeline {

    agent any

    stages {

        stage('Checkout') {
            steps {
                echo 'Checking out ShopSphere source code...'

                checkout scm
            }
        }

        stage('Install Dependencies') {
            steps {
                echo 'Installing Product Service dependencies...'

                bat '''
                    cd product-service

                    echo Checking Python version...
                    "C:\\Users\\rudra\\AppData\\Local\\Python\\bin\\python.exe" --version

                    echo Checking pip version...
                    "C:\\Users\\rudra\\AppData\\Local\\Python\\bin\\python.exe" -m pip --version

                    echo Upgrading pip...
                    "C:\\Users\\rudra\\AppData\\Local\\Python\\bin\\python.exe" -m pip install --upgrade pip

                    echo Installing requirements...
                    "C:\\Users\\rudra\\AppData\\Local\\Python\\bin\\python.exe" -m pip install -r requirements.txt

                    echo Installing testing tools...
                    "C:\\Users\\rudra\\AppData\\Local\\Python\\bin\\python.exe" -m pip install pytest pytest-cov
                '''
            }
        }

        stage('Run Tests') {
            steps {
                echo 'Running Product Service tests...'

                bat '''
                    cd product-service

                    "C:\\Users\\rudra\\AppData\\Local\\Python\\bin\\python.exe" -m pytest -v
                '''
            }
        }

        stage('Code Coverage') {
            steps {
                echo 'Generating code coverage report...'

                bat '''
                    cd product-service

                    "C:\\Users\\rudra\\AppData\\Local\\Python\\bin\\python.exe" -m pytest --cov=app --cov-report=term-missing
                '''
            }
        }
    }

    post {

        success {
            echo '========================================'
            echo 'ShopSphere CI Pipeline PASSED!'
            echo '========================================'
        }

        failure {
            echo '========================================'
            echo 'ShopSphere CI Pipeline FAILED!'
            echo 'Check the Console Output for details.'
            echo '========================================'
        }

        always {
            echo 'ShopSphere CI Pipeline execution completed.'
        }
    }
}