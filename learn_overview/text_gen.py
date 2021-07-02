from pathlib import Path

from jinja2 import Environment, FileSystemLoader
from yaml import safe_load


TEMPLATE_FILE = Path('templates', 'index.html')
INPUT_FILE = Path('data.yaml')
OUTPUT_FILE = Path(__file__).parents[1] / 'output' / 'learn_overview' / 'index.html'

env = Environment(loader=FileSystemLoader(TEMPLATE_FILE.parent))
template = env.get_template(TEMPLATE_FILE.name)

data = safe_load(INPUT_FILE.read_text())

completed = []
uncompleted = []

for task in data:
    if task.get('completed', False):
        completed.append(task)
    else:
        uncompleted.append(task)


rendered_template = template.render(completed=completed, uncompleted=uncompleted)

OUTPUT_FILE.write_text(rendered_template)