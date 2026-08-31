<h1 align="center">📂 Download and Move - Organizador Automático de Arquivos 🐍</h1>

<p align="center">
  <img src="https://img.shields.io/badge/Python-3776AB.svg?style=for-the-badge&logo=python&logoColor=white" alt="Python Badge">
  <img src="https://img.shields.io/badge/Status-Conclu%C3%ADdo-success?style=for-the-badge" alt="Status Badge">
</p>

<p align="center">
  <i>Uma automação que monitora sua pasta de Downloads e organiza seus arquivos automaticamente.</i><br>
  <b>Autor:</b> Caetano Bordin
</p>

---

## 🧩 Sobre o Projeto 👩‍💻

**Download and Move** é uma aplicação desenvolvida em **Python** que transforma a pasta de Downloads em um sistema de organização automática.

O programa permanece monitorando uma pasta em tempo real e, sempre que um novo arquivo é detectado, identifica sua extensão e decide automaticamente para qual categoria ele deve ser enviado.

Em vez de precisar organizar manualmente cada arquivo baixado, o programa realiza todo o processo:

**Download → Detecção → Identificação → Organização → Movimentação**

As categorias atualmente utilizadas são:

* 🖼️ **Image_Files**
* 🎬 **Video_Files**
* 📄 **Document_Files**
* ⚙️ **Setup_Files**

Caso um arquivo com o mesmo nome já exista no destino, o programa gera automaticamente um novo nome utilizando um número aleatório, evitando a substituição do arquivo original.

O projeto foi desenvolvido como uma experiência prática de **automação, manipulação de arquivos e interação com o sistema operacional**, indo além de exercícios convencionais de Python.

---

## 🧰 Tecnologias Utilizadas

| Categoria                      | Detalhes                        |
| ------------------------------ | ------------------------------- |
| 💻 **Linguagem**               | Python 3                        |
| 👀 **Monitoramento**           | Watchdog                        |
| 📁 **Manipulação de arquivos** | `os` e `shutil`                 |
| 🎲 **Geração de nomes**        | `random`                        |
| ⏱️ **Controle de tempo**       | `time`                          |
| ⚙️ **Arquitetura**             | Event-driven / Observer Pattern |

---

## ⚙️ Funcionalidades

### 👀 Monitoramento em Tempo Real

* Monitora continuamente a pasta `Downloads`
* Detecta automaticamente novos arquivos
* Utiliza o `Observer` da biblioteca Watchdog
* Reage ao evento de criação de novos arquivos

### 🧠 Identificação Automática

O programa analisa a extensão do arquivo e determina sua categoria automaticamente.

**🖼️ Imagens**

* `.jpg`
* `.jpeg`
* `.png`
* `.jfif`
* `.webp`
* `.gif`

**🎬 Vídeos**

* `.mpg`
* `.mp2`
* `.mpeg`
* `.mpe`
* `.mpv`
* `.mp4`
* `.m4p`
* `.m4v`
* `.avi`
* `.mov`

**📄 Documentos**

* `.ppt`
* `.xls`
* `.csv`
* `.pdf`
* `.txt`

**⚙️ Arquivos de instalação**

* `.exe`
* `.bin`
* `.cmd`
* `.msi`
* `.dmg`

### 📂 Organização Automática

Ao detectar um arquivo compatível:

1. O programa identifica o nome e a extensão.
2. Descobre a categoria correspondente.
3. Verifica se o diretório de destino existe.
4. Cria o diretório caso seja necessário.
5. Verifica se já existe um arquivo com o mesmo nome.
6. Caso exista, gera um novo nome.
7. Move o arquivo para sua categoria.
8. Exibe o progresso no terminal.

### 🔄 Prevenção de Conflitos

Caso `arquivo.pdf` já exista em `Document_Files`, o programa não sobrescreve o arquivo.

Em vez disso, pode gerar um nome como:

```text
arquivo482.pdf
```

Assim, os dois arquivos podem permanecer armazenados.

### 🖥️ Feedback no Terminal

Durante a execução, o programa fornece informações sobre o que está acontecendo:

```text
Executando...
Baixado trabalho.pdf
Diretório existe...
Movendo trabalho.pdf....
```

Isso permite acompanhar o funcionamento da automação em tempo real.

---

## 🧠 Como o Sistema Funciona

O funcionamento pode ser representado de forma simples:

```text
                 📥 DOWNLOADS
                      │
                      ▼
              👀 Observer detecta
                novo arquivo
                      │
                      ▼
             🔍 Identifica extensão
                      │
          ┌───────────┼───────────┐
          ▼           ▼           ▼
       🖼️ IMAGEM   🎬 VÍDEO    📄 DOCUMENTO
          │           │           │
          └───────────┼───────────┘
                      │
                      ▼
              📂 Cria categoria
                 se necessário
                      │
                      ▼
              ⚠️ Nome duplicado?
                 /          \
               SIM          NÃO
                │             │
                ▼             ▼
          🔢 Novo nome    Nome original
                │             │
                └──────┬──────┘
                       ▼
                  🚚 MOVE FILE
                       │
                       ▼
                 📁 ORGANIZADO
```

---

## 📚 Aprendizados

Durante o desenvolvimento deste projeto, foram aplicados conceitos importantes de Python e de interação com o sistema operacional.

### 🔸 Monitoramento de Eventos

Foi utilizado o **Watchdog** para transformar o programa em uma aplicação orientada a eventos.

Em vez de verificar manualmente a pasta a cada momento, o sistema reage quando um novo arquivo é criado.

```python
class FileMovementHandler(FileSystemEventHandler):

    def on_created(self, event):
        ...
```

### 🔸 Manipulação do Sistema de Arquivos

Foram utilizados recursos do módulo `os` para:

* Separar nome e extensão;
* Obter nomes de arquivos;
* Verificar a existência de diretórios;
* Criar novas pastas.

### 🔸 Movimentação de Arquivos

A biblioteca `shutil` foi utilizada para realizar a movimentação dos arquivos:

```python
shutil.move(path1, path3)
```

### 🔸 Estruturas de Dados

Um dicionário foi utilizado para relacionar categorias às suas extensões:

```python
dir_tree = {
    "Image_files": [...],
    "Video_Files": [...],
    "Document_Files": [...],
    "Setup_Files": [...]
}
```

Isso permite adicionar novas categorias e extensões de maneira relativamente simples.

### 🔸 Tratamento de Conflitos

O projeto também trabalha com uma situação comum em sistemas de arquivos: dois arquivos possuírem o mesmo nome.

O programa verifica a existência do arquivo antes de realizar a movimentação e gera um novo nome quando necessário.

### 🔸 Programação Orientada a Eventos

O projeto apresenta um conceito muito importante:

> O programa não precisa esperar uma ação do usuário para funcionar. Ele permanece observando o sistema e reage quando um evento acontece.

Esse conceito é utilizado em diversos tipos de aplicações reais.

---

## 🚀 Como Executar

### 1. Instale o Python

Certifique-se de possuir o **Python 3** instalado.

Você pode verificar utilizando:

```bash
python --version
```

### 2. Instale o Watchdog

No terminal:

```bash
pip install watchdog
```

### 3. Configure os diretórios

No código, altere:

```python
from_dir = "C:/Users/DELL/Downloads"
```

para o caminho da sua pasta de Downloads.

Depois altere:

```python
to_dir = "C:/Users/DELL/Documents/Arquivos_Documentos"
```

para o diretório onde deseja que os arquivos sejam organizados.

### 4. Execute

```bash
python main.py
```

Depois disso, o programa permanecerá ativo monitorando a pasta configurada.

Para interromper:

```text
CTRL + C
```

---

## 🧪 Exemplo de Uso

Imagine que a pasta `Downloads` esteja assim:

```text
Downloads/
├── foto.png
├── trabalho.pdf
├── video.mp4
└── instalador.exe
```

Após o programa detectar os arquivos, a estrutura poderá ficar:

```text
Arquivos_Documentos/
├── Image_files/
│   └── foto.png
│
├── Document_Files/
│   └── trabalho.pdf
│
├── Video_Files/
│   └── video.mp4
│
└── Setup_Files/
    └── instalador.exe
```

O usuário não precisa mover nenhum deles manualmente.

---

## 🔮 Possíveis Evoluções

O projeto pode ser expandido para se tornar um organizador de arquivos ainda mais completo.

Algumas possibilidades:

* 📦 Adicionar novas categorias;
* 🧹 Organizar arquivos que já estão na pasta antes da execução;
* 🗓️ Organizar arquivos por data;
* 📝 Criar um sistema de logs;
* ⚙️ Utilizar um arquivo de configuração em vez de caminhos fixos;
* 🔔 Adicionar notificações quando um arquivo for movido;
* 🛡️ Melhorar o tratamento de erros;
* 🔄 Criar uma interface gráfica;
* 🚀 Inicializar automaticamente junto com o Windows.

---

## 📜 Licença

* **Permissão de Uso:** O código pode ser usado somente para fins educacionais.

* **Modificação e Distribuição:** Qualquer pessoa pode modificar o código e redistribuí-lo, seja na forma original ou modificada, desde que citando os autores.

* **Inclusão da Licença:** Ao redistribuir o software, a licença original e o aviso de direitos autorais devem ser incluídos no código-fonte ou na documentação, garantindo que futuros usuários conheçam seus direitos.

* **Isenção de Garantia:** O software é fornecido **"como está"**, sem garantias de qualquer tipo, explícitas ou implícitas. Os autores não são responsáveis por quaisquer danos decorrentes do uso do software.

---

## 👤 Autor

* [@Caetano-2012](https://www.github.com/Caetano-2012)
