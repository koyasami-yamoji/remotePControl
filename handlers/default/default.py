from aiogram import Router, F
from aiogram.types import Message
from aiogram.filters import CommandStart
from aiogram_dialog import Dialog, DialogManager, Window, StartMode
from aiogram_dialog.widgets.text import Const
from aiogram_dialog.widgets.kbd import Row, Button
from aiogram_dialog.widgets.markup.reply_keyboard import ReplyKeyboardFactory

from states.states import DialogStartMenuStates

router = Router()

start_dialog = Dialog(
	Window(
		Const('Доброго времени бытия!'),
		Row(
			Button(text=Const('🎵 Media'),
				   id='media'),
			Button(text=Const('📺 Monitoring'),
				   id='monitoring'),
			Button(text=Const('😁 trolling'),
				   id='trolling'),
		),
		Row(
			Button(text=Const('⌨ Keyboard'),
				   id='keyboard'),
			Button(text=Const('📁 Files'),
				   id='files'),
			Button(text=Const('🔊 Volume'),
				   id='volume')
		),
		state=DialogStartMenuStates.start,
		markup_factory=ReplyKeyboardFactory(resize_keyboard=True,
											input_field_placeholder=Const('Выберите действие'))
	)
)


@router.message(CommandStart())
async def start(message: Message, dialog_manager: DialogManager):
	print('qwe')
	await dialog_manager.start(state=DialogStartMenuStates.start, mode=StartMode.RESET_STACK)


@router.message()
async def echo(message: Message):
	await message.answer(text=f"{message.from_user.id} {message.text}")