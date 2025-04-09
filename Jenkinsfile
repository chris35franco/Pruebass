pipeline {
    agent {
        docker {
            image 'python:3.10'
        }
    }

    stages {
        stage('Instalar dependencias') {
            steps {
                sh 'pip install -r requirements.txt'
            }
        }

        stage('Ejecutar pruebas') {
            steps {
                sh 'pytest prueba_calculo_pago.py'
            }
        }
    }
}
