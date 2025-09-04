# atv_API_simples

## ⚙️ Como rodar localmente
```bash
git clone https://github.com/guithunder/aula-back.git
cd meu_projeto_api
pip install -r requirements.txt
uvicorn app.main:app --reload

start uvicorn app.main:app --host 0.0.0.0 --port $PORT
build uvicorn app.main:app --host 0.0.0.0 --port $PORT
.env APP_NAME= API_TEST  APP_VERSION = "1.0.0"