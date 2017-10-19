from config import sessions
functions = []


class Misery(Exception):
    pass


def passer(*args, **kwargs):
    def decorator(func):
        def wrapped_func(*args, **kwargs):
            try:
                result = func(*args, **kwargs)
                if result:
                    return result
                raise Misery()
            except Exception as e:
                if type(e) is not Misery:
                    print('**error**.{}'.format(e))
                raise Misery()

        functions.append(wrapped_func)
    return decorator


def handle(session):
    for func in functions:
        try:
            return func(session)
        except Misery:
            pass
    sessions.save(session)
    return 'no body was responsible'
