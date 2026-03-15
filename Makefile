test:
	@uv run pytest

lint:
	@uv run ruff check ascii_art/ tests/

create:
	@uv build
