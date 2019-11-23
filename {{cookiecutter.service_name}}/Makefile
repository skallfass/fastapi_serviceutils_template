.DEFAULT_GOAL := help
SHELL := bash

.PHONY : check clean docker docs finalize info init tests update help
.SILENT: check clean docker docs finalize info init tests update _create_devs_env _create_main_env _update_devs_env _update_main_env

python_meant=$(cat .python-version)
python_used=$(which python)
python_version=$(python --version)
project_version=$(grep 'version = ' pyproject.toml | sed 's/version = //' | sed 's/"//' | sed 's/"//')


# Show info about current project
info:
	echo "Project:"
	echo "========"
	echo "version: $(value project_version)"
	echo ""
	echo 'Used config:' && \
	echo '============' && \
	cat app/config.yml && \
	echo "" && \
	echo 'Python:' && \
	echo '=======' && \
	echo "used python: $(value python_used)" && \
	echo "version:     $(value python_version)" && \
	echo "" && \
	echo "Info about current environment:" && \
	echo '===============================' && \
	poetry show

# Cleans the working directory
clean:
	rm -rf htmlcov; \
	rm -rf *.egg-info; \
	rm -rf dist; \
	rm -rf **/__pycache__; \
	rm -rf docs/_build; \
	rm -rf docs/api; \
	rm -rf .pytest_cache; \
	rm -rf .coverage; \
	rm -rf log

_create_env:
	poetry install

_update_env:
	poetry update

_lock_it:
	poetry lock
	dephell deps convert --to requirements.txt

_coverage_badge:
	coverage-badge -f -o docs/source/coverage.svg

_docker_build_image:
	docker build -t {{cookiecutter.service_name}}:$(value project_version) .

# Run tests using pytest
tests:
	pytest

# Finalize the main env
finalize: tests _lock_it

# Create sphinx documentation for the project
docs: tests _coverage_badge
	PYTHONPATH=. pydocmd build

# Initialize project
init: _create_env _lock_it
	git init
	git add .
	git commit -m 'Initial commit'

# Update environments based on pyproject.toml definitions and run pre-commit
update: _update_env _lock_it

check:
	pre-commit run --all-files

# Create docker-image for project
docker: finalize _docker_build_image

# Show this help prompt.
help:
	@ echo 'Helpers for development inside {{cookiecutter.service_name}} based on fastapi using fastapi-serviceutils.'
	@ echo
	@ echo '  Usage:'
	@ echo ''
	@ echo '    make <target> [flags...]'
	@ echo ''
	@ echo '  Targets:'
	@ echo ''
	@ awk '/^#/{ comment = substr($$0,3) } comment && /^[a-zA-Z][a-zA-Z0-9_-]+ ?:/{ print "   ", $$1, comment }' $(MAKEFILE_LIST) | column -t -s ':' | sort
	@ echo ''
	@ echo '  Flags:'
	@ echo ''
	@ awk '/^#/{ comment = substr($$0,3) } comment && /^[a-zA-Z][a-zA-Z0-9_-]+ ?\?=/{ print "   ", $$1, $$2, comment }' $(MAKEFILE_LIST) | column -t -s '?=' | sort
	@ echo ''
	@ echo ''
	@ echo '  Note:'
	@ echo '      This workflow requires the following programs / tools to be installed:'
	@ echo '      - poetry'
	@ echo '      - dephell'
	@ echo '      - pyenv'

