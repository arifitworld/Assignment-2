import openai
from base64 import b64encode
from requests import get, post

# functions
def paragraph(text):
    '''
  :param text: enter your text
  :return: It will return you  gutenberg fromatted paragraph code.
  '''
    code = f'<!-- wp:paragraph --><p>{text}</p><!-- /wp:paragraph -->'
    return code


def h2(text):
    '''
  :param text: Enter the title text
  :return: it will return gutenberg H2 tag.
  '''
    code = f'<!-- wp:heading --><h2>{text}</h2><!-- /wp:heading -->'
    return code