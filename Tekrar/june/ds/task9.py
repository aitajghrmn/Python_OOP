filmler = [
    {"ad": "Inception", "imdb": 8.8},
    {"ad": "Interstellar", "imdb": 8.6},
    {"ad": "The Batman", "imdb": 7.9},
    {"ad": "Avatar 2", "imdb": 7.6}
]

trending=[x["ad"] for x in filmler if x["imdb"] > 8 ]
print(trending)