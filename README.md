# HtmlTagRemover
a python class for remove html tags from string

### how to use
first import the class where ever you want, then:
```
from html_tag_remover import HtmlTagRemover

body = "<body><p>P tag</p><ul><li>LI tag</li></ul></body>"
HtmlTagRemover(body)
```
and the result is :

![Image of Yaktocat](result.png)

### PS:
`<li>` tags each export in new line

`<img>` link of the images are extracted with format : !i https://site.com/images/img.png i!

`<a>` just text of this tags will export

`<blockquote>` extracted as : !b this is blockquote b!

`<script>` if there is script like Aparat.com or Youtube.com or any script from another websites will extracted as (just inside of tag): !s script ... s!

also you can change result as you wants `But dont put results in '<>' because they removed by script :D`

have fun :)
