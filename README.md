# Projecto eCommerce con Django
Presenta Juliho Castillo

El código del proyecto se encuentra en la carpeta `eCommerce`. Para cada entrega se creará una rama diferente del repositorio:

| Módulo | Tema | URL |
| ------ | ---- | --- |
| 14 | Fundamentos de Linux e Introducción a Django | https://github.com/julihocc/ebac-python-backend/tree/Fundamentos-de-Linux-e-Introducci%C3%B3n-a-Django%E2%80%9D |

A continuación se detalla el trabajo realizado en cada entrega. 

### Fundamentos de Linux e introducción a Django

Hemos iniciado exitosamente un proyecto Django y mostrado `cart.checkout()` en el frontend, siguiendo estos pasos:

1. Configuramos un nuevo proyecto Django y una aplicación llamada `store`.
2. Creamos modelos `Product` y `Cart`, basados en clases Python proporcionadas, e integrándolos a nuestra aplicación Django.
3. Implementamos una vista, `checkout_view`, para manejar el proceso de compra, incluyendo la creación o recuperación de un carrito, añadiendo productos para demostración, y preparando un mensaje con el total de la compra.
4. Configuramos patrones de URL para dirigir las solicitudes a la vista de compra y aseguramos que el proyecto reconociera correctamente la aplicación `store`.
5. Resolvimos problemas relacionados con la aplicación `store` no siendo reconocida, configuraciones erróneas de URL, y manejamos errores `NoneType` asegurando la existencia de una instancia de carrito antes de intentar operaciones sobre ella.
6. Modificamos la vista de compra para añadir un producto al carrito con fines demostrativos, logrando así mostrar con éxito el mensaje de compra en el frontend.

**Para acceder a la vista:**
- **Inicia el servidor de desarrollo Django:** En tu directorio de proyecto, ejecuta `python manage.py runserver`. Este comando inicia un servidor web local.
- **Accede a la Vista:** Abre un navegador web y navega a `http://127.0.0.1:8000/store/checkout/` para acceder a la vista de compra. Si seguiste los pasos correctamente, deberías ver el mensaje de compra en tu navegador.