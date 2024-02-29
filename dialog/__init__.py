from aiogram import Router

from .start.start_dialog import start_dialog
from .file_manage.file_manage_dialog import file_manage_dialog
from .monitoring.monitoring_dialog import monitoring_dialog
from .media.media_dialog import media_dialog
from .keyboard_control.keyboard_contriol_dialog import keyboard_control_dialog
from .trolling.trolling_dialog import trolling_dialog
from .volume_control.volume_control_dialog import volume_dialog


def include_dialogs():
	router = Router()
	router.include_routers(start_dialog,
						   file_manage_dialog,
						   monitoring_dialog,
						   media_dialog,
						   keyboard_control_dialog,
						   trolling_dialog,
						   volume_dialog)
	return router
