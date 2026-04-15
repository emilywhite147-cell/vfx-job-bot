def is_relevant_job(title: str, text: str = "") -> bool:
    text_all = (title + " " + text).lower()

    roles = [
        "vfx producer",
        "production manager",
        "vfx production manager",
        "line producer"
    ]

    locations = [
        "london",
        "uk",
        "united kingdom"
    ]

    # must match role
    role_match = any(role in text_all for role in roles)

    # must match location
    location_match = any(loc in text_all for loc in locations)

    return role_match and location_match
