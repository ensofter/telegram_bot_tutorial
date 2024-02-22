from aiogram.filters import BaseFilter
from aiogram.types import Message


class IsDigitOrFloat(BaseFilter):

    async def __call__(self, message: Message, **kwargs) -> bool:
        command_args = kwargs['command'].args
        if command_args is not None:
            if command_args.isdigit() or command_args.replace(".", "").isnumeric():
                return True
            return False
