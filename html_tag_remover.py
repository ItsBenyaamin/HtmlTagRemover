import re
from scrapy import Selector

class HtmlTagRemover():
    final_callback = callable
    body = ""
    last_tag_name = ""

    def __init__(self, callback, html_body):
        self.final_callback = callback
        self.body = html_body
        self.parse()

    def parse(self):
        tag_start_position = 0
        tag_end_position   = 0
        tag_name_start     = False
        tag_detection      = False
        tag_name           = ""
        is_clear_text      = True

        for index in range(0, len(self.body)):
            char = self.body[index]
            if char == "<":
                tag_name_start     = True
                tag_name          += char
                tag_detection          = True
                is_clear_text          = False
                tag_start_position     = index
            elif char == ">":
                if tag_detection:
                    tag_name          += char
                    tag_end_position   = index
                    if tag_name.startswith("<li"):
                        self.body      = self.body[0:tag_start_position] + "\n" + self.body[tag_end_position + 1::]
                    elif tag_name.startswith("<img"):
                        select = Selector(tag_name)
                        link = "!i " + select.xpath('//img/@src').extract()[0] + " i!"
                        self.body      = self.body[0:tag_start_position] + "\n" + link + "\n" + self.body[tag_end_position + 1::]
                    elif tag_name.startswith("<script"):
                        script = "!s " + self.body[tag_start_position + 1 : tag_end_position] + " s!"
                        self.body      = self.body[0:tag_start_position] + "\n" + script + "\n" + self.body[tag_end_position + 1::]
                    elif tag_name.startswith("<blockquote"):
                        self.body      = self.body[0:tag_start_position] + "\n!b " + self.body[tag_end_position + 1::]
                    elif tag_name.startswith("</blockquote"):
                        self.body      = self.body[0:tag_start_position] + " b!\n" + self.body[tag_end_position + 1::]
                    elif tag_name.startswith("<ul"):
                        self.body      = self.body[0:tag_start_position] + "\n" + self.body[tag_end_position + 1::]
                    elif tag_name.startswith("</ul"):
                        self.body      = self.body[0:tag_start_position] + "\n" + self.body[tag_end_position + 1::]
                    elif tag_name.startswith("h1") or tag_name.startswith("h2") or tag_name.startswith("h3") or tag_name.startswith("h4") or tag_name.startswith("h5") or tag_name.startswith("h6"):
                        self.body      = self.body[0:tag_start_position] + "\n" + self.body[tag_end_position + 1::]
                    else:
                        self.body  = self.body[0:tag_start_position] + self.body[tag_end_position + 1::]

                    self.last_tag_name = tag_name
                    tag_detection      = False
                    tag_name_start     = False
                    tag_name           = ""
                    
                break
            else:
                if tag_name_start:
                    tag_name          += char

        if not is_clear_text:
            self.parse()
        else:
            self.on_finished(self.body)

    def on_finished(self, body):
        self.final_callback(body)
        print("finished! all html tags are removed.")