from fastapi import FastAPI

app = FastAPI()

@app.get("/health")
def health_check():
    """a"""
    return {"status": "ok", "message": "API funcionando!"}

@app.get("/me")
def about_me():
    return {
        "nome": "guilherme lopes",
        "email": "seuemail@example.com",
        "curso": "Si",
        "github": "https://github.com/guithunder",
        "cidade": "barbalha",
        "interesses": ["Python", "APIs", "FastAPI", "Tecnologia , meme"]
    }