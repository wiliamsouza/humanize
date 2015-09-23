clean: clean-eggs clean-build
	@find . -iname '*.pyc' -delete
	@find . -iname '*.pyo' -delete
	@find . -iname '*~' -delete
	@find . -iname '*.swp' -delete
	@find . -iname '__pycache__' -delete

clean-eggs:
	@find . -name '*.egg' -print0|xargs -0 rm -rf --
	@rm -rf .eggs/

clean-build:
	@rm -fr build/
	@rm -fr dist/
	@rm -fr *.egg-info

test:
	python setup.py test

makei18n:
	pybabel extract . > /tmp/humanize2.po
	pybabel update -i /tmp/humanize2.po -o humanize/locale/pt_BR/LC_MESSAGES/humanize.po  -l pt_BR

compilei18n:
	pybabel compile -f -l pt_BR -i humanize/locale/pt_BR/LC_MESSAGES/humanize.po -o humanize/locale/pt_BR/LC_MESSAGES/humanize.mo
