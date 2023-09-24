install:
	poetry install
brain-game:
	poetry run brain-game
brain-even:
	poetry run brain-even
brain-calc:
	poetry run brain-calc
brain_gcd:
	poetry run brain-gcd
brain-progression:
	poetry run brain-progression
brain-prime:
	poetry run brain-prime
build:
	poetry build
publish:
	poetry publish --dry-run
package-install:
	python3 -m pip install --user dist/*.whl
package-reinstall:
	python3 -m pip install --user --force-reinstall dist/*whl
lint:
	poetry run flake8 brain_games
