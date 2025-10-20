pipeline {
    agent any

    stages {
        // Stage 1 : récupérer le code depuis Git
        stage('Checkout') {
            steps {
                checkout scm
            }
        }

        // Stage 2 : installer Python et créer l'environnement virtuel
        stage('Set up Python') {
            steps {
                sh '''
                    # Mettre à jour les paquets
                    apt-get update
                    # Installer Python3, pip et venv
                    apt-get install -y python3 python3-venv python3-pip
                    # Créer l'environnement virtuel
                    python3 -m venv venv
                    # Activer l'environnement et mettre pip à jour
                    . venv/bin/activate
                    pip install --upgrade pip
                '''
            }
        }

        // Stage 3 : exécuter les tests unitaires
        stage('Run tests') {
            steps {
                sh '''
                    # Activer l'environnement virtuel
                    . venv/bin/activate
                    # Lancer les tests unitaires
                    python -m unittest discover -s ci_demo/tests
                '''
            }
        }
    }

    // Notifications en fin de pipeline
    post {
        success {
            echo 'Pipeline completed successfully!'
        }
        failure {
            echo 'Pipeline failed.'
        }
    }
}
