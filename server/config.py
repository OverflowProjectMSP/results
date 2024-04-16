from dataclasses import dataclass


@dataclass
class Config:
    PASSWORD_PG: str = '***'
    PORT_PG: str = '5432'