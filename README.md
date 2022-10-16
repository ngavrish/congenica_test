# congenica_test
Auotmated tests for hiring challange at Congenica

From cloned repo directory run:

export PYTHONPATH="${PYTHONPATH}:${PWD}" && pip install -r requirements.txt && pytest -s -v congenica_test/tests/web/ --app=web 
