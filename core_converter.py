import markdown


def convert_markdown_to_html(markdown_text):
    """Converts a string of markdown to HTML"""
    try:
        html = markdown.markdown(markdown_text, extensions=[
                                 'fenced_code', 'tables'])
        return html
    except Exception as e:
        return f'Error converting mardown : {e}'


if __name__ == "__main__":
    sample_markdown = """
    # Hello World!

    This is a *sample* example.

    - Item 1
    - Item 2
    ```python
    print("Hello form the code block")
    """

    html_output = convert_markdown_to_html(sample_markdown)
    print("-----Sample Markdown----")
    print(sample_markdown)
    print("\n----Generated HTML----")
    print(html_output)
