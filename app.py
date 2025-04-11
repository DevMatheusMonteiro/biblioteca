from database_config_sqlalchemy import create_tables
from utils.validar_inputs import entrar_data
from view.menu import Menu
from datetime import datetime
# Projeto final
create_tables()
Menu.menu()