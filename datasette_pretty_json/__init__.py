from datasette import hookimpl
import jinja2
import json


@hookimpl(trylast=True)
def render_cell(value):
    if not isinstance(value, str):
        return None
    stripped = value.strip()
    if not (
        (stripped.startswith("{") and stripped.endswith("}"))
        or (stripped.startswith("[") and stripped.endswith("]"))
    ):
        return None
    try:
        data = json.loads(value)
    except ValueError:
        return None
    return jinja2.Markup(
        '<pre>{data}</pre>'.format(
            data=jinja2.escape(json.dumps(data, indent=4))
        )
    )
