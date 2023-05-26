from .controllers.funcionario_controller import FuncionarioItem , FuncionarioList
from .controllers.item_controller import ItemItem, ItemList
from .controllers.fornecedor_controller import FornecedorItem, FornecedorList
from .controllers.venda_controller import VendaItem, VendaList


def initialize_endpoints(api):
    api.add_resource(FuncionarioItem, "/funcionario/<int:funcionario_id>")
    api.add_resource(FuncionarioList, "/funcionario")

    api.add_resource(ItemItem, "/item/<int:item_id>")
    api.add_resource(ItemList, "/item")

    api.add_resource(FornecedorItem, "/fornecedor/<int:fornecedor_id>")
    api.add_resource(FornecedorList, "/fornecedor")

    api.add_resource(VendaItem, "/venda/<int:venda_id>")
    api.add_resource(VendaList, "/venda")