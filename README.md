# API-OpenAI

## Pré-requisitos

- Python 3.7+ instalado
- Chave de API da OpenAI (obtenha em https://platform.openai.com)
- Git (opcional, para clonar o repositório)

---

## Passos para rodar a aplicação

### 1. Clonar o repositório (opcional)

```bash
git clone https://github.com/seu_usuario/seu_repositorio.git
cd seu_repositorio
````

### 2. Criar e ativar um ambiente virtual (recomendado)

```bash
python -m venv venv
```

* No Windows:

```bash
venv\Scripts\activate
```

* No Linux/macOS:

```bash
source venv/bin/activate
```

### 3. Instalar as dependências

```bash
pip install -r requirements.txt
```

### 4. Configurar a chave da API OpenAI

Crie um arquivo `.env` na raiz do projeto com o conteúdo:

```
OPENAI_API_KEY=sua_chave_aqui
```

### 5. Rodar a aplicação Flask

```bash
python app.py
```
### 6. Acessar a aplicação

Abra no navegador(Exemplo):

```
http://127.0.0.1:6000
```

---

## Observações adicionais

* Verifique no código `app.py` se a leitura da variável `OPENAI_API_KEY` está configurada corretamente.

* Pastas `templates` e `static` são para arquivos HTML e recursos estáticos (CSS, JS, imagens).

