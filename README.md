# prompt-handler

Утилиты для загрузки (`load_prompt`) и рендеринга (`prepare_prompt`) текстовых шаблонов промптов.

* 🚚 **load_prompt** — безопасно читает файл с промптом из файловой системы
* 🖋️ **prepare_prompt** — подставляет значения в плейсхолдеры шаблона (через `str.format`)

Пакет не имеет жёстких зависимостей.

## Установка

### Установка из репозитория (Git)

* **Для пользователей с `uv` и `pyproject.toml` (рекомендуемый способ)**:
  ```bash
  uv add git+https://github.com/VLMHyperBenchTeam/prompt_handler.git@main
  uv sync
  ```
* **Для пользователей с `pip` или `uv` (прямая установка)**:
  ```bash
  pip install git+https://github.com/VLMHyperBenchTeam/prompt_handler.git@main
  # или
  uv pip install git+https://github.com/VLMHyperBenchTeam/prompt_handler.git@main
  ```

### Установка из локального дистрибутива

1.  Сборка: `uv build` (создает `.whl` и `.tar.gz` в `dist/`)
2.  Установка: `uv pip install dist/prompt-handler-0.0.1.dev1-py3-none-any.whl`
    > **Примечание:** `uv add` не поддерживает установку из `.whl` файлов. Для этого всегда используйте `uv pip install`.

### Установка в режиме разработки

```bash
uv pip install -e .
# или для пользователей pip
pip install -e .