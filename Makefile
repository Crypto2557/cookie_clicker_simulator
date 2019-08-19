run:
	python main.py

run_tests:
	python tests/main.py


install_conda:
	conda env create -f environment.yml

install_pip:
	pip install -f requirements.txt
