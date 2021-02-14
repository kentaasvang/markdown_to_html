import argparse
import markdown2
from jinja2 import Template


TEMPLATE = """
<!doctype html>
<html lang="en">
  <head>
    <!-- Required meta tags -->
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">

    <!-- Bootstrap CSS -->
    <link 
        href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta2/dist/css/bootstrap.min.css" 
        rel="stylesheet" 
        integrity="sha384-BmbxuPwQa2lc/FVzBcNJ7UAyJxM6wuqIj61tLrc4wSX0szH/Ev+nYRRuWlolflfl" 
        crossorigin="anonymous"
    >
    
    <style type="text/css">
        .codehilite .hll { background-color: #ffffcc }
        .codehilite  { background: #f8f8f8; }
        .codehilite .c { color: #408080; font-style: italic } /* Comment */
        .codehilite .err { border: 1px solid #FF0000 } /* Error */
        .codehilite .k { color: #008000; font-weight: bold } /* Keyword */
        .codehilite .o { color: #666666 } /* Operator */
        .codehilite .ch { color: #408080; font-style: italic } /* Comment.Hashbang */
        .codehilite .cm { color: #408080; font-style: italic } /* Comment.Multiline */
        .codehilite .cp { color: #BC7A00 } /* Comment.Preproc */
        .codehilite .cpf { color: #408080; font-style: italic } /* Comment.PreprocFile */
        .codehilite .c1 { color: #408080; font-style: italic } /* Comment.Single */
        .codehilite .cs { color: #408080; font-style: italic } /* Comment.Special */
        .codehilite .gd { color: #A00000 } /* Generic.Deleted */
        .codehilite .ge { font-style: italic } /* Generic.Emph */
        .codehilite .gr { color: #FF0000 } /* Generic.Error */
        .codehilite .gh { color: #000080; font-weight: bold } /* Generic.Heading */
        .codehilite .gi { color: #00A000 } /* Generic.Inserted */
        .codehilite .go { color: #888888 } /* Generic.Output */
        .codehilite .gp { color: #000080; font-weight: bold } /* Generic.Prompt */
        .codehilite .gs { font-weight: bold } /* Generic.Strong */
        .codehilite .gu { color: #800080; font-weight: bold } /* Generic.Subheading */
        .codehilite .gt { color: #0044DD } /* Generic.Traceback */
        .codehilite .kc { color: #008000; font-weight: bold } /* Keyword.Constant */
        .codehilite .kd { color: #008000; font-weight: bold } /* Keyword.Declaration */
        .codehilite .kn { color: #008000; font-weight: bold } /* Keyword.Namespace */
        .codehilite .kp { color: #008000 } /* Keyword.Pseudo */
        .codehilite .kr { color: #008000; font-weight: bold } /* Keyword.Reserved */
        .codehilite .kt { color: #B00040 } /* Keyword.Type */
        .codehilite .m { color: #666666 } /* Literal.Number */
        .codehilite .s { color: #BA2121 } /* Literal.String */
        .codehilite .na { color: #7D9029 } /* Name.Attribute */
        .codehilite .nb { color: #008000 } /* Name.Builtin */
        .codehilite .nc { color: #0000FF; font-weight: bold } /* Name.Class */
        .codehilite .no { color: #880000 } /* Name.Constant */
        .codehilite .nd { color: #AA22FF } /* Name.Decorator */
        .codehilite .ni { color: #999999; font-weight: bold } /* Name.Entity */
        .codehilite .ne { color: #D2413A; font-weight: bold } /* Name.Exception */
        .codehilite .nf { color: #0000FF } /* Name.Function */
        .codehilite .nl { color: #A0A000 } /* Name.Label */
        .codehilite .nn { color: #0000FF; font-weight: bold } /* Name.Namespace */
        .codehilite .nt { color: #008000; font-weight: bold } /* Name.Tag */
        .codehilite .nv { color: #19177C } /* Name.Variable */
        .codehilite .ow { color: #AA22FF; font-weight: bold } /* Operator.Word */
        .codehilite .w { color: #bbbbbb } /* Text.Whitespace */
        .codehilite .mb { color: #666666 } /* Literal.Number.Bin */
        .codehilite .mf { color: #666666 } /* Literal.Number.Float */
        .codehilite .mh { color: #666666 } /* Literal.Number.Hex */
        .codehilite .mi { color: #666666 } /* Literal.Number.Integer */
        .codehilite .mo { color: #666666 } /* Literal.Number.Oct */
        .codehilite .sa { color: #BA2121 } /* Literal.String.Affix */
        .codehilite .sb { color: #BA2121 } /* Literal.String.Backtick */
        .codehilite .sc { color: #BA2121 } /* Literal.String.Char */
        .codehilite .dl { color: #BA2121 } /* Literal.String.Delimiter */
        .codehilite .sd { color: #BA2121; font-style: italic } /* Literal.String.Doc */
        .codehilite .s2 { color: #BA2121 } /* Literal.String.Double */
        .codehilite .se { color: #BB6622; font-weight: bold } /* Literal.String.Escape */
        .codehilite .sh { color: #BA2121 } /* Literal.String.Heredoc */
        .codehilite .si { color: #BB6688; font-weight: bold } /* Literal.String.Interpol */
        .codehilite .sx { color: #008000 } /* Literal.String.Other */
        .codehilite .sr { color: #BB6688 } /* Literal.String.Regex */
        .codehilite .s1 { color: #BA2121 } /* Literal.String.Single */
        .codehilite .ss { color: #19177C } /* Literal.String.Symbol */
        .codehilite .bp { color: #008000 } /* Name.Builtin.Pseudo */
        .codehilite .fm { color: #0000FF } /* Name.Function.Magic */
        .codehilite .vc { color: #19177C } /* Name.Variable.Class */
        .codehilite .vg { color: #19177C } /* Name.Variable.Global */
        .codehilite .vi { color: #19177C } /* Name.Variable.Instance */
        .codehilite .vm { color: #19177C } /* Name.Variable.Magic */
        .codehilite .il { color: #666666 } /* Literal.Number.Integer.Long */

        /* custom styling */

        .codehilite {
            display: table;
            padding: 15px;
            border-radius: 5px;
            margin-bottom: 15px;
        }
    </style>

    <title> {{ title }} </title>
  </head>
  <body>

    <div class="container">
        {{ content }}
    </div>

    <!-- Option 1: Bootstrap Bundle with Popper -->
    <script 
        src="https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta2/dist/js/bootstrap.bundle.min.js" 
        integrity="sha384-b5kHyXgcpbZJO/tY9Ul7kGkf1S0CWuKcCD38l8YkeH8z8QjE0GmW1gYU5S9FOnJ0" 
        crossorigin="anonymous">
    </script>

  </body>
</html>
"""

def main():

    # create parser and parse input arguments
    parser = argparse.ArgumentParser(
        description="sum the integers at the command line")

    parser.add_argument(
        "markdown_files",
        nargs="+",
        help="markdown-files to be converted to HTML")

    args = parser.parse_args()

    # read markdown-files and convert to HTML
    markdown_files = args.markdown_files
    html_files = []
    append_html = html_files.append

    for markdown_file in markdown_files:
        with open(markdown_file) as md_file:
            content = md_file.read()
            content = markdown2.markdown(content, extras=["fenced-code-blocks"])
            append_html(content)

    # create HTML document from bootstrap-template with converted markdown files
    template = Template(TEMPLATE)
    finished_templates = []
    append_finished = finished_templates.append
    for html_file in html_files:
        markdown_html = template.render(title="My New Markdown", content=html_file)
        append_finished(markdown_html)

    # write html-files
    for index,finished_template in enumerate(finished_templates): 
        with open(f"test_file_{index}.html", "w") as new_file:
            new_file.write(finished_template)


if __name__ == "__main__": 
    main()

