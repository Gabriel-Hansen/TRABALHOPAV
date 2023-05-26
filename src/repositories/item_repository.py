import sqlalchemy
from ..models.models import Item, db  

def get_itens() -> sqlalchemy.orm.query.Query:
    itens = db.session.query(Item).all()
    return itens

def get_item(id: int) -> Item:
    item = db.session.query(Item).get(id)
    return item

def delete_item(id: int):
    item = db.session.query(Item).get(id)
    db.session.delete(item)
    db.session.commit()

def add_item(nome: str, codigo_barras: str, preco: float, quantidade_estoque: int, fornecedor_id: int) -> Item:
 
    item = Item(nome=nome, codigo_barras=codigo_barras, preco=preco, quantidade_estoque=quantidade_estoque, fornecedor_id=fornecedor_id)
    db.session.add(item)
    db.session.commit()
    return item
    
def update_item(nome: str, codigo_barras: str, preco: float, quantidade_estoque: int, fornecedor_id: int, id: int) -> Item:
    item = db.session.query(Item).get(id)

    item.nome = nome
    item.codigo_barras = codigo_barras
    item.preco = preco
    item.quantidade_estoque = quantidade_estoque
    item.fornecedor_id = fornecedor_id

    db.session.commit()
    
    return item
