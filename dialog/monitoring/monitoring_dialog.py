from aiogram_dialog import Dialog, Window
from aiogram_dialog.widgets.text import Const, Format, List, Multi
from aiogram_dialog.widgets.kbd import Row, Button, Column, SwitchTo, Start, Back, Group

from states.states import DialogMonitoringStates
from utils.common import MAIN_MENU_BUTTON
from .getters import get_disk_info, platform_os, get_pc_load_info
from utils.get_pc_temp import get_sensor_data
from .utils import BACK_TO_MONITORING_MENU

monitoring_dialog_menu_window = Window(
	Multi(
		Format(text='{Caption} - {EditionID}'),
		Format(text='Version - {Version}'),
		Format(text='Windows Directory - {WindowsDirectory}'),
		Format(text='UserName - {UserName}'),
		Format(text='InstallDate - {InstallDate}\n'),
		Format(text='Время работы компьютера - {time_work_pc}'),
		sep='\n'
	),
	Group(
		Row(
			SwitchTo(
				text=Const('Загруженность системы'),
				id='system_load',
				state=DialogMonitoringStates.system_load
			),
			SwitchTo(
				text=Const('Температура'),
				id='temperature',
				state=DialogMonitoringStates.system_temp
			),
			SwitchTo(
				text=Const('загруженность дисков'),
				id='disc_load',
				state=DialogMonitoringStates.disc_load,
			),
			SwitchTo(
				text=Const('Процессы'),
				id='process',
				state=DialogMonitoringStates.process,
			),
		),
		width=2
	),
	MAIN_MENU_BUTTON,
	state=DialogMonitoringStates.monitoring_menu,
	getter=platform_os
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
	Multi(
		Format(text='RAM free - {virtual_ram_info}'),
		Format(text='CPU load : {cpu_percent}%'),
		Format(text="name - {gpu_info[0]}\n"
					"temp - {gpu_info[1]}\n"
					"driver - {gpu_info[2]}\n"
					"memoryTotal - {gpu_info[3]}\n"
					"memoryUsed - {gpu_info[4]}\n"
					"memoryFree - {gpu_info[5]}\n"),
		sep='\n\n'
	),
	BACK_TO_MONITORING_MENU,
	state=DialogMonitoringStates.system_load,
	getter=get_pc_load_info
)

monitoring_dialog = Dialog(
	monitoring_dialog_menu_window,
	disc_load_window,
	system_temp_window,
	system_load_window,
)
