
# :computer: Simulador de Máquina de Turing

<p align="justify">O código desenvolvido executa uma máquina de turing determinística padrão que calcula funções numéricas.
Para isso, é necessário utilizar um arquivo texto que contenha as informações da máquina no seguinte formato:</p>

```bash
(
conjunto de estados,
alfabeto de entrada,
alfabeto de fita,
{
funções de transição
-
-
-
...
}
Estado inicial
)
fita
```

## :bookmark_tabs: Descrição

1. O estado inicial deve ser sempre 'q0';

2. A fita, deve sempre começar com 'B' e terminar com símbolos 'B' suficientes para realizar as transições.

<p align="justify">Como forma de exemplo existem os arquivos entrada.txt e entrada2.txt que correspondem respectivamente à uma máquina 
que realiza soma de dois números e uma máquina que copia o argumento da fita.
Qualquer outro exemplo a ser testado deve seguir os padrões anteriores.</p>


## :video_game: Como executar

Para sua execução, digite o seguinte comando:

```bash
python TM_Simulator.py argumento1 argumento2
```
- Sendo argumento1, o arquivo de entrada com extensão .txt que contém a máquina a ser simulada;
- Sendo argumento2, o o arquivo de de saída com extensão .txt que gravará as configurações da fita.

## :closed_lock_with_key: Licença

Este projeto está sob a licença do MIT. Consulte a [LICENÇA](./LICENSE) para obter mais informações.
