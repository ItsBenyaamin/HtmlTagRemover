from html_tag_remover import HtmlTagRemover

def result(result):
    print("clear text :\n" + result)


test = HtmlTagRemover(result, "<body><p>P tag</p><ul><li>LI tag</li></ul></body>")