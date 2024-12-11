from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.middleware.cors import CORSMiddleware
from pathlib import Path

from Cliente import cliente_view
from Produto import produto_view
from Venda import venda_view


# Aplicação FastAPI
app = FastAPI()

app.include_router(produto_view.router)
app.include_router(venda_view.router)
app.include_router(cliente_view.router)


# Configuração de CORS (opcional para acessar localmente com diferentes portas)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Configuração de arquivos estáticos
static_folder = Path(__file__).parent / "static"
app.mount("/static", StaticFiles(directory=static_folder), name="static")


# Rota para servir o HTML principal
@app.get("/", response_class=HTMLResponse)
def get_home():
    with open(static_folder / "index.html", "r") as file:
        html_content = file.read()
    return HTMLResponse(content=html_content)




#COMANDO PARA RODAR O SERVIDOR
#uvicorn main:app --reload