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
            sh 'python calc.py'
          }
        }

        stage('Build') {
          steps {
            sh 'python3 -m pytest'
          }
        }

      }
    }

    stage('Python Test') {
      steps {
        sh 'python pytest'
      }
    }

  }
}