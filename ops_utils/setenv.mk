all: install_deps

create_virtualenv:
	@echo "Creating virtualenv"
	@python3 -m venv ../venv --clear

update_pip: create_virtualenv
	@echo "Updating pip"
	@. ../venv/bin/activate; python3 -m pip install --upgrade pip==23.2.1 --require-virtualenv

install_deps: update_pip
	@echo "Installing dependencies"
	@. ../venv/bin/activate; pip3 install --no-cache-dir --require-virtualenv -r ../requirements/requirements.txt
