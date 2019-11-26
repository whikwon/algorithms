format:
	isort -rc .
	yapf -i -r --style .style.yapf .

test: 
	flake8 .
	isort -rc --check-only --diff .
	yapf -r -d --style .style.yapf .
