import argparse, easydict


def ipython_args(args_dict: dict):
    if is_notebook():
        args = easydict.EasyDict()
        for key, value in args_dict.items():
            args[key] = value
        return args
    else:
        parser = argparse.ArgumentParser()
        for key, value in args_dict.items():
            parser.add_argument('--'+key, type=type(value), default=value)
        return parser.parse_args()
    
def is_notebook() -> bool:
    try:
        shell = get_ipython().__class__.__name__
        if shell == 'ZMQInteractiveShell':
            return True   # Jupyter notebook or qtconsole
        elif shell == 'TerminalInteractiveShell':
            return False  # Terminal running IPython
        else:
            return False  # Other type (?)
    except NameError:
        return False      # Probably standard Python interpreter