pipeline {
  agent any
  stages {
    stage('Checkout Code') {
      steps {
        git(url: 'https://github.com/devkaigen/poc-deploy-desktop.git', branch: 'main', credentialsId: '3b0d0363-a972-4cb3-8237-b927199bc945')
      }
    }

  }
}