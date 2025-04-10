def format_datetime(value, fmt='%Y년 %m월 %d일 %p %I:%M'):
    return value.strftime(fmt)

import markdown

def format_markdown(text):
    # 텍스트가 None이거나 비어있으면 빈 문자열 반환
    if not text:
        return ''
    
    # markdown 라이브러리로 HTML 변환
    extensions = ['nl2br', 'fenced_code']
    return markdown.markdown(text, extensions=extensions)