thondef parse_instagram_post(post):
    try:
        user_data = post.get('node', {})
        username = user_data.get('owner', {}).get('username', None)
        return username
    except KeyError as e:
        print(f"Error parsing post data: {e}")
        return None