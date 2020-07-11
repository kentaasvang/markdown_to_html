import argparse
from markdown2 import Markdown
from jinja2 import Template


TEMPLATE = """
<!doctype html>
<html lang="en">
    <head>
        <!-- Required meta tags -->
        <meta charset="utf-8">
        <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">

        <!-- Bootstrap CSS -->
        <link rel="stylesheet" 
              href="https://stackpath.bootstrapcdn.com/bootstrap/4.5.0/css/bootstrap.min.css" 
              integrity="sha384-9aIt2nRpC12Uk9gS9baDl411NQApFmC26EwAOH8WgZl5MYYxFfc+NcPb1dKGj7Sk" 
              crossorigin="anonymous">

        <title>{{ title }}</title>
    </head>
    <body>
    
        <div class="container">
            {{ content }}
        </div>

        <!-- Optional JavaScript -->
        <!-- jQuery first, then Popper.js, then Bootstrap JS -->
        <script src="https://code.jquery.com/jquery-3.5.1.slim.min.js" 
                integrity="sha384-DfXdz2htPH0lsSSs5nCTpuj/zy4C+OGpamoFVy38MVBnE+IbbVYUew+OrCXaRkfj" 
                crossorigin="anonymous"></script>
        <script src="https://cdn.jsdelivr.net/npm/popper.js@1.16.0/dist/umd/popper.min.js" 
                integrity="sha384-Q6E9RHvbIyZFJoft+2mJbHaEWldlvI9IOYy5n3zV9zzTtmI3UksdQRVvoxMfooAo" 
                crossorigin="anonymous"></script>
        <script src="https://stackpath.bootstrapcdn.com/bootstrap/4.5.0/js/bootstrap.min.js" 
                integrity="sha384-OgVRvuATP1z7JjHLkuOU7Xw704+h835Lr+6QL9UvYjZE3Ipu6Tp75j7Bh/kR0JKI" 
                crossorigin="anonymous"></script>
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

    # create HTML document from bootstrap-template with html-converted markdown files
    template = Template(TEMPLATE)
    for html_file in html_files:
        markdown_html = template.render(title="My New Markdown", content=html_file)
        with open("test_file.html", "w") as new_file:
            new_file.write(markdown_html)



if __name__ == "__main__": 
    main()

    
