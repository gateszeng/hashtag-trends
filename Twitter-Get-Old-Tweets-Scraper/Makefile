targets = "(__pycache__|*.pyc|*.pyo)"

install:
	pip3 install -r requirements.txt

clean:
	find . | grep -E $(targets) | xargs rm -rf
