import re




def markdown_to_html(markdown_text):


    # Cabeçalhos
    markdown_text = re.sub(r'^(#{1})\s+(.+)$', r'<h1>\2</h1>', markdown_text, flags=re.MULTILINE)
    markdown_text = re.sub(r'^(#{2})\s+(.+)$', r'<h2>\2</h2>', markdown_text, flags=re.MULTILINE)
    markdown_text = re.sub(r'^(#{3})\s+(.+)$', r'<h3>\2</h3>', markdown_text, flags=re.MULTILINE)
    
    # Bold
    markdown_text = re.sub(r'\*{2}([^\s].*[^\s])\*{2}', r'<b>\1</b>', markdown_text)

    # Italic
    markdown_text = re.sub(r'\*([^\s].*[^\s])\*', r'<i>\1</i>', markdown_text)

    # Blockquote
    markdown_text = re.sub(r'^(>+)(.*)', r'<blockquote>\2</blockquote>', markdown_text, flags=re.MULTILINE)

    # Image
    markdown_text = re.sub(r'!\[(.*)\]\((.*)\)', r'<img src="\2" alt="\1"/>', markdown_text)

    # Link
    markdown_text = re.sub(r'\[(.*)\]\((.*)\)', r'<a href="\2">\1</a>', markdown_text)

    # Horizontal Rule
    markdown_text = re.sub(r'^((-\s*){3,})$', r'<hr>', markdown_text, flags=re.MULTILINE)

    # Code
    markdown_text = re.sub(r'`(.*)`', r'<code>\1</code>', markdown_text, flags=re.MULTILINE)

    # Ordered List
    markdown_text = re.sub(r'((\d+\.\s(.+)\n((?!\d+\.\s(.+))(?<!\n{2}).*\n)*)+)', r'<ol>\n\1</ol>\n', markdown_text)
    markdown_text = re.sub(r'\d+\.\s(.*)\n((?!\d+\.\s(.+))(?!</ol>)(?<!\n{2})(?P<line>.*)\n)*', r'<li>\1\g<line></li>\n', markdown_text)

    # Unordered List
    markdown_text = re.sub(r'((-\s(.+)\n((?!-\s(.+))(?<!\n{2}).*\n)*)+)', r'<ul>\n\1</ul>\n', markdown_text)
    markdown_text = re.sub(r'-\s(.*)\n((?!-\s(.+))(?!</ul>)(?<!\n{2})(?P<line>.*)\n)*', r'<li>\1\g<line></li>\n', markdown_text)
    
    return markdown_text


def wrap_in_paragraph(contentHTML):
    return re.sub(r'^(?!\n|<li>|<ul>|</ul>|<ol>|</ol>|<hr>)(.+)', r'<p>\1</p>', contentHTML, flags=re.MULTILINE)


preHTML = """
 <!DOCTYPE html>
<html>
<body>
"""

postHTML = """
</body>
</html> 
"""

file_path = "TEST.md"
with open(file_path, "r") as file:
    markdown_text = file.read()

contentHTML = wrap_in_paragraph(markdown_to_html(markdown_text))

pagHTML = preHTML + contentHTML + postHTML

output_file_path = "output.html"
with open(output_file_path, "w") as output_file:
    output_file.write(pagHTML)
