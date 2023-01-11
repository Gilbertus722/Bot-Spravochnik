import crud
import logger as lg
import user_interface as ui

lg.logging.info('Start')
crud.init_data_base('base_phone.csv')
ui.ls_menu()