from pydantic import BaseModel

class BaseSchema(BaseModel):
    def to_json(self) -> str:
        """Converte o modelo em um JSON serializado."""
        return self.json()

    def to_dict(self) -> dict:
        """Converte o modelo em um dicionário."""
        return self.dict()