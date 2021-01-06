"""Utils to display to be returned to the user on the console."""
import os
import string

import termcolor


def get_template_dir_path():
    """Return the path of the template's directory.
    
    Returns:
        str: the template dir path.
    """
    template_dir_path = None
    try:
        import settings
        if settings.TEMPLATE_PATH:
            template_dir_path = settings.TEMPLATE_PATH
    except ImportError:
        pass

    if not template_dir_path:
        base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        template_dir_path = os.path.join(base_dir, 'templates')

    return template_dir_path


class NoTemplateError(Exception):
    """No Template Error"""


def find_template(temp_file):
    """Find for template file in the given location.

    Returns:
        NoTemplateError: If the fil does not exists.
    """
    template_dir_path = get_template_dir_path()
    temp_file_path = os.path.join(template_dir_path, temp_file)
    if not os.path.exists(temp_file_path):
        raise NoTemplateError('Could not find {}'.format(temp_file))
    return temp_file_path


def get_template(template_file_path, color=None):
    """Return the path of the template.

    Args:
        template_file_path (stre): The template file path
        color: (str): Color formatting for output in terminal
            See in more details: https://pypi.python.org/pypi/termcolor

    Returns:
        string.Template: Return templates with characters in templates.
    """
    template = find_template(template_file_path)
    with open(template, 'r', encoding='utf-8') as template_file:
        # ファイルの内容を読み込む
        contents = template_file.read()
        # 改行コードを削除
        contents = contents.rstrip(os.linesep)
        # ファイルの内容の前後に=を60個連結させて枠を付ける装飾をしている
        contents = '{splitter}{sep}{contents}{sep}{splitter}{sep}'.format(
            contents=contents, splitter="=" * 60, sep=os.linesep)
        # 出力時の文字色を指定
        contents = termcolor.colored(contents, color)
        return string.Template(contents)
