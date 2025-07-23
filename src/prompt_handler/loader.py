"""prompt_handler.loader
~~~~~~~~~~~~~~~~~~~~~~~~

Утилита для безопасной загрузки текста промптов из файлов.
Ранее находилась в корне пакета, перенесена для единообразия структуры.
"""
from pathlib import Path
from typing import Union

__all__ = ["load_prompt"]


def load_prompt(prompt_path: Union[str, Path], *, encoding: str = "utf-8") -> str:
    """Загружает промпт из файла.

    Args:
        prompt_path: Путь к файлу с промптом.
        encoding: Кодировка файла (по умолчанию ``utf-8``).

    Returns:
        Содержимое файла как строку.

    Raises:
        ValueError: Неверный тип или пустое значение ``prompt_path``.
        FileNotFoundError: Файл не существует или не является файлом.
        OSError: Ошибка чтения файла.
    """
    if not prompt_path:
        raise ValueError("prompt_path не может быть пустым")

    # Унифицируем тип.
    if isinstance(prompt_path, str):
        prompt_path = Path(prompt_path)
    elif not isinstance(prompt_path, Path):
        raise ValueError("prompt_path должен быть строкой или Path объектом")

    if not prompt_path.exists():
        raise FileNotFoundError(f"Файл промпта не найден: {prompt_path}")
    if not prompt_path.is_file():
        raise FileNotFoundError(f"Путь не является файлом: {prompt_path}")

    try:
        return prompt_path.read_text(encoding=encoding)
    except OSError as exc:
        raise OSError(f"Не удалось прочитать файл промпта {prompt_path}: {exc}") from exc 