def clip(text, max_len=80):
    """cut the text before or after the max length"""
    end = None
    if len(text) > max_len:
        space_before = text.rfind(' ', 0, max_len)
        if space_before >= 0:
            end = space_before
        else:
            space_after = text.rfind(' ', max_len)
            if space_after >= 0:
                end = space_after
    if end is None:  # There is no space
        end = len(text)
    return text[:end].rstip()
