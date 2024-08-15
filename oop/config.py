from pydantic import BaseModel


class Settings(BaseModel):
    G: float = 9.87


settings = Settings()
