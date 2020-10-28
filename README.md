

# Game-CG
Desarrollar un proyecto utilizando los materiales de la clase
# Dependencias:
 *Python 3.8.6
 *Pygame 1.9.3
 *PyOPENGL 3.1.5

### Datos Academicos 📚📓

- **Institucion:** Universidad Nacional de San Antonio Abad del Cusco
- **Facultad:** Facultad de ingenieria electrica, electronica, informatica y mecanica
- **Escuela Profesional:** Ingenieria Informatica y de Sistemas

### PROYECTO: DESARROLLO DE UN JUEGO EN 2D - PROYECTO FINAL DE COMPUTACION GRAFICA

**CURSO:** Computación Grafica I

**DOCENTE:*** Quintanilla Portugal,Roxana Lisette - _Docente_ - [Concytec](http://directorio.concytec.gob.pe/appDirectorioCTI/VerDatosInvestigador.do?id_investigador=40930).

**ESTUDIANTES:** 
- **Inca Cruz, Carlos Eduardo** - _GitHub Account_ - [CarlosEdu322](https://github.com/CarlosEdu322)
- **Huancara Ccolqque, Alex Helder** - _GitHub Account_ - [AlexHelder-Tyzer](https://github.com/AlexHelder-Tyzer)
- **Ttito Saya, Alexander** - _GitHub Account_ - [AlexanderTS1](https://github.com/AlexanderTS1)

**OBJETIVOS:**

- Utilizar los conceptos basicos y avanzados del curso relacionados con graficas en 2D
- Utilizar las librerias implementadas en el laboratorio de Computacion grafica

**DESARROLLO DEL PROYECTO:**

**1. IDEA DEL JUEGO:** 
- El juego consiste en una lucha de supervivencia entre dos bandos (Player VS PC); el player tendra un avatar("un soldado") quien hará uso de arma de fuego para disparar al oponente(run and gone), cuando el player gana pasa al siguiente nivel enfrentandose a enemigos mas peligrosos,¿cómo sabemos si hemos ganado el nivel?. El Soldado tanto el oponente cuenta con una barra de vida que va disminuyendo cuando los sujestos son impactados por el proyectil; si la barra de vida del oponente queda vacia hemos logrado pasado el nivel caso contrario perdimos el juego.El juego contará con tres niveles y cada enemigo te atacará con sus crias.

Al implementar el juego se utilizará los algoritmos implementados en el laboratorio del curso tales como generar canvas,generar  lineas utilizando algoritmo DDA, transformaciones en 2D(traslación, rotación, escalamiento y reflexión)

**2. DESCRIPCIÓN BÁSICA DEL JUEGO**
- Se tendrán 2 lados por bando(el lado izquierdo del player y el lado derecho el player)
- El player con su avatar("un soldado") disparará las municiones al oponente(no dispara nada, ataca con sus crias).
- Se pasa de nivel cuando la barra de vida del oponente queda vacío
- El juego termina cuando la barra del soldado queda vacío

**3. DESAROLLO DEL CODIGO**
- Herramienta a utilizar Python 3.8.6 con librerias(Pygame 1.9.3,PyOPENGL 3.1.5) https://www.python.org/
- Se grafica y pinta el personaje utilizando matrices(Librería numpy de Paython) https://pypi.org/project/numpy/
- El fondo es una matriz  que tiene el mismo tamaño del display 
- Se utiliza los eventos del pygame https://pypi.org/project/pygame/
