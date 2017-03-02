# Librería subprocces y sus maravillas

Desde ya un buen tiempo la fundación Python lleva recomendando el uso de la librería subprocess sobre la librería os, actualmente deprecada, para tratar la gestión y administración del sistem.

El módulo subprocess nos permite ejecutar procesos, conectarlos en pipes de STDIN / STDOUT / ERR, y obtener sus códigos de retorno.

Trata de reemplazar funciones del módulo os como os.system, os.spawn, os.popen...

# subprocess.run()

`subprocess.run(args, *, stdin=None, input=None, stdout=None, stderr=None, shell=False, timeout=None, check=False, encoding=None, errors=None)`

Corre el comando descrito en los argumentos, y retorna una instancia de CompletedProcess, representando que esta ha terminado.

**No captura STDOUT o STDERR por defecto, para hacerlo se pasa PIPE en el argumento stdout y/o argumentos stderr**

`timeout` se le pasa a Popen.communicate(), y si este expira el proceso hijo será matado.

`input` se le pasa a Popen.communicate() y devuelve el STDIN del subproceso. Si se especifican el `encoding`, o `errors`, o `universal_newlines` es True, se crea automáticamente el pipe y no se usa el argumento `stdin`.

`check` levanta excepción si devuelve 1.


```
subprocess.run('ls', '-l')
```


```
subprocess.run('cat', '/etc/environment')
```


```
subprocess.run("exit 1", shell=True, check=True)
```


----------------------------------------------------------------------------------

# **Antigua API de alto nivel**

# subprocess.call()

`subprocess.call(args, *, stdin=None, stdout=None, stderr=None, shell=False, timeout=None)`

### CHANGELOG:

* Desde la versión 3.5 se encuentra en desuso en favor subprocess.run()
* En la versión 3.3 se añade timeout(tiempo de espera) como argumento

Corre el comando descrito en los argumentos, espera a que este se complete y retorna el atributo returncode.

A partir de la versión 3.5 sería equivalente a ```run(...).returncode```

Tenemos dos formas de usarlo.

* Método 1 
  - 
  ```
  subprocess.call('lsusb', '-d')
  ```

+ Método 2

  De este modo, pasándole la ejecución directamente al Shell, se permite aprovechar todas las características de este último, sin embargo puede causar una falla de seguridad al tomar input insanitizado de una fuente no fiable y dejar el programa vulnerable a ataques de shell injection. No se recomienda su uso.
+ ```
    subprocess.call('ls', '-l', shell=True)
    ```

No se debería utilizar stdout=PIPE o stderr=PIPE ya que los procesos hijos se bloquearán si hay un output excesivo para el buffer. Por esto se añadió el timeout en la versión 3.3.


# subprocess.check_call()

`subprocess.check_call(args, *, stdin=None, stdout=None, stderr=None, shell=False, timeout=None)`

Corre el comando descrito en los argumentos, espera a que este se complete y retorna el estado de la ejecución. Si el código de retorno es 1, se levanta excepción de llamada a proceso, `CalledProcessError`, que traerá el atributo `returncode`.

A partir de la versión 3.5 sería equivalente a ```run(..., check=True)```

Por el resto funciona exactamente igual que `subprocess.call()`

# subprocess.check_output()

### CHANGELOG

* Se añade en la versión 3.1
* En la versión 3.3 se añade timeout(tiempo de espera) como argumento
* En la 3.4 se añade soporte para el argumento *input*

`subprocess.check_output(args, *, stdin=None, stderr=None, shell=False, encoding=None, errors=None, universal_newlines=False, timeout=None)`

Corre el comando descrito en los argumentos, y retorna su salida. Si el código de retorno es 1, se levanta excepción de llamada a proceso, `CalledProcessError`, que traerá los atributos `returncode` y `output`, que contendrá cualquier salida.

Es equivalente a `run(..., check=True, stdout=PIPE).stdout`.

También se puede capturar el error en el resultado usando `stderr=subprocess.STDOUT`.
