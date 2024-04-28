from aiogram_dialog import Dialog, Window, LaunchMode
from aiogram_dialog.widgets.text import Const, Format
from aiogram_dialog.widgets.kbd import Row, Start

from dialog.start.getters import getter_currency
from states import states

main_menu = Window(
	Const('<b>🎇🎆Доброго времени бытия</b>\n'),
	Format(text="{currency}"),
	Format(text="{weather_text}"),
	Row(
		Start(
			text=Const('🎵 Media'),
			id='media',
			state=states.DialogMediaStates.media_menu
		),
		Start(
			text=Const('📺 Monitoring'),
			id='monitoring',
			state=states.DialogMonitoringStates.monitoring_menu
		),
		Start(
			text=Const('😁 trolling'),
			id='trolling',
			state=states.DialogTrollingStates.trolling_menu
		),
	),
	Row(
		Start(
			text=Const('⌨ Keyboard'),
			id='keyboard',
			state=states.DialogKeyboardStates.keyboard_menu
		),
		Start(
			text=Const('📁 Files'),
			id='files',
			state=states.DialogFilterStates.file_manager_menu
		),
		Start(
			text=Const('🔊 Volume'),
			id='volume',
			state=states.DialogVolumeStates.volume_menu
		)
	),
	state=states.DialogStartMenuStates.menu,
	getter=getter_currency
)

start_dialog = Dialog(
	main_menu
)
