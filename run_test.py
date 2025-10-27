import pytest

#Lista de archyivos de pruebas a ejecutar

test_files = [
    "Test/test_login.py",
    "Test/test_inventory.py"
]

#Argumentos para ejecutar pruebas:

pytest_args = test_files + ["--html=report.html","--self-contained-html","-v"]


pytest.main(pytest_args)
