pipeline {
  agent any
  stages {
    stage('Checkout Code') {
      steps {
        git(url: 'https://github.com/devkaigen/poc-deploy-desktop', branch: 'main')
      }
    }

    stage('Log') {
      parallel {
        stage('Log') {
          steps {
            sh 'ls -la'
          }
        }

        stage('Build') {
          steps {
            sh 'python calc.py'
          }
        }

      }
    }

    stage('Python Test') {
      steps {
        sh 'python -m pytest'
      }
    }

  }
}