def get_web(url):
    """ URL을 넣으면 페이지를 가져온다 """
    import urllib.request
    response = urllib.request.urlopen(url)
    data = response.read()
    decoded = data.decode("utf-8")
    return decoded

url = input()
content=get_web(url)
print(content)
