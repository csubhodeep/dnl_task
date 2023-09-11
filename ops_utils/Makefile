
all: install_deps

create_virtualenv:
	@echo "Creating virtualenv"
	@python3 -m venv ../venv --clear


update_pip: create_virtualenv
	@echo "Updating pip"
	@. ../venv/bin/activate; python3 -m pip install --upgrade pip==23.2.1 --require-virtualenv

install_pip_tools: update_pip
	@echo "Installing pip-tools"
	@. ../venv/bin/activate; pip3 install pip-tools==7.3.0 --require-virtualenv

install_deps: install_pip_tools
	@echo "Installing dependencies"
	@. ../venv/bin/activate; pip-sync ../requirements/requirements.txt --pip-args '--no-cache-dir --require-virtualenv'
