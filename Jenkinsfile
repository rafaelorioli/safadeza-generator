pipeline {
  agent any
  stages {
    stage('Gera Docker Image') {
      agent {
        dockerfile {
          filename 'Dockerfile'
        }

      }
      steps {
        echo 'Criando Docker Image'
      }
    }
    stage('Executa Docker Image') {
      agent {
        docker {
          image 'safadeza-generator'
          args 'python main.py --post-to-twitter'
        }

      }
      steps {
        echo 'Executando Docker Image'
      }
    }
  }
}