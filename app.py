from database_config_sqlalchemy import create_tables
from utils.validar_inputs import entrar_data
from view.menu_usuario import MenuUsuario
# Projeto final
create_tables()
MenuUsuario.listar_usuarios()