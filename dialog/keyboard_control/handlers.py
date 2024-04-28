from aiogram.types import CallbackQuery
from aiogram_dialog import DialogManager
from aiogram_dialog.widgets.kbd import Button
from pynput.keyboard import Controller, Key


async def on_block_screen(
	callback: CallbackQuery,
	widget: Button,
	manager: DialogManager
):
	controller: Controller = manager.middleware_data['controller']
	pres_release_buttons(controller, Key.cmd_l, 'l')


async def on_work_screen(
	callback: CallbackQuery,
	widget: Button,
	manager: DialogManager
):
	controller: Controller = manager.middleware_data['controller']
	pres_release_buttons(controller, Key.cmd, 'd')


async def on_task_manager(
	callback: CallbackQuery,
	widget: Button,
	manager: DialogManager
):
	controller: Controller = manager.middleware_data['controller']
	pres_release_buttons(controller, Key.ctrl, Key.shift, Key.esc)


async def on_open_folder(
	callback: CallbackQuery,
	widget: Button,
	manager: DialogManager
):
	controller: Controller = manager.middleware_data['controller']
	pres_release_buttons(controller, Key.cmd, 'e')


def pres_release_buttons(controller: Controller, *keys):
	for key in keys:
		controller.press(key)
	for key in keys:
		controller.release(key)
