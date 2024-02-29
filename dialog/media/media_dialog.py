from aiogram_dialog import Dialog, Window
from aiogram_dialog.widgets.text import Const
from aiogram_dialog.widgets.kbd import Row, Button, Column, SwitchTo, Start

from states import states
from utils.common import MAIN_MENU_BUTTON

media_dialog = Dialog(
	Window(
		Const(text='🎵 Media'),
		MAIN_MENU_BUTTON,
		state=states.DialogMediaStates.media_menu
	)
)
