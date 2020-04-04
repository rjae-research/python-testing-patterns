def not_none(target):
    def verify_not_none(*args, **kwargs):
        if None in args or None in kwargs.values():
            raise ValueError(f"{target.__name__} cannot be None")
        return target(*args, **kwargs)
    return verify_not_none
