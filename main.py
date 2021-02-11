import argparse
from markdown2 import Markdown
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
    convert_markdown = Markdown().convert
    append_html = html_files.append

    for markdown_file in markdown_files:
        with open(markdown_file) as md_file:
            content = md_file.read()
            content = convert_markdown(content)
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

    
