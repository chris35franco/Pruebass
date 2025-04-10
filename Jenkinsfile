pipeline {
    agent any
    stages {
        stage('Crear entorno virtual e instalar dependencias') {
            steps {
                sh '''
                    python3 -m venv venv
                    . venv/bin/activate
                    pip install -r requirements.txt
                '''
            }
        }
        stage('Ejecutar pruebas') {
            steps {
                sh '''
                    . venv/bin/activate
                    pytest prueba_calculo_pago.py
                '''
            }
        }
    }
}



