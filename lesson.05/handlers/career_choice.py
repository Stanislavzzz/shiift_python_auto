from aiogram import types, Router, F
from aiogram.filters.command import Command
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State, StatesGroup

from keyboards.prof_keyboard import make_row_keyboard


router = Router()


available_jobs = [
    "Программист",
    "Менеджер",
    "Дизайне",
]

available_grades = [
    "Junior",
    "Middle",
    "Senior",
]


class CareerChoice(StatesGroup):
    job = State()
    grade = State()


@router.message(Command('prof'))
async def command_prof(message: types.Message, state: FSMContext):
    await message.answer(f"Выбери профессию", reply_markup=make_row_keyboard(available_jobs))
    await state.set_state(CareerChoice.job)


@router.message(CareerChoice.job, F.text.in_(available_jobs))
async def prof_chosen(message: types.Message, state: FSMContext):
    await state.update_data(job=message.text)
    await message.answer(f"Выбери уровень", reply_markup=make_row_keyboard(available_grades))
    await state.set_state(CareerChoice.grade)


@router.message(CareerChoice.job)
async def prof_chosen_incorrect(message: types.Message):
    await message.answer(f"Выбери профессию из списка ниже", reply_markup=make_row_keyboard(available_jobs))


@router.message(CareerChoice.grade, F.text.in_(available_grades))
async def grade_chosen(message: types.Message, state: FSMContext):
    user_data = await state.get_data()
    await message.answer(f"Ты выбрал профессию {user_data['job']} и уровень {message.text}", reply_markup=types.ReplyKeyboardRemove())
    await state.clear()


@router.message(CareerChoice.grade)
async def grade_chosen_incorrect(message: types.Message):
    await message.answer(f"Выбери уровень из списка ниже", reply_markup=make_row_keyboard(available_grades))
