# 🖼️ Conversor de Formato de Imagem

Um script Python simples e eficiente para converter imagens em lote de formatos como `.png` e `.webp` para `.jpg`, otimizando o espaço de armazenamento e garantindo compatibilidade.

## ❔ Por que usar?

Muitas vezes, você possui imagens em formatos de alta qualidade ou com transparência (como `.png` ou `.webp`), mas precisa delas em formato `.jpg` para:
* **Economizar espaço:** O formato `.jpg` geralmente oferece uma compressão muito maior.
* **Compatibilidade:** Algumas plataformas ou sistemas mais antigos só aceitam o formato `.jpg`.
* **Remover transparência:** Converter de `RGBA` (com transparência) para `RGB` (sem transparência).

Este script automatiza esse processo para pastas inteiras de uma só vez.

## ✨ Recursos

* Converte múltiplos formatos de entrada (`.png`, `.webp` por padrão).
* Salva em um formato de saída configurável (`.jpg` por padrão).
* Processa todas as imagens de uma pasta `entrada` e as salva em uma pasta `saida`.
* Preserva os nomes de arquivo originais.
* **Lida corretamente com transparência:** Converte imagens `RGBA` para `RGB` antes de salvar como `.jpg`, evitando erros.
* Permite configurar o nível de **qualidade** da compressão `.jpg`.

## 🚀 Começando

Siga estas instruções para colocar o projeto em funcionamento na sua máquina local.

### 1. Requisitos

* Python 3.6 ou superior
* A biblioteca [Pillow](https://python-pillow.org/)

### 2. Instalação

1.  Clone este repositório ou apenas baixe o arquivo `converter.py`.
2.  Crie as pastas necessárias. A estrutura de arquivos esperada é:

    ```
    SeuProjeto/
    |
    |-- converter.py    <-- O script Python
    |
    |-- entrada/          <-- Coloque suas imagens .png e .webp aqui
    |
    ```

3.  Instale a biblioteca `Pillow` (se ainda não a tiver):

    ```bash
    pip install Pillow
    ```

### 3. Como Usar

1.  **Adicione suas imagens:** Coloque todas as imagens que você deseja converter (ex: `foto.png`, `logo.webp`) dentro da pasta `entrada/`.
2.  **Execute o script:** Abra seu terminal, navegue até a pasta do projeto (`SeuProjeto/`) e execute:

    ```bash
    python converter.py
    ```
3.  **Verifique os resultados:** O script criará automaticamente a pasta `saida/` (se ela não existir) e salvará todas as imagens convertidas lá dentro (ex: `foto.jpg`, `logo.jpg`).

    A estrutura final ficará assim:
    ```
    SeuProjeto/
    |
    |-- converter.py
    |
    |-- entrada/
    |   |-- foto.png
    |   |-- logo.webp
    |
    |-- saida/
    |   |-- foto.jpg
    |   |-- logo.jpg
    |
    ```

## 🔧 Configuração

Você pode alterar facilmente as configurações do script editando as variáveis no topo do arquivo `converter.py`:

```python
# --- Configuração ---
pasta_entrada = 'entrada'
pasta_saida = 'saida'
formatos_entrada = ('.png', '.webp')  # Adicione outros formatos se precisar
formato_saida_ext = '.jpg'
formato_saida_pil = 'JPEG'
qualidade_jpg = 85  # Ajuste de 0 a 100 (mais alto = melhor qualidade, maior tamanho)
# --------------------

## 🧑‍💻 Autor

* **GitHub:** [@molz3ra](https://github.com/molz3ra)
* **LinkedIn:** [linkedin.com/in/mol035](https://www.linkedin.com/in/mol035)
