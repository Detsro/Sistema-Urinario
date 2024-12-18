# -*- coding: utf-8 -*-
"""
Created on Mon Dec 16 15:30:33 2024

@author: Marco
"""

import numpy as np
import matplotlib.pyplot as plt
import control
from scipy import signal  # Importar para la señal triangular

# Configuración de tiempo
t0, tF, dt = 0, 10, 1E-2  # Configuración del tiempo inicial, final y el paso
N = round((tF - t0) / dt) + 1
t = np.linspace(t0, tF, N)  # Vector de tiempo

# Señal de entrada (señal triangular)
frecuencia = 0.1  # Frecuencia de la señal triangular en Hz
u1 = (signal.sawtooth(2 * np.pi * frecuencia * t, width=0.9)+1)/2  # Señal triangular

# Elementos del circuito Caso
L1 = 1E-6  # Inductancia en henrios
R1 = 0.3  # Resistencia en ohmios
R2 = 0.3
R3 = 0.3
C1 = 0.9  # Capacitancia en faradios
C2 = 0.9

# Elementos del circuito Control
L2 = 2E-6  # Inductancia en henrios
R4 = 0.6  # Resistencia en ohmios
R5 = 0.3
R6 = 0.3
C3 = 1  # Capacitancia en faradios
C4 = 1.9

# Función de transferencia Caso
a1 = C1 * C2 * L1 * R2 + C1 * C2 * L1 * R3
b1 = C1 * L1 + C2 * L1 + C1 * C2 * R1 * R2 + C1 * C2 * R1 * R3 + C1 * C2 * R2 * R3
c1 = C1 * R1 + C2 * R1 + C2 * R3 + C1 * R2
d1 = 1
num1 = [C1 * R2, 1]  # Numerador de la función de transferencia del Caso
den1 = [a1, b1, c1, d1]  # Denominador de la función de transferencia del Caso
sys1 = control.tf(num1, den1)

# Función de transferencia Control
a2 = C3 * C4 * L2 * R5 + C3 * C4 * L2 * R6
b2 = C3 * L2 + C4 * L2 + C3 * C4 * R4 * R5 + C3 * C4 * R4 * R6 + C3 * C4 * R5 * R6
c2 = C3 * R4 + C4 * R4 + C4 * R6 + C3 * R5
d2 = 1
num2 = [C3 * R5, 1]  # Numerador de la función de transferencia del Control
den2 = [a2, b2, c2, d2]  # Denominador de la función de transferencia del Control
sys2 = control.tf(num2, den2)

# Imprimir funciones de transferencia
print("Función de transferencia del Caso:")
print(sys1)
print("\nFunción de transferencia del Control:")
print(sys2)

# Respuesta del sistema para "Caso"
response_caso = control.forced_response(sys2, t, u1)
salida_caso = response_caso[1]  # Salida del sistema para el Caso

# Respuesta del sistema para "Control"
response_control = control.forced_response(sys1, t, u1)
salida_control = response_control[1]  # Salida del sistema para el Control

# Crear la gráfica
plt.figure(figsize=(10, 6))

# Graficar entrada
plt.plot(t, u1, '-', color='red', label='Entrada ($V_{entrada}$)', linewidth=1.5)

# Graficar salida caso
plt.plot(t, salida_caso, '-', color='green', label='Caso ($V_{Caso}$)', linewidth=1.5)

# Graficar salida control
plt.plot(t, salida_control, '-', color='blue', label='Control ($V_{Control}$)', linewidth=1.5)

# Graficar salida tratamiento
plt.plot(t, salida_control, '--', color='yellow', label='Tratamiento ($V_{Tratamiento}$)', linewidth=1.5)

# Configuración de la gráfica
plt.grid(True, linestyle='--', linewidth=0.5)
plt.xlim(0, 10)
plt.ylim(0, 1.5)  # Ajustar los límites del eje Y para reflejar mejor las curvas
plt.xlabel('Tiempo (s)', fontsize=12)
plt.ylabel('Voltaje (V)', fontsize=12)
plt.title('Sistema Urinario', fontsize=14)
plt.legend(loc='best', fontsize=10)

# Guardar la gráfica como imagen
plt.savefig('sistema_urinario.png', dpi=300, bbox_inches='tight')
plt.show()
