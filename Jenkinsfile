pipeline {
  agent any
  stages {
    stage('Checkout Code') {
      steps {
        git(url: 'https://github.com/devkaigen/poc-deploy-desktop', branch: 'main', credentialsId: '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')
      }
    }

    stage('Log') {
      parallel {
        stage('Log') {
          steps {
            sh 'pwd && ls -la'
          }
        }

        stage('Build') {
          steps {
            sh 'python3 calc.py'
          }
        }

      }
    }

    stage('Python Test') {
      steps {
        sh 'python3 -m pytest'
      }
    }

  }
}