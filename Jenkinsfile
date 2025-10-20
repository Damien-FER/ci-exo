pipeline {
  agent any
  stages {
    stage('Checkout') {
      steps { checkout scm }
    }
    stage('Set up Python') {
      steps {
        sh 'python3 -m venv venv'
        sh '. venv/bin/activate && pip install --upgrade pip'
      }
    }
    stage('Run tests') {
      steps {
        sh '. venv/bin/activate && python -m unittest discover -s ci_demo/tests'
      }
    }
  }
  post {
    success { echo 'Pipeline completed successfully!' }
    failure { echo 'Pipeline failed.' }
  }
}