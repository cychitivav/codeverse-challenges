# Angular 

## Angular CLI installation
Es necesario tener node.js con la versión LTS (Long Term Support) instalada.

Para instalar el cliente globla de Angular primero se verifica la versión de node.js y el instalador de paquetes de npm.

```bash
node -v
npm -v
```

Luego, se instala el cliente global de Angular:

```bash
npm i -g @angular/cli
```

Con `ng version` se sabe si angular se instaló correctamente y la versión descargada.


### Mi primer proyecto Angular

```bash
ng new <name>
```


* `ng serve`: `-o` to open browser or `--port=<num>` to specify port
* `ng version`: in the folder of a project, shows the version of angular and the dependencies<>
