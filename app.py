from flask import Flask, render_template, request, jsonify
import random

app = Flask(__name__)

@app.route('/')
def index():
    print("Se accedió a la ruta raíz.")
    return render_template('index.html')

@app.route('/get_response', methods=['POST'])
def get_response():
    message = request.form['message']
    response = generate_response(message)
    return jsonify({'response': response})

def generate_response(message):
    # Se convierte el mensaje a minisculas para facilitat la coincidencia
    message = message.lower()

    # Keywords
    responses = {
         'hola': ['¡Hola! ¿Cómo puedo ayudarte hoy?', '¡Hola! ¿En qué puedo asistirte?', 'Hola, ¿cómo estás? ¿En qué puedo ayudarte?'],
        'que es azure?': ['Azure es la plataforma de computación en la nube de Microsoft. ¿Necesitas información específica sobre Azure?'],
        'az900': ['El examen AZ-900: Microsoft Azure Fundamentals evalúa los conceptos básicos de Azure. ¿Tienes alguna pregunta en particular sobre este examen?'],
        'az104': ['El examen AZ-104: Microsoft Azure Administrator evalúa las habilidades de administración de Azure. ¿En qué puedo ayudarte con respecto a este examen?'],
        'plataforma de azure': ['La plataforma de Azure ofrece una amplia gama de servicios en la nube para desarrollar, implementar y administrar aplicaciones. ¿Qué te gustaría saber sobre la plataforma de Azure?'],
        'ayuda': ['Estoy aquí para responder tus preguntas sobre Azure, AZ-900, AZ-104 y más. ¿En qué puedo asistirte?'],
        'gracias': ['De nada, ¡siempre estoy aquí para ayudarte!', '¡No hay problema! ¿Hay algo más en lo que pueda ayudarte?'],
        'iaas': ['Azure Infrastructure as a Service (IaaS) te ofrece recursos de computación, almacenamiento y redes en la nube para que puedas ejecutar tus aplicaciones y cargas de trabajo. ¿Necesitas información sobre IaaS en Azure?'],
        'paas': ['Azure Platform as a Service (PaaS) te permite crear, implementar y administrar aplicaciones sin tener que preocuparte por la infraestructura subyacente. ¿Qué te gustaría saber sobre PaaS en Azure?'],
        'servicios cognitivos': ['Azure Cognitive Services te ofrece APIs preentrenadas para agregar capacidades de visión, voz, lenguaje y búsqueda a tus aplicaciones. ¿Tienes preguntas sobre los servicios cognitivos en Azure?'],
        'streaming': ['Azure Stream Analytics es un servicio de análisis en tiempo real que te permite procesar y analizar datos de streaming en tiempo real. ¿Qué te gustaría saber sobre el streaming en Azure?'],
        'costos': ['Azure Cost Management + Billing te ayuda a optimizar y administrar los costos de tus recursos en la nube de Azure. ¿Necesitas información sobre cómo controlar los costos en Azure?'],
        'migration': ['Azure Migration te ofrece herramientas y servicios para ayudarte a migrar tus aplicaciones y cargas de trabajo a la nube de Azure de manera rápida y sencilla. ¿Tienes preguntas sobre migración en Azure?'],
        'resiliencia': ['Azure te ofrece una amplia gama de servicios y características para garantizar la resiliencia y la continuidad del negocio de tus aplicaciones en la nube. ¿Qué te gustaría saber sobre la resiliencia en Azure?'],
        'que es disponibilidad?': ['Azure garantiza una alta disponibilidad para tus aplicaciones y servicios en la nube a través de redundancia geográfica y servicios de conmutación por error. ¿Necesitas información sobre la disponibilidad en Azure?'],
        'escalabilidad automática': ['Azure Autoscale te permite escalar automáticamente tus aplicaciones en función de la demanda para garantizar un rendimiento óptimo. ¿Tienes preguntas sobre la escalabilidad automática en Azure?'],
        'machine learning': ['Azure Machine Learning es un servicio de aprendizaje automático completamente administrado que te permite crear, entrenar e implementar modelos de aprendizaje automático en la nube. ¿Qué te gustaría saber sobre el aprendizaje automático en Azure?'],
        'kubernetes': ['Azure Kubernetes Service (AKS) te permite implementar, administrar y escalar contenedores de Docker de manera eficiente con orquestación de Kubernetes. ¿Necesitas información sobre Kubernetes en Azure?'],
        'coservación': ['Azure Conservation te ofrece herramientas y servicios para monitorear y optimizar el consumo de energía en tus aplicaciones y cargas de trabajo en la nube de Azure. ¿Tienes preguntas sobre la conservación de energía en Azure?'],
'iot': ['Azure IoT (Internet of Things) te permite conectar, monitorear y administrar dispositivos IoT de manera segura y escalable en la nube de Azure. ¿Qué te gustaría saber sobre IoT en Azure?'],
'seguridad': ['Azure Security Center te ofrece herramientas de seguridad integradas y servicios de inteligencia contra amenazas para proteger tus aplicaciones y datos en la nube de Azure. ¿Necesitas información sobre seguridad en Azure?'],
'gdpr': ['Azure cumple con el Reglamento General de Protección de Datos (GDPR) de la Unión Europea para proteger la privacidad y los derechos de los ciudadanos europeos en el procesamiento de datos personales. ¿Tienes preguntas sobre GDPR en Azure?'],
'certificaciones': ['Azure cuenta con una amplia gama de certificaciones de cumplimiento para garantizar que tus aplicaciones y datos cumplan con los estándares de seguridad y privacidad más exigentes. ¿Necesitas información sobre las certificaciones en Azure?'],
'monitorización': ['Azure Monitor te ofrece herramientas integradas para recopilar, analizar y actuar sobre los datos de telemetría de tus aplicaciones y servicios en la nube de Azure. ¿Tienes preguntas sobre la monitorización en Azure?'],
'integración continua': ['Azure DevOps te ofrece herramientas de integración continua (CI) para automatizar la compilación, las pruebas y la implementación de tus aplicaciones en la nube de Azure. ¿Necesitas información sobre la integración continua en Azure?'],
'servicios híbridos': ['Azure Arc te permite extender los servicios de Azure a cualquier infraestructura, incluidos los entornos locales, multicloud y perimetrales. ¿Qué te gustaría saber sobre los servicios híbridos en Azure?'],
'funciones': ['Azure Functions te permite ejecutar código sin servidor en respuesta a eventos en la nube de Azure. ¿Tienes preguntas sobre las funciones en Azure?'],
'blockchain': ['Azure Blockchain Service te permite crear, implementar y administrar redes de blockchain con facilidad en la nube de Azure. ¿Necesitas información sobre blockchain en Azure?'],
'paquete de servicios': ['Azure ofrece un paquete completo de servicios en la nube, que incluye cómputo, almacenamiento, redes, bases de datos, análisis, inteligencia artificial, IoT, seguridad y mucho más. ¿Qué te gustaría saber sobre el paquete de servicios de Azure?']
}
                        

    
    for keyword, response_options in responses.items():
        if keyword in message:
            # Se escoge respuesta de las opciones
            response = random.choice(response_options)
            return response

    # Si no se aproxima a la keyword, dice lo siguiente:
    return 'Lo siento, no entendí tu pregunta. ¿Puedes ser más específico o preguntar de otra manera?'

if __name__ == '__main__':
    app.run(debug=True)