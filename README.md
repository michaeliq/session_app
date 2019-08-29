# session_app

Session app

La siguiente descripción enumera las caracteristicas de la app y los recursos que se deben instalar
en el servidor para su correcto despliegue. Session es una app que posee las caracteristicas propias de
una Api para el registro, modificación, eliminación y seleccion de información mediante consultas a 
la base de datos. Se utilizo el lenguaje python en su versión 3 para la creación del backend y el Framework-light
Flask para la construcción y el manejo de las peticiones Web, ademas de librerias de python tales como
request, render_template, redirect, entre otros.

A continuación se expone la estructura del back-end:

creación de rutas:
Login : esta ruta permite la autenticación del usuario y ofrece verificar el
acceso a las funciones de la Api. Para esta ruta se usa la libreria request
la cual trae los datos del formulario en pagina de login. Dichos datos son
comparados con los datos del servidor usando la libreria bcrypt para desencriptar
la contraseña en ambos lados de la app. Por ultimo se regresa una respuesta en 
formato html para dar la bienvenida al usuario y mostrar los datos registrados
hasta el momento. Dicha respuesta aprovecha la libreria redirect para servir
una pagina web html con codigo python embebido.
Se manejan variables que capturan datos como: correo, password.
Tambien se crea un objeto conexión que permite manipular y hacer consultas
a base de datos mysql.
Esta ruta dara dos posibles respuestas gracias a una condición:
Da acceso al usuario o le indica que los datos estan erroneos y debe verificar.


Logout: esta ruta permite destruir los datos en la variable de sesión y servir
la pagina de autenticación de usuario.


Sigin: en esta ruta podemos registrar los usuarios proporcionando un nombre,
correo, contraseña.Luego se prepara una instancia del objeto mysql para preparar
la consulta, la contraseña se pasa a través del metodo bcrypt para crear una
cadena de caracteres la cual se guardara en la base de datos.Y luego a traves 
de flask enviamos una respuesta al usuario y servimos la pagina de bienvenida al
usuario.

Update: a través de esta ruta se carga una pagina que facilita cambiar los datos
de un registro en la base de datos. Al seleccionar uno de los registros se envia
una petición al servidor y este devuelve los datos del registro. En esta pagina
se enviaran los datos a través de la ruta Up_usu

Up_usu: En esta ruta se envia los datos que seran cambiados del registro seleccionado.
Primero se comprueba el metodo a traves del cual fueron enviado los datos, luego
se instancian los datos suministrados por el usuario y si es preciso el cambio de
la contraseña se usa la libreria bcrypt para encriptar la contraseña. Se crear un
objeto de consulta mysql y se prepara la consulta de actualización. Por ultimo se
envia un mensaje al usuario y junto con la pagina de inicio donde se evidencian
los datos modificados.

Index: el metodo index facilita mostrar los usuarios en la pagina principal.
cuando se despliega la aplicación luego de autenticar al usuario se sirven los
registros guardados. Se crea una instancia del objeto mysql y luego se
prepara la consulta y se sirve la pagina de inicio html.

Delete: esta ruta facilita la eliminación de un registro. Primero se selecciona
el registro en cuestion y luego se crea una instancia del objeto mysql. Se prepara
la consulta de eliminación sql y se ejecuta. Si es exitoso se envia el mensaje
con el registro eliminado y se sirve la pagina de inicio para mostrar los cambios
realizados.

Configuraciones:
Se debe señalar el nombre de usuario, el nombre del host, la contraseña y el nombre
de la base de datos. 
Para el bcrypt se usa el metodo bcrypt.gensalt() con el cual se prepara la contraseña
que encripta la clave proporcionada por los usuarios.

Por ultimo se despliega el servidor con el metodo flask.run y se puede facilitar
un puerto para acceder y otras opciones para desarrollo.
