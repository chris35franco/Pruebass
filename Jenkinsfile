pipeline {
    agent any
    stages {
        stage('Instalar dependencias') {
            steps {
                sh 'pip3 install -r requirements.txt'
            }
        }
        stage('Ejecutar pruebas') {
            steps {
                sh 'python3 -m pytest prueba_calculo_pago.py'
            }
        }
    }
}


