def get_average_rating(books):
    if not books:
        return 0
    total = sum(book['rating'] for book in books)
    return round(total / len(books), 2)

def get_author_statistics(books):
    if not books:
        return {}
    stats = {}
    for book in books:
        author = book['author']
        if author not in stats:
            stats[author] = []
        stats[author].append(book['rating'])

    author_stats = {}
    for author, ratings in stats.items():
        author_stats[author] = {
            "count": len(ratings),
            "avg_rating": round(sum(ratings) / len(ratings), 2)
        }
    return author_stats
