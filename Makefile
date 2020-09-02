
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
