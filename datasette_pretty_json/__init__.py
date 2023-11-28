from datasette import hookimpl
from markupsafe import Markup, escape
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
    return Markup(
        '<pre style="white-space: pre-wrap">{data}</pre>'.format(
            data=escape(json.dumps(data, indent=4))
        )
    )
