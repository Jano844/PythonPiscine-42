# ft_package

A simple test Python package that provides the function `count_in_list`.

## create venv
python3 -m venv venv

## 
pip show -v ft_package -> show Package Description

## Make Changes in the Package

While Developing ->	pip install -e .
pip install --force-reinstall -e . -> needed after setup file changes


Deployment ->	python3 -m build
After Code Changes ->	pip install --force-reinstall ./dist/...

```python
from ft_package import count_in_list

print(count_in_list(["toto", "tata", "toto"], "toto"))  # Output: 2
print(count_in_list(["toto", "tata", "toto"], "tutu"))  # Output: 0




