pipeline {
    agent any
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

