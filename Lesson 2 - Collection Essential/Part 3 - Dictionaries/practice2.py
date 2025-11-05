def calculate_engagement_rate(post):
    likes = post.get("likes")
    comments = post.get("comments")
    shares = post.get("shares")
    views = post.get("views")

    engagement = likes + comments + shares
    rate = (engagement / views) * 100
    if views == 0 or "":
        return 0
    return f"{rate:.2f}"
    # return round(rate, 2)


post = {"views": 1000, "likes": 50, "comments": 10, "shares": 5}
print(calculate_engagement_rate(post))  # 6.5
