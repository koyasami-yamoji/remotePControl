from aiogram_dialog.widgets.kbd import Start
from aiogram_dialog.widgets.text import Const
from states.states import DialogStartMenuStates


MAIN_MENU_BUTTON = Start(
	text=Const('🎌 MENU'),
	id='__main__',
	state=DialogStartMenuStates.menu
)