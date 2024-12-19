[![Open in MATLAB Online](https://www.mathworks.com/images/responsive/global/open-in-matlab-online.svg)](https://matlab.mathworks.com/open/github/v1?repo=Detsro/Sistema-Urinarioo)




# Sistema de Continencia Urinario

## Estudiantes
Alejandra Lizeth Meza Armenta 19212415  
Marco Pérez Chávez 19212423  
Mauricio Jesús Meraz Galeana 18210139  
Departamento de Ingeniería Eléctrica y Electrónica, Tecnológico Nacional de México/IT Tijuana, Blvd. Alberto Limón Padilla s/n, Tijuana, C.P. 22454, B.C., México. Email: correo1@tectijuana.edu.mx; correo2@tectijuana.edu.mx; correo3@tectijuana.edu.mx

## Asignaturas o departamento donde se puede usar la actividad
Modelado de Sistemas Fisiológicos de Ingeniería Biomédica

## Información general
El modelado de sistemas fisiológicos es una herramienta importante en Ingeniería Biomédica que permite comprender el funcionamiento del cuerpo humano, así como diseñar y evaluar terapias y dispositivos médicos. Se define como el proceso de formular modelos matemáticos o computacionales que representan el comportamiento y la interacción de los sistemas biológicos y fisiológicos.  

Esta asignatura aporta al perfil del Ingeniero Biomédico la capacidad de realizar investigación científica en el área de Biología de Sistemas, con la finalidad de dirigir y participar en equipos de trabajo interdisciplinarios en contextos nacionales e internacionales. Asimismo, busca proporcionar soluciones informáticas para resolver problemas en el campo de la Ingeniería Biomédica con ética profesional. Esto se logra proporcionando al estudiante bases sólidas para modelar sistemas y diseñar controladores destinados a resolver problemas en las áreas de atención médica y del sector industrial médico.  

La construcción de analogías entre circuitos eléctricos y sistemas fisiológicos para la formulación de modelos matemáticos y el diseño de controladores mediante la experimentación *in silico* brinda herramientas de gran aplicación en el quehacer profesional del Ingeniero Biomédico.  

La asignatura de Modelado de Sistemas Fisiológicos forma parte del plan de estudios de la carrera de Ingeniería Biomédica y tiene como competencia general del curso: **Utilizar las propiedades de los circuitos RLC para describir la dinámica de sistemas fisiológicos, obtener modelos matemáticos y aplicar el control clásico.** Esto tiene como objetivo integrar los principios de la Ingeniería de Control, la Electrónica Analógica y las Ciencias de la Computación con la Anatomía y Fisiología del cuerpo humano, proporcionando descripciones cuantitativas y cualitativas de sistemas fisiológicos complejos. La meta es modelar, analizar, controlar, ilustrar y predecir su dinámica tanto en el corto como en el largo plazo.

## Objetivo general
Diseñar un gemelo digital de un sistema fisiológico que permita identificar las diferencias entre un paciente afectado por una enfermedad (caso) y un individuo saludable (control), para desarrollar un protocolo de tratamiento mediante un sistema de control en lazo cerrado.

## Descripción detallada del sistema
El sistema urinario se representa mediante un circuito eléctrico que modela dos escenarios: el caso afectado y el control normal.  

En el **caso afectado**, se incluyen los componentes L1, R1, R2, R3, C1 y C2, que representan las características fisiológicas del sistema bajo condiciones alteradas, como la resistencia inicial al flujo y la capacidad de almacenamiento.  

En el **control normal**, el sistema está compuesto por los elementos L2, R4, R5, R6, C3 y C4, que reflejan las condiciones fisiológicas normales, incluyendo la inercia al flujo sanguíneo y las obstrucciones uretrales moderadas.  

En ambos escenarios, el sistema cuenta con una entrada representada por Ve(t), que es el volumen de orina en función del tiempo. Esta variable describe cómo varía la cantidad de orina generada con el tiempo y funciona como el estímulo que alimenta el sistema. Por otro lado, la salida del sistema está representada por Vs(t), que corresponde a la presión vesical durante el vaciamiento, indicando la presión generada dentro de la vejiga al expulsar la orina.  

Una señal rampa permite simular el proceso natural de carga y descarga que ocurre en el sistema urinario, específicamente en la vejiga. Este tipo de señal es útil para estudiar cómo el sistema responde a un incremento constante y sostenido de un estímulo, así como al aumento gradual de presión o volumen. Esto permite observar cómo responde el sistema en términos de almacenamiento, regulación del flujo y vaciamiento, así como en comportamientos fisiológicos.

## Referencias principales

[1] Stanford Children's Health. (n.d.). Anatomy of the urinary system [Online]. Available: [https://www.stanfordchildrens.org/es/topic/default?id=anatomy-of-the-urinary-system-85-P04568](https://www.stanfordchildrens.org/es/topic/default?id=anatomy-of-the-urinary-system-85-P04568)  
.
[2] Kenhub. (n.d.). Sistema urinario [Online]. Available: [https://www.kenhub.com/es/library/anatomia-es/sistema-urinario](https://www.kenhub.com/es/library/anatomia-es/sistema-urinario)




