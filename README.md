# RepasoObjetos-Catalogo
Universidad Distrital Francisco Jose de Paula Santander

Especialidad en Ingeniería de Software

Informatica 1

#Juan Sebastian Vega Guarin

#Principios SOLID

#Principio de Responsabilidad Única
Las clases que fueron desarrolladas tiene una única responsabilidad, la línea de funcionamiento es un proceso simple de información de acuerdo a una función ramdon para seleccionar Orcos o Humanos, en este proceso las clases se dedican especialmente a mostrar la infomación e imagen solicitada por la función.

#Principio Abierto/Cerrado
Podemos evidenciar este principio dentro de nuestro código pues las clases que hemos construido se encuentran abiertos para su extensión, pero se encuentran cerrados para la modificación, dentro de nuestro código podemos evidenciar como extendemos las funcionalidades para crear nuevos “productos” pero en ningún momento modificamos o alteramos los parámetros y atributos de la clase padre.

#Principio de substitución de Liskov
Gracias a la herencia que hemos construido dentro de nuestro código y la línea de desarrollado que hemos generado, podemos evidenciar el uso de superclases y subclases y el funcionamiento entre ellas cumple con el principio de sustituir una subclase por una super clase sin afectar el funcionamiento.

#DRY
Nuestra aplicación por ahora es bastante precisa y pequeña en su envergadura, las clases que poseemos se comunican con las directamente cercanas, lo que nos ayuda a encontrar fácilmente las funcionalidades que necesitamos llamar desde otros lados del código y hacer uso de buenas prácticas entre las clases expuestas.

#KISS
La aplicación que hemos diseñado mantiene simple la funcionalidad de sus componentes, mantiene un llamado preciso y exacto de las funciones que hemos diseñado para cumplir con el resultado esperado, funciones fáciles de entender para el desarrollador y una lógica que cumple con paramétricas para poder agregar o modificar determinadas funcionalidades.


#Patrones de Diseño

#Versión 1 del codigo

#Abstrac factory: 
En nuestra aplicación poseemos una “Fabrica” general con unos métodos determinados los cuales son precisos en sus funciones, esta Fabrica genérica la implementan dos fabricas especificas para “Orcas” o “Humanos” las cuales y nos refieren acciones más puntuales sobre mi código dependiendo el tipo de objeto.

#Facade: 
Proporciona en nuestro código una interfaz unificada para un conjunto de interfaces que implementa de ella dentro de nuestro subsistema. Definiendo una interfaz de alto nivel “Fabrica” facilitando el uso de nuestras funcionalidades en nuestros subsistemas “Orcos” o “Humanos”.

#Version 2 del codigo

#Bridge:
Por medio de este patron podemos implementar muchas más funcionalidades dentro de nuestro código, representando en un abstracción llamada "Producto" podemos diseñar más implementadores de estas caracteristicas sin alterar nuestro flujo inicial y sin llegar a alterar al cliente de la aplicación.

![image](https://user-images.githubusercontent.com/12587275/115155769-eda37700-a046-11eb-962d-929dc57cd222.png)


Endpoint:

GET: http://127.0.0.1:5000/v1


![image](https://user-images.githubusercontent.com/12587275/115159319-344d9d00-a058-11eb-8e17-f72ad4454cef.png)


GET: http://127.0.0.1:5000/v2


![image](https://user-images.githubusercontent.com/12587275/115159338-46c7d680-a058-11eb-9cc2-350bb55c0334.png)

