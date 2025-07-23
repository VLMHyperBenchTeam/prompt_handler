"""prompt_handler.renderer
~~~~~~~~~~~~~~~~~~~~~~~~

Простейший движок рендеринга текстовых шаблонов промптов.

Использует встроенный ``str.format``. Подключение сторонних
шаблонизаторов не планируется.
"""
from typing import Any

__all__ = ["render_prompt"]


def render_prompt(template: str, /, **kwargs: Any) -> str:
    """Рендерит шаблон промпта.

    Args:
        template: Строка-шаблон, содержащая плейсхолдеры в синтаксисе
            ``str.format`` (например, ``{name}``).
        **kwargs: Параметры для подстановки в шаблон.

    Returns:
        Сформированная строка.
    """
    try:
        return template.format(**kwargs)
    except KeyError as exc:
        missing = exc.args[0]
        raise ValueError(f"Отсутствует значение для плейсхолдера '{missing}'") from exc 