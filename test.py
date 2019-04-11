from html_tag_remover import HtmlTagRemover

def result(body):
    print("clear text :" + body)


test = HtmlTagRemover(result, "<body><p>P tag</p><ul><li>LI tag</li></ul></body>")