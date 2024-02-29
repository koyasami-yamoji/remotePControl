from aiogram_dialog import Dialog, Window
from aiogram_dialog.widgets.text import Const
from aiogram_dialog.widgets.kbd import Row, Button, Column, SwitchTo, Start

from states import states
from utils.common import MAIN_MENU_BUTTON

keyboard_control_dialog = Dialog(
	Window(
		Const(text='⌨ Keyboard'),
		MAIN_MENU_BUTTON,
		state=states.DialogKeyboardStates.keyboard_menu
	)
)
