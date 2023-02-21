pipeline {
  agent any
  stages {
    stage('Git Checkout ') {
      steps {
        git(url: 'https://github.com/devkaigen/poc-deploy-desktop.git', branch: 'main')
      }
    }

    stage('') {
      steps {
        sh 'pwd && ls -la'
      }
    }

  }
}