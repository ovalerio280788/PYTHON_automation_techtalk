singleton_instances = {}


def singleton(class_):
    def getinstance(*args, **kwargs):
        if class_ not in singleton_instances:
            singleton_instances[class_] = class_(*args, **kwargs)
        return singleton_instances[class_]

    return getinstance
