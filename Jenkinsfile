pipeline {
  agent any
  stages {
    stage('Checkout Code') {
      steps {
        git(url: 'https://github.com/devkaigen/poc-deploy-desktop.git', branch: 'main')
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

    stage('Build') {
      steps {
        sh 'pyinstaller --clean --onefile --noconsole  window.py && ls -la'
        archiveArtifacts 'dist/window'
      }
    }

  }
}