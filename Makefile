install:
	poetry install
brain-game:
	poetry run brain-game
brain-even:
	poetry run brain-even
brain-calc:
	poetry run brain-calc
build:
	poetry build
publish:
	poetry publish --dry-run
package-install:
	python3 -m pip install --user dist/*.whl
lint:
	poetry run flake8 brain_games
