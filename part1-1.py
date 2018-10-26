from collections import Counter

urls = [
    "http://www.google.com/a.txt",
    "http://www.google.com.tw/a.txt",
    "http://www.google.com/download/c.jpg",
    "http://www.google.co.jp/a.txt",
    "http://www.google.com/b.txt",
    "https://facebook.com/movie/b.txt",
    "http://yahoo.com/123/000/c.jpg",
    "http://gliacloud.com/haha.png",
]

def sort(urls):
    data = []
    for url in urls:
        last = url.split('/')[-1]
        data.append(last)

    sort = Counter(data)
    top_three = sort.most_common(3)
    return top_three

print(sort(urls))
