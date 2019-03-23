import re


class HtmlTagRemover():
    body = ""
    last_non_tag_index = 0
    last_tag_name = ""

    def __init__(self, html_body):
        self.body = html_body
        self.parse(0)

    def parse(self, start_index):
        tag_start_position = 0
        tag_end_position   = 0
        tag_name_start     = False
        tag_detection      = False
        tag_name           = ""
        is_clear_text      = True

        for index in range(0, len(self.body)):
            char = self.body[index]
            self.last_non_tag_index    = index - 1
            if char == "<":
                if self.body[index + 1] != "/":
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
                        img_body       = re.split('"', tag_name)
                        link           = ""
                        for img_index in range(0, len(img_body)):
                            if(img_body[img_index].startswith("http://") or img_body[img_index].startswith("https://")):
                                link   = '//' + img_body[img_index] + '//'
                                break
                        self.body      = self.body[0:tag_start_position] + "\n" + link + "\n" + self.body[tag_end_position + 1::]
                    elif "span" in tag_name:
                        self.body      = self.body[0:tag_start_position] + "\n" + self.body[tag_end_position + 1::]
                    else:
                        if self.last_tag_name.startswith("<li"):
                            self.body  = self.body[0:tag_start_position] + "\n \n" + self.body[tag_end_position + 1::]
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
            self.parse(self.last_non_tag_index)
        else:
            print("done!\n\n")
            print(self.body)

    def write(self):
        with open("result.txt", "w", encoding="utf-8") as file:
            file.write(self.body)