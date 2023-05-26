import sqlalchemy
from ..models.models import Venda, db
from datetime import datetime

def get_vendas() -> sqlalchemy.orm.query.Query:
    vendas = db.session.query(Venda).all()
    return vendas

def get_venda(id: int) -> Venda:
    venda = db.session.query(Venda).get(id)
    return venda

def delete_venda(id: int):
    venda = db.session.query(Venda).get(id)
    db.session.delete(venda)
    db.session.commit()

def add_venda(item_id: int, funcionario_id: int, quantidade_vendida: int, total_vendido: int, data_venda: datetime) -> Venda:
    
    venda = Venda(item_id=item_id, funcionario_id=funcionario_id, quantidade_vendida=quantidade_vendida, total_vendido=total_vendido, data_venda=data_venda)
    db.session.add(venda)
    db.session.commit()
    return venda
    
def update_venda(item_id: int, funcionario_id: int, quantidade_vendida: int, total_vendido: int, data_venda_str: str, id: int) -> Venda:
    venda = db.session.query(Venda).get(id)
    
    data_venda = datetime.strptime(data_venda_str, "%Y-%m-%d")

    venda.item_id = item_id
    venda.funcionario_id = funcionario_id
    venda.quantidade_vendida = quantidade_vendida
    venda.total_vendido = total_vendido
    venda.data_venda = data_venda

    db.session.commit()
    
    return venda