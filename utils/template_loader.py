from jinja2 import Environment, FileSystemLoader
from dataclasses import asdict

from models.sense import FinalSense


def render_card_html(final_sense: FinalSense, path: str) -> str:
    env = Environment(
        loader=FileSystemLoader("templates"),
        autoescape=True
    )

    template = env.get_template(path)

    context = {"sense": asdict(final_sense)}
    html = template.render(context)
    return html
