# Game-CG
Desarrollar un proyecto utilizando los materiales de la clase


DESARROLLO DE UN JUEGO EN 2D - PROYECTO FINAL DE COMPUTACION GRAFICA

OBJETIVOS:

- Utilizar los conceptos basicos avanzados del curso
- Utilizar las librerias implementadas en el laboratorio de Computacion grafica

DESARROLLO DEL PROYECTOS:

1. IDEA DEL JUEGO: 
- El juego consiste en una lucha armado entre dos bandos (Player VS PC); el player tendra un avatar(personaje en 2D +"un soldado") quien hará uso de arma de fuego para disparar al oponente mientras el oponente sea impactado por una cierta cantidad de muniones el oponente girará 45 grados , despues el oponente gira 90 grados el cual significa perdida de su nave y muerte, entonces la nave perdida se traslada al territorio del player (el territorio del player es un poligono y el oponente montado en su nave se mueve de forma predeterminada. Al implementar el juego se utilizará los algoritmos implementados en el laboratorio del curso tales como generar canvas,dibujar poligono, rellenar poligono , transformaciones en 2D(traslación,rotación y reflexión) anexado en codigo utils.py

2. DESCRIPCIÓN BÁSICA DEL JUEGO
- Se tendrán 2 lados por bando(el lado izquierdo del player y el lado derecho el player)
- El player con su avatar(personaje en 2D +"un soldado") disparará las municiones al oponente(no dispara nada) que se va mover de abajo hacia arriba y viceversa
4 impactos de bala hará que el oponente gire 45 grados
- 8 impactos de bala hara que el oponente gire 90 grados, caso que significará la muerte del oponente y exapropiacion de la nave que sera trasladado al terreno del player
- El juego termina cuando el player gana 5 naves.
