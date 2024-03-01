from aiogram.fsm.state import StatesGroup, State


class DialogStartMenuStates(StatesGroup):
	menu = State()


class DialogMonitoringStates(StatesGroup):
	monitoring_menu = State()
	disc_load = State()
	system_temp = State()


class DialogMediaStates(StatesGroup):
	media_menu = State()


class DialogTrollingStates(StatesGroup):
	trolling_menu = State()


class DialogKeyboardStates(StatesGroup):
	keyboard_menu = State()


class DialogFilterStates(StatesGroup):
	file_manager_menu = State()


class DialogVolumeStates(StatesGroup):
	volume_menu = State()





