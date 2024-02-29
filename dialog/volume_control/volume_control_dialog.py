from aiogram_dialog.widgets.kbd import Row, Button, Column, SwitchTo, Start
from aiogram_dialog.widgets.text import Const
from aiogram_dialog import Dialog, Window

from states import states
from utils.common import MAIN_MENU_BUTTON

volume_dialog = Dialog(
	Window(
		Const(text='🔊 Volume'),
		MAIN_MENU_BUTTON,
		state=states.DialogVolumeStates.volume_menu
	)
)
