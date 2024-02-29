from aiogram_dialog import Dialog, Window
from aiogram_dialog.widgets.text import Const
from aiogram_dialog.widgets.kbd import Row, Button, Column, SwitchTo, Start

from states import states
from utils.common import MAIN_MENU_BUTTON

monitoring_dialog = Dialog(
	Window(
		Const(text='📺 Мониторинг системы'),
		Column(
			Button(text=Const('Загруженность системы'), id='system_load'),
			Button(text=Const('Температура'), id='temperature'),
			Button(text=Const('Время работы'), id='time_work')
		),
		MAIN_MENU_BUTTON,
		state=states.DialogMonitoringStates.monitoring_menu
	)
)
