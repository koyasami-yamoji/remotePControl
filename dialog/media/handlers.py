from aiogram.types import CallbackQuery
from aiogram_dialog import DialogManager
from aiogram_dialog.widgets.kbd import Button
from pynput.keyboard import Key, Controller


async def on_prev_press(
	callback: CallbackQuery,
	widget: Button,
	manager: DialogManager
):
	controller: Controller = manager.middleware_data['controller']
	controller.tap(Key.media_previous)
	await callback.answer('prev')


async def on_next_press(
	callback: CallbackQuery,
	widget: Button,
	manager: DialogManager
):
	controller: Controller = manager.middleware_data['controller']
	controller.tap(Key.media_next)
	await callback.answer('next')


async def on_play_pause_press(
	callback: CallbackQuery,
	widget: Button,
	manager: DialogManager
):
	controller: Controller = manager.middleware_data['controller']
	controller.tap(Key.media_play_pause)
	await callback.answer('⏯')


async def on_volume_minus_press(
	callback: CallbackQuery,
	widget: Button,
	manager: DialogManager
):
	controller: Controller = manager.middleware_data['controller']
	controller.tap(Key.media_volume_down)
	await callback.answer('➖')


async def on_volume_plus_press(
	callback: CallbackQuery,
	widget: Button,
	manager: DialogManager
):
	controller: Controller = manager.middleware_data['controller']
	controller.tap(Key.media_volume_up)
	await callback.answer('➕')


async def on_volume_off_on_press(
	callback: CallbackQuery,
	widget: Button,
	manager: DialogManager
):
	controller: Controller = manager.middleware_data['controller']
	controller.tap(Key.media_volume_mute)
	await callback.answer('⏯ Volume')
