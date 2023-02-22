pipeline {
  agent any
  stages {
    stage('Checkout Code') {
      steps {
        git(url: 'https://github.com/devkaigen/poc-deploy-desktop.git', branch: 'ER-19-Executable-test')
      }
    }

    stage('Log') {
      parallel {
        stage('Log') {
          steps {
            sh 'pwd && ls -la'
          }
        }

        stage('Python test') {
          steps {
            sh 'python3 -m pytest'
          }
        }

      }
    }

  }
}