from jinja2 import Environment, FileSystemLoader


TEMPLATES_DIR = 'templates'
TEMPLATE_FILENAME ='readme_template.md'

env = Environment(loader=FileSystemLoader(TEMPLATES_DIR))
template = env.get_template(TEMPLATE_FILENAME)
