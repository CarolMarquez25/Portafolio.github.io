    Plantilla de una página para estudio de diseño - ARCHIVADO
Plantilla de sitio web plana y responsiva, diseñada por cssauthor y codificada por Maxim Orlov .

Demostración: http://website-templates.github.io/design-studio_one-page-template

Demostración de maqueta Maqueta de producto creada con http://frame.lab25.co.uk/

Contenido
Estructura de carpetas y archivos
Requisitos:
Configuración del editor
Cómo empezar
Configuración del sitio
Tareas
Limpieza
Desarrollador
Construir
Reconstruir
Servidor
Duende
Recarga en vivo
Licencia
Estructura de carpetas y archivos
./
├── .editorconfig
├── gulpfile.js
├── package.json
├── README.md
|
├── gulp_tasks/                                * gulp tasks
|   ├── config/                                * gulp tasks config
│   |   ├── paths.js
│   |   └── aliases.js
│   |
|   └── task.js
|
├── screenshots/                               * responsive test screenshots
|
├── dev/                                       * site source
│   ├── images/                                * image sources
|   │
│   ├── pug/                                   * templates
|   |   ├── blocks/                            * blocks library
|   │   |   └── block.pug
|   │   ├── helpers/                           * helper mixins
|   │   ├── vendor/                            * third-party code
|   │   ├── layouts/                           * page layouts
|   │   └── pages/                             * main pages templates
|   │
│   ├── js/                                    * source js
|   |   ├── vendor/                            * vendor scripts library
|   |   ├── lib/                               * site scripts library
|   │   ├── head.js                            * head scripts
|   │   └── body.js                            * body scripts
|   │
|   ├── sass/                                  * sass preprocessor styles
|   |   ├── blocks/                            * blocks library
|   │   |   └── block.sass
|   │   ├── helpers/                           * mixins and vars
|   │   ├── vendor/                            * third-party code
|   │   ├── custom.sass
|   │   ├── noscript.sass
|   │   └── screen.sass
|   │
│   ├── helpers/                               * helper files
|   |   ├── favicon.ico
|   |   └── .htaccess
|   │
│   ├── fonts/                                 * font sources
|   │
│   └── data/                                  * configs and data for templates
│
└── build/                                     * built source
    ├── index.html
    ├── page.html
    |
    └── static/                                * static assets
        ├── css/                               * minified styles
        |
        ├── images/                            * minified images
        │
        ├── js/                                * minified assembled js
        |
        └── fonts/                             * @font-face-ready webfonts

Requisitos
Node.js
Sistema de construcción: Grunt o Gulp
Opcionalmente:
Configuración del editor
Configuración del editor
Este proyecto tiene un archivo .editorconfig en la raíz. Describe el estilo de sangría, los espacios finales, etc. Ver más detalles aquí.

Cómo empezar
Si no has usado Gulp antes, asegúrate de consultar la guía de introducción y también estas recetas .

Antes de comenzar es necesario tener instalado npm , así como gulp globalmente.

Algunos pasos sencillos para empezar:

Instale las dependencias package.jsonejecutando: npm install.
¡Ejecute tareas de la lista a continuación y comience el desarrollo!
Editar la configuración general en la sección dev/data/config.jsonVer configuración del sitio
Configuración del sitio
Este código repetitivo utiliza plantillas Pug con configuraciones de datos externas. La configuración principal se encuentra en dev/data/config.jsonel archivo. Y está disponible para su uso en plantillas conconfig.key-name

Tareas
Aquí vienen grupos de tareas de gulp con algunas explicaciones.

Limpieza
Eliminar marcadores de posición de los directorios de trabajo. Gulp:gulp cleanup

Eliminar archivos de gitkeep
Desarrollador
Tarea de desarrollo con servidor estático. Gulp:gulp dev

Paquete de javascripts
Compilar hojas de estilo Sass
Agregar prefijos de proveedores en CSS
Combinar consultas de medios en archivos CSS
Compilar plantillas de Pug
Ayudantes de sincronización y otros recursos
Sincronizar imágenes
Ejecute el servidor estático BrowserSync con recarga en vivo usando
Esté atento a los cambios y ejecute la tarea de desarrollo
Construir
Tarea de construcción. ¡Gulp!gulp build

Minimizar imágenes
Minificar archivos javascript
Minimizar hojas de estilo
Minificar HTML
Ejecutar el servidor estático de BrowserSync
Reconstruir
Regenerar y compilar el proyecto ejecutando todas las tareas. Gulp:gulp rebuild

Paquete de javascripts
Compilar hojas de estilo Sass
Agregar prefijos de proveedores en CSS
Combinar consultas de medios en archivos CSS
Compilar plantillas de Pug
Ayudantes de sincronización y otros recursos
Sincronizar imágenes
Minimizar imágenes
Minificar archivos javascript
Minimizar hojas de estilo
Minificar HTML
Servidor
Ejecuta el servidor sin estar pendiente de los cambios. Gulp:gulp server

Ejecutar el servidor estático de BrowserSync
Recarga en vivo
Este proyecto utiliza BrowserSync como servidor estático con la opción de recarga en vivo habilitada y configurada.

Licencia
Instituto Tecnológico de Massachusetts (MIT)

