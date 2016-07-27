test:
	@py.test --cov-report term-missing --cov=ascii_art/ --flake8 -vs tests/ ascii_art/;

create:
	@python setup.py sdist bdist_wheel

upload:
	@python setup.py sdist bdist_wheel upload
