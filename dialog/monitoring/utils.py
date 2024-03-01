from aiogram_dialog.widgets.text import Const
from aiogram_dialog.widgets.kbd import SwitchTo

from states.states import DialogMonitoringStates

BACK_TO_MONITORING_MENU = SwitchTo(
				text=Const('Назад'),
				id='__back_to_monitoring_menu__',
				state=DialogMonitoringStates.monitoring_menu,
			)