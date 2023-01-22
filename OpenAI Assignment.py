import openai
from base64 import b64encode
from requests import get, post
from functions import h2, paragraph

# WordPress Data
wpuser = 'arifitdev@gmail.com'
wppass = 'PHP7 hETy zsow 6hpu gnDJ N7gJ'
credientials = f'{wpuser}:{wppass}'
token = b64encode(credientials.encode())
wpheader = {'Authorization': f'Basic {token.decode("utf-8")}'}

openai.api_key = "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"


def oai(prompt):
    response = openai.Completion.create(
        model="text-davinci-003",
        prompt=prompt,
        temperature=0.7,
        max_tokens=256,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0
    )
    output = response.get('choices')[0].get('text')
    return output


# Read file from computer
file = open('keywords.txt', 'r+')
keywords = file.readlines()
file.close()
# print(keywords)

# make a blank list and append the keyword to it.
key_list = []
for key in keywords:
    keyword = key.rstrip('\n')
    key_list.append(keyword)

# accessing the single key using while loop
i = 0
while i < len(key_list):
    signle_key = key_list[i]
    i += 1
    intro_prompt = f'write intro about {signle_key}'
    intro = oai(intro_prompt)
    heading1 = f'What is a {signle_key}?'
    heading1_pera = oai(heading1)
    # print(paragraph(heading1_pera))
    heading2 = f'Why {signle_key} is important?'
    heading2_pera = oai(heading2)
    heading3 = f'How to Choose {signle_key}?'
    heading3_pera = oai(heading3)
    heading4 = f'Best Features of {signle_key}'
    heading4_pera = oai(heading4)
    heading5 = f'Conclusion about {signle_key}'
    heading5_pera = oai(heading5)

    # wordPress content generate
    intro = paragraph(intro)
    head1 = h2(heading1)
    head1_pera = paragraph(heading1_pera)
    head2 = h2(heading2)
    head2_pera = paragraph(heading2_pera)
    head3 = h2(heading3)
    head3_pera = paragraph(heading3_pera)
    head4 = h2(heading4)
    head4_pera = paragraph(heading4_pera)
    head5 = h2(heading5)
    head5_pera = paragraph(heading5_pera)

    content = f'{intro} {head1} {head1_pera} {head2} {head2_pera} {head3} {head3_pera} {head4} {head4_pera} {head5} {head5_pera}'

    title = f'Best {signle_key} in 2023'

    data = {
        'title': title.title(),
        'content': content,
        'slug': signle_key.strip().lower().replace(' ', '-')
    }
    api_url = 'https://wordpress-880942-3117404.cloudwaysapps.com/wp-json/wp/v2/posts'
    response = post(api_url, headers=wpheader, json=data)
    print(f'{title} is posted successfully')
