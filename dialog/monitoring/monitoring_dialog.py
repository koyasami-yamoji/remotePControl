from aiogram_dialog import Dialog, Window
from aiogram_dialog.widgets.text import Const, Format, List
from aiogram_dialog.widgets.kbd import Row, Button, Column, SwitchTo, Start, Back, Group

from states.states import DialogMonitoringStates
from utils.common import MAIN_MENU_BUTTON
from utils.pc_monitoring import get_disk_info
from utils.get_pc_temp import get_sensor_data
from .utils import BACK_TO_MONITORING_MENU

monitoring_dialog_menu_window = Window(
	Const(text='📺 Мониторинг системы'),
	Group(
		Row(
			Button(text=Const('Загруженность системы'), id='system_load'),
			SwitchTo(
				text=Const('Температура'),
				id='temperature',
				state=DialogMonitoringStates.system_temp
			),
			Button(text=Const('Время работы'), id='time_work'),
			SwitchTo(
				text=Const('загруженность диска'),
				id='disc_load',
				state=DialogMonitoringStates.disc_load,
			),
		),
		width=2
	),
	MAIN_MENU_BUTTON,
	state=DialogMonitoringStates.monitoring_menu,
)

disc_load_window = Window(
	List(
		field=Format(
			text='<b>Disc: {item[1]}</b> \n<b>Total:</b> <u>{item[2]}</u> GB | '
			'<b>Used</b>: <u>{item[3]}</u> GB | <b>Free</b>: <u>{item[4]}</u> GB | '
			'<b>Load</b>: <u>{item[5]}%</u>\n\n'),
		items='discs'),
	BACK_TO_MONITORING_MENU,
	state=DialogMonitoringStates.disc_load,
	getter=get_disk_info
)

system_temp_window = Window(
	List(
		field=Format('{item[0]}'),
		items='sensor_data'
	),
	BACK_TO_MONITORING_MENU,
	state=DialogMonitoringStates.system_temp,
	getter=get_sensor_data
)


system_load_window = Window(
	List(
		field=Format('{item[0]}'),
		items='system_load_data'
	),
	BACK_TO_MONITORING_MENU,
	state=DialogMonitoringStates.monitoring_menu
)


monitoring_dialog = Dialog(
	monitoring_dialog_menu_window,
	disc_load_window,
	system_temp_window
)
