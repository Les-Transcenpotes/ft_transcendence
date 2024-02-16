def ensure_JWT(view_func):
    view_func._ensure_JWT = True
    return view_func

def ensure_refresh_token(view_func):
    view_func._ensure_refresh_token = True
    return view_func


