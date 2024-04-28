from aiogram_dialog import Dialog, Window
from aiogram_dialog.widgets.text import Const
from aiogram_dialog.widgets.kbd import Row, Button, Column, SwitchTo, Start

from states import states
from utils.common import MAIN_MENU_BUTTON
from .handlers import (on_block_screen, on_work_screen, on_task_manager, on_open_folder)

keyboard_control_dialog = Dialog(
	Window(
		Const(text='⌨ Keyboard'),
		Row(
			Button(
				text=Const(text='Блокировка экрана'),
				id='block_screen',
				on_click=on_block_screen
			),
			Button(
				text=Const(text='Переход с/на раб стол'),
				id='work_screen',
				on_click=on_work_screen
			)
		),
		Row(
			Button(
				text=Const(text='Диспетчер задач'),
				id='task_manager',
				on_click=on_task_manager
			),
			Button(
				text=Const('Проводник'),
				id='open_folder',
				on_click=on_open_folder
			)
		),
		MAIN_MENU_BUTTON,
		state=states.DialogKeyboardStates.keyboard_menu
	)
)
