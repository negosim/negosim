import importlib.util


def get_object(package_name, file_name, *init_args):
    file_name = text_splitor(file_name, '.')[0]
    spec = importlib.util.spec_from_file_location(file_name, f"{package_name}/{file_name}.py")
    foo = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(foo)
    klass = getattr(foo, file_name)
    obj = klass(*init_args)
    return obj


def text_splitor( text, separator):
    seperated_text_list = str(text).split(separator)
    return seperated_text_list