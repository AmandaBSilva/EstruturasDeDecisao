Seja `cond` uma condição lógica, que pode resultar em verdadeiro ou falso. Uma estrutura condicional pode ser construída da seguinte maneira:

```python
if (cond):
    comandos caso cond seja verdadeira
else:
    comandos caso cond seja falsa
```

Caso existam 2 condições, `cond1` e `cond2`, onde `cond2` deve ser avaliada caso `cond1` não seja verdade, a estrutura obedece o seguinte formato:

```python
if (cond2):
    comandos caso cond1 seja verdadeira
elif (cond2):
    comando caso cond2 seja verdadeira e cond1 falsa
else:
    comandos caso cond1 e cond2 sejam falsas
```
