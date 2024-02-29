from aiogram_dialog import Dialog, Window
from aiogram_dialog.widgets.text import Const
from aiogram_dialog.widgets.kbd import Row, Button, Column, SwitchTo, Start

from states import states
from utils.common import MAIN_MENU_BUTTON

file_manage_dialog = Dialog(
	Window(
		Const(text='📁 Files'),
		MAIN_MENU_BUTTON,
		state=states.DialogFilterStates.file_manager_menu
	)
)
