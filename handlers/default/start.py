from aiogram import Router
from aiogram.types import Message
from aiogram.filters import CommandStart
from aiogram_dialog import Dialog, DialogManager, StartMode


from states.states import DialogStartMenuStates

router = Router()


@router.message(CommandStart())
async def start(message: Message, dialog_manager: DialogManager):
	await dialog_manager.start(state=DialogStartMenuStates.menu, mode=StartMode.RESET_STACK)
