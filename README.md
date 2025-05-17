	
# 🧮 Aplicación Web de Contador

Una aplicación web simple y escalable desarrollada con **Python**, **Flask** y **Docker**.  
Proporciona un contador básico con funcionalidades de **Sumar**, **Restar** y **Reiniciar** a través de una interfaz web limpia.

Este proyecto fue desarrollado como **proyecto final para la asignatura de Telemática**, enfocado en el despliegue con contenedores y conceptos de escalabilidad.

## ✨ Características

- Interfaz web responsiva con un diseño limpio.
- Operaciones del contador: ➕ Sumar, ➖ Restar, 🔄 Reiniciar.
- Construido utilizando **Python** y **Flask**.
- Empaquetado en un **contenedor Docker**.
- Desplegable en cualquier entorno que soporte Docker.

## 🛠️ Requisitos Previos

- Tener **Docker** instalado en la máquina.
- Tener el **puerto 3000** abierto en el servidor o equipo local.

## 🚀 Instrucciones de Despliegue

### 1. Clonar el Repositorio
```bash
cd <carpeta-del-repositorio>
git clone https://github.com/samuel-boteroa/docker-web-counter
```

### 2. Construir la Imagen de Docker
```bash
docker build . -t webcounter 
```

### 3. Ejecutar el Contenedor
```bash
docker run -d -p 3000:3000 webcounter
```


## 🏗️ Estructura del Proyecto

```
.
├── main.py         # Aplicación web en Flask con la lógica del contador
├── Dockerfile      # Instrucciones para la creación del contenedor
└── README.md       # Documentación del proyecto (este archivo)
```

## 👤 Autor

- Samuel Botero ALzate

## 📄 Licencia

Este proyecto es de uso educativo como parte del **Proyecto Final de la Asignatura de Telemática**.
