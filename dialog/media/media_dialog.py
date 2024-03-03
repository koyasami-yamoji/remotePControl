from aiogram_dialog import Dialog, Window
from aiogram_dialog.widgets.text import Const
from aiogram_dialog.widgets.kbd import Row, Button

from states import states
from utils.common import MAIN_MENU_BUTTON
from .handlers import (on_volume_plus_press,
					   on_volume_minus_press,
					   on_volume_off_on_press,
					   on_play_pause_press,
					   on_next_press,
					   on_prev_press)

media_dialog = Dialog(
	Window(
		Const(text='🎵 Media'),
		Row(
			Button(
				text=Const("⏮prev"),
				id='prev_media',
				on_click=on_prev_press
			),
			Button(
				text=Const("⏯ play-pause"),
				id='play_media',
				on_click=on_play_pause_press
			),
			Button(
				text=Const("⏭next"),
				id='next_media',
				on_click=on_next_press
			),
		),
		Row(
			Button(
				text=Const('🔽Volume-'),
				id='volume_minus',
				on_click=on_volume_minus_press
			),
			Button(
				text=Const('⏯ Volume off/on'),
				id='volume_off_on',
				on_click=on_volume_off_on_press
			),
			Button(
				text=Const('🔼Volume+'),
				id='volume_plus',
				on_click=on_volume_plus_press
			)
		),
		MAIN_MENU_BUTTON,
		state=states.DialogMediaStates.media_menu
	)
)
