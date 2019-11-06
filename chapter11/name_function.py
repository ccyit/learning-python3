def get_formatted_name(first, last, middle=''):
    """产生一个整洁的名字"""
    if middle:
        full_name = first + ' ' + middle + ' ' + last
    else:
        full_name = first + ' ' + last
    return full_name.title()


if __name__ == "__main__":
    formatted_name = get_formatted_name('janis', 'joplin')
    print(formatted_name)
