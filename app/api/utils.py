def generate_code(url):
    converted_url = sum(map(ord, url))
    mod = converted_url % 100000
    code = f"{mod:05}"
    return code
