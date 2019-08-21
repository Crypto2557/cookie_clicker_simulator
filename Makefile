run:
	python main.py

run_tests:
	python tests/main.py

typecheck:
	mypy main.py

formatcheck:
	find . -name '*.py' -print0 | xargs -0 yapf --style google --diff

checks: run_tests typecheck formatcheck

install_conda:
	conda env create -f environment.yml

install_pip:
	pip install -f requirements.txt
