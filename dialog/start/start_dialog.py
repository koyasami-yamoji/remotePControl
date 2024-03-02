from aiogram_dialog import Dialog, Window, LaunchMode
from aiogram_dialog.widgets.text import Const
from aiogram_dialog.widgets.kbd import Row, Start

from states import states

start_dialog = Dialog(
	Window(
		Const('Доброго времени бытия'),
		Row(
			Start(text=Const('🎵 Media'),
				  id='media',
				  state=states.DialogMediaStates.media_menu),
			Start(text=Const('📺 Monitoring'),
				  id='monitoring',
				  state=states.DialogMonitoringStates.monitoring_menu),
			Start(text=Const('😁 trolling'),
				  id='trolling',
				  state=states.DialogTrollingStates.trolling_menu),
		),
		Row(
			Start(text=Const('⌨ Keyboard'),
				  id='keyboard',
				  state=states.DialogKeyboardStates.keyboard_menu),
			Start(text=Const('📁 Files'),
				  id='files',
				  state=states.DialogFilterStates.file_manager_menu),
			Start(text=Const('🔊 Volume'),
				  id='volume',
				  state=states.DialogVolumeStates.volume_menu)
		),
		state=states.DialogStartMenuStates.menu,
	),
	launch_mode=LaunchMode.ROOT
)
