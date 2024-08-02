import re


def remove_report_emoji(text: str) -> str:
    return text.replace('🚩', '')


def remove_urls_from_images(text: str) -> str:
    return re.sub(r'(!)\[(.*)]\(.*\)', r'\2', text)


def remove_images(text: str) -> str:
    return re.sub(r'(!)\[(.*)]\(.*\)', '', text)


def remove_urls_from_hyperlinks(text: str) -> str:
    return re.sub(r'\[(.*)?]\(.*?\)', r'\1', text)


def remove_hyperlinks(text: str) -> str:
    return re.sub(r'\[(.*)?]\(.*?\)', '', text)


def remove_urls(text: str) -> str:
    return re.sub(r'(http|https)://([\w_-]+(?:(?:\.[\w_-]+)+))([\w.,@?^=%&:/~+#-]*[\w@?^=%&/~+#-])', '', text)


def remove_codeblock(text: str) -> str:
    code_block_pattern_1 = re.compile(r'<code>.*?</code>', re.DOTALL)
    post_without_code_block = re.sub(code_block_pattern_1, '', text)

    code_block_pattern_2 = re.compile(r'```.*?```', re.DOTALL)
    post_without_code_block = re.sub(code_block_pattern_2, '', post_without_code_block)

    return post_without_code_block


def remove_emojis(text: str) -> str:
    return re.sub(r'[\U00010000-\U0010ffff]', '', text)


if __name__ == '__main__':
    image = '''RuntimeError


![image.png](https://cdn-uploads.huggingface.co/production/uploads/636da884c4a7a729c162a94e/8On-4oqtluQl2EplsXJmc.png)
this bug huppened when I run the code

![image.png](https://cdn-uploads.huggingface.co/production/uploads/636da884c4a7a729c162a94e/1ZDs7JOMVMLbROpo-4GcZ.png)
'''
    print(image)
    print(remove_urls_from_images(image))
    print(remove_images(image))
    print(remove_emojis(image))
