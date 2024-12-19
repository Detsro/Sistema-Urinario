[![Open in MATLAB Online](https://www.mathworks.com/images/responsive/global/open-in-matlab-online.svg)](https://matlab.mathworks.com/open/github/v1?repo=Detsro/Sistema-Urinarioo)



# Sistema de Continencia Urinario

## Estudiantes
Alejandra Lizeth Meza Armenta 19212415
Marco Perez Chavez 19212423
Mauricio Jésus Meraz Galeana 18210139
Departamento de Ingeniería Eléctrica y Electrónica, Tecnológico Nacional de México/IT Tijuana, Blvd. Alberto Limón Padilla s/n, Tijuana, C.P. 22454, B.C., México. Email: correo1@tectijuana.edu.mx; correo2@tectijuana.edu.mx correo3@tectijuana.edu.mx

## Asignaturas o departmento donde se puede usar la Actividad
Modelado de Sistemas Fisiológicos de Ingeniería Biomédica

## Información general
El modelizado de sistemas fisiológicos es una herramienta importante en Ingeniería Biomédica, permite comprender el funcionamiento del cuerpo humano, así como diseñar y evaluar terapias y dispositivos médicos; se define como el proceso de formular modelos matemáticos o computacionales que representan el comportamiento y la interacción de los sistemas biológicos y fisiológicos. Esta asignatura pretende aportar al perfil del Ingeniero Biomédico la capacidad de realizar investigación científica en el área de Biología de Sistemas con la finalidad de dirigir y participar en equipos de trabajo interdisciplinarios en contextos nacionales e internacionales, así como de proporcionar soluciones informáticas para resolver problemas en el campo de la Ingeniería Biomédica con ética profesional; lo anterior al proporcionar al estudiante bases sólidas para modelizar sistemas y diseñar controladores para la solución de problemas en las áreas de atención médica y del sector industrial médico. La construcción de analogías entre circuitos eléctricos y sistemas fisiológicos para la formulación de modelos matemáticos y el diseño de controladores mediante la experimentación in silico brindan herramientas de gran aplicación en el quehacer profesional del Ingeniero Biomédico.

La asignatura de Modelado de Sistemas Fisiológicos forma parte del plan de estudios de la carrera en Ingeniería Biomédica con la siguiente competencia general del curso: Utiliza las propiedades de los circuitos RLC para describir la dinámica de sistemas fisiológicos, obtener modelos matemáticos y aplicar el control clásico, esto con el objetivo de integrar los principios de la Ingeniería de Control, la Electrónica Analógica y las Ciencias de la Computación con la Anatomía y Fisiología del cuerpo humano para proporcionar descripciones cuantitativas y cualitativas de sistemas fisiológicos complejos con el objetivo de modelizar, analizar, controlar, ilustrar y predecir su dinámica tanto en el corto como en el largo plazo.

## Objetivo general
Diseñar un gemelo digital de un sistema fisiológico que permita identificar las diferencias entre un paciente afectado por una enfermedad (caso) y un individuo saludable (control) para desarrollar un protocolo de tratamiento mediante un sistema de control en lazo cerrado.

## Descripción detallada del sistema
El sistema urinario se representa mediante un circuito eléctrico que modela dos escenarios: el caso 
afectado y el control normal. En el caso, se incluyen los componentes L1, R1, R2, R3, C1 y C2, que 
representan las características fisiológicas del sistema bajo condiciones alteradas, como la resistencia 
inicial al flujo y la capacidad de almacenamiento. Por otro lado, el control normal está compuesto por 
los elementos L2, R4, R5, R6, C3 y C4, que reflejan las condiciones fisiológicas normales, incluyendo 
la inercia al flujo sanguíneo y las obstrucciones uretrales moderadas.
En ambos escenarios, el sistema cuenta con una entrada representada por Ve(t), que es el volumen 
de orina en función del tiempo. Esta variable describe cómo varía la cantidad de orina generada en el 
tiempo y funciona como el estímulo que alimenta el sistema. Por su parte, la salida del sistema está 
representada por Vs(t), que corresponde a la presión vesical durante el vaciamiento, indicando la 
presión generada dentro de la vejiga al expulsar la orina.
Una señal rampa nos permite simular el proceso natural de carga y descarga que ocurre en el sistema urinario 
específicamente en la vejiga 
Este tipo de señal es útil para estudiar como el sistema responde a un incremento constante y sostenido de un 
estimo asi como el aumento gradual de presión o volumen. Observa como responde em términos de 
almacenamiento y regulación de flujo y vaciamento asi como comportamientos fisiologiocos.

## Referencias principales

[1] Stanford Children's Health. (n.d.). Anatomy of the urinary system [Online]. Available: [https://www.stanfordchildrens.org/es/topic/default?id=anatomy-of-the-urinary-system-85-P04568](https://www.stanfordchildrens.org/es/topic/default?id=anatomy-of-the-urinary-system-85-P04568)

[2] H. Motulsky, Intuitive biostatistics: a nonmathematical guide to statistical thinking. 4th ed. Oxford, New York, USA: Oxford University Press, 2014.

[3] P. A. Valle, L. N. Coria, C. Plata & Y. Salazar, “CAR-T cell therapy for the treatment of ALL: eradication conditions and in silico experimentation,” Hemato, vol. 2, issue 3, pp. 441-462, Jul 2021. https://doi.org/10.3390/hemato2030028 

[4] MathWorks. (n.d.). Sistemas Dinámicos [Online]. Available: https://www.mathworks.com/discovery/dynamic-systems.html

[5] Kenhub. (n.d.). Sistema urinario [Online]. Available: [https://www.kenhub.com/es/library/anatomia-es/sistema-urinario](https://www.kenhub.com/es/library/anatomia-es/sistema-urinario)


