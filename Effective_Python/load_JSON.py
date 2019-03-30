def decode(data, default={}):
    try:
        return json.loads(data)
    except ValueError:
        return default
