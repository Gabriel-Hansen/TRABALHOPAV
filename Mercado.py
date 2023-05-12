#Primeiro arquivo de teste

from sqlalchemy import create_engine, Column, Integer, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

engine = create_engine('sqlite:///mercado.db', echo=True)
Base = declarative_base()

class Funcionario(Base):
    __tablename__ = 'funcionarios'
    id = Column(Integer, primary_key=True)
    nome = Column(String)
    cpf = Column(String)
    cargo = Column(String)
    senha = Column(String)

class Item(Base):
    __tablename__ = 'itens'
    id = Column(Integer, primary_key=True)
    nome = Column(String)
    codigo_barras = Column(String)
    preco = Column(Integer)
    quantidade_estoque = Column(Integer)
    fornecedor_id = Column(Integer, ForeignKey('fornecedores.id'))
    fornecedor = relationship("Fornecedor", back_populates="itens")

class Fornecedor(Base):
    __tablename__ = 'fornecedores'
    id = Column(Integer, primary_key=True)
    nome = Column(String)
    endereco = Column(String)
    itens = relationship("Item", back_populates="fornecedor")



class Venda(Base):
    __tablename__ = 'vendas'
    id = Column(Integer, primary_key=True)
    item_id = Column(Integer, ForeignKey('itens.id'))
    item = relationship("Item")
    funcionario_id = Column(Integer, ForeignKey('funcionarios.id'))
    funcionario = relationship("Funcionario")
    quantidade_vendida = Column(Integer)
    total_vendido = Column(Integer)
    data_venda = Column(String)

Base.metadata.create_all(engine) 



#create

#from sqlalchemy.orm import sessionmaker8

#Session = sessionmaker(bind=engine)
#session = Session()

#novo_item = Item(nome="Arroz", codigo_barras="7891234567890", preco=500, quantidade_estoque=100, fornecedor_id=1)
#session.add(novo_item)
#session.commit()

#novo_fornecedor = Fornecedor(nome="Fornecedor A", endereco="Rua 123, Bairro C", itens=[novo_item])
#session.add(novo_fornecedor)
#session.commit()


#novo_funcionario = Funcionario(nome="João", cpf="12345678901", cargo="Atendente", senha="1234")
#session.add(novo_funcionario)
#session.commit()


#read

#itens = session.query(Item).all()
#for item in itens:
   # print(item.nome, item.codigo_barras, item.preco, item.quantidade_estoque)

#fornecedores = session.query(Fornecedor).all()
#for fornecedor in fornecedores:
  #  print(fornecedor.nome, fornecedor.endereco)
  #  for item in fornecedor.itens:
    #    print("\t", item.nome)

#funcionarios = session.query(Funcionario).all()
#for funcionario in funcionarios:
  #  print(funcionario.nome, funcionario.cpf, funcionario.cargo)


#update

#item = session.query(Item).filter_by(nome="Arroz").first()
#item.preco = 600
#session.commit()


#fornecedor = session.query(Fornecedor).filter_by(nome="Fornecedor A").first()
#fornecedor.endereco = "Rua 456, Bairro D"
#session.commit()

#delete

#item = session.query(Item).filter_by(nome="Arroz").first()
#session.delete(item)
#session.commit()


#fornecedor = session.query(Fornecedor).filter_by(nome='Empresa de Alimentos').first()
#session.delete(fornecedor)
#session.commit()

