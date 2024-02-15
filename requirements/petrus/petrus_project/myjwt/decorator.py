def exempt_JWT(view_func):
    view_func._skip_JWT = True
    return view_func

