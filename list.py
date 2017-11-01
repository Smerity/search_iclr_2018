sample = '''<li class="note" data-id="SyyGPP0TZ"><h4>
  <a href="https://openreview.net/forum?id=SyyGPP0TZ&amp;noteId=SyyGPP0TZ">Regularizing and Optimizing LSTM Language Models</a>
    <a href="https://openreview.net/pdf?id=SyyGPP0TZ" class="pdf-link" title="Download PDF" target="_blank"><img src="./ICLR 2018 Conference _ OpenReview_files/pdf_icon_blue.svg"></a>'''

import re

txt = open('iclr.htm').read()

pdf_re = re.compile(r'<a href="([^"]+)" class="pdf-link"')

name_pdf_re = re.compile(r'<a href="([^"]+)" class="pdf-link"')

links = pdf_re.findall(txt)

for i, link in enumerate(links):
  print('echo Paper {} of {}: {}'.format(i, len(links), link.split('?id=')[1]))
  print('wget {} -o {}.pdf'.format(link, link.split('?id=')[1]))
  print('sleep 1')
