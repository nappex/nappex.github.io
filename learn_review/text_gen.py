from pathlib import Path

from jinja2 import Environment, FileSystemLoader
from yaml import safe_load


TEMPLATES_DIR = 'templates'
TEMPLATE_FILENAME ='index.html'
INPUT_FILE = Path('data.yaml')
OUTPUT_FILE = Path(__file__).parents[1] / 'output' / 'learn_review' / 'index.html'

env = Environment(loader=FileSystemLoader(TEMPLATES_DIR))
template = env.get_template(TEMPLATE_FILENAME)

data = safe_load(INPUT_FILE.read_text())

print(data)


completed = filter(lambda task: task.get('complete', False), data)

rendered_template = template.render(completed=completed)

OUTPUT_FILE.write_text(rendered_template)