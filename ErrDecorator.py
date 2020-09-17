import os


class NotNameError(Exception):
    """
    self-written exception
    serves to give text for recording
    """

    def __str__(self):
        return 'it is not name!'


class NotEmailError(Exception):
    """
    self-written exception
    serves to give text for recording
    """

    def __str__(self):
        return 'it is not email!'


def log_errors(bad_dst):
    """
    a function that takes a parameter - the recording path
    this is a decorator
    if there is no exception in the function being decorated
    then the this decorator won't work
    """

    def get_log_errors(func):
        def surrogate(*args, **kwargs):
            try:
                result = func(*args, **kwargs)
                return result
            except (ValueError, NotNameError, NotEmailError) as exc:
                with open(os.path.join(bad_dst), "a", encoding='utf-8') as file:
                    file.write(f'{exc} type {type(exc)} \n')
                raise exc

        return surrogate

    return get_log_errors
