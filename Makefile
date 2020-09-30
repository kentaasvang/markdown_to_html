
default:
	@( \
		echo "make test: source environment and run script with test file"; \
		echo "make clean: remove files produced by 'make test'"; \
		echo "make open: opens the file produced by the script in the chrome browser"; \
		echo "make install: installs all the dependecies"; \
	)

test:
	( \
		source venv/bin/activate; \
		python3 main.py test_file.md; \
	)

clean:
	rm -rf test_file_*

open:
	open -a "Google Chrome" test_file_0.html

install:
	source venv/bin/activate && pip install -r requirements.txt
