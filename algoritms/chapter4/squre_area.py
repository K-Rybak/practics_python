def find_large_area(w, h):
    if w % h == 0:
        return w / h
    else:
        return find_large_area()