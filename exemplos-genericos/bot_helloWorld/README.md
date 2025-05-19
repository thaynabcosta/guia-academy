# BotCity - Exemplo: Automatizando o Bloco de Notas

Este projeto demonstra uma automação simples com BotCity Core, onde o bot abre o Bloco de Notas, digita uma mensagem e salva o arquivo. Antes disso, ele verifica se já existe um arquivo com o mesmo nome e o remove, se necessário.

---

## 🎯 Objetivo

Criar um bot que:

1. Verifica se já existe um arquivo `.txt` com o nome esperado e o remove.
2. Abre o Bloco de Notas.
3. Digita "Hello World".
4. Salva o arquivo com um nome pré-definido.

---

## 🧠 Conceitos aplicados

- Automação de interface gráfica com BotCity Core (`DesktopBot`)
- Integração com BotMaestro (`BotMaestroSDK`)
- Manipulação de arquivos com Python
- Uso de constantes e funções auxiliares

---

## 📁 Estrutura do Projeto

bot_helloWorld/  
├── utils/  
│ ├── constants.py  
│ └── remove_files.py  
├── bot_helloWorld.botproj  
├── bot.py  
├── build.bat  
├── build.ps1  
├── build.sh  
├── hello-world.txt  
├── README.md  
└── requirements.txt  


---

## ⚙️ Como Executar

### Pré-requisitos

- Python 3.12.5+
- Instale as dependências com:

```bash
pip install -r requirements.txt
```

### 📌 Este projeto usa:

- "botcity-framework-core>=1.2.1,<2.0"  
- "botcity-maestro-sdk>=0.3.3,<1.0"

## Execução

Com Maestro (modo produção):

```bash
python bot.py --access-token=SEU_TOKEN --task-id=ID_DA_TAREFA --server=https://maestro.botcity.dev
```

Modo local (offline):

```bash
python bot.py 
```

## 📎 Referências

- [📚 Documentação BotCity Core](https://documentation.botcity.dev/core)
- [🧠 Documentação BotMaestro SDK](https://documentation.botcity.dev/maestro/sdk/)

---

Feito com 💻 por **Thayná Costa** ✨
