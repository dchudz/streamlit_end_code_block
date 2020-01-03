"""
This file implements a function you can use to make streamlit output more like a notebook.

I am not affiliated with the Streamlit team in any way.

Feel free to copy/paste this code to anywhere you want.
"""
import traceback
import sys

import streamlit as st
from streamlit.source_util import open_python_file

_current_end_line = 0
_space_for_code = st.empty()

assert sys.version_info >= (3, 4)

def end_code_block(display=True):
    """Ends the current code block and sends it to streamlit output.

    Args:
        display: whether to show this code block in the output
    """
    global _current_end_line
    global _space_for_code
    frame = traceback.extract_stack()[-2]  # stack[-1] would be this frame itself
    # stack[-2] is the frame in the user's "notebook" calling us
    # (as long as the user is calling us directly)
    filename, lineno = frame.filename, frame.lineno
    with open_python_file(filename) as source_file:
        source_lines = source_file.readlines()
    lines_to_display = source_lines[_current_end_line:(lineno - 1)]  # `lineno-1` means we skip showing the call to us
    _current_end_line = lineno
    if display:
        _space_for_code.code(''.join(lines_to_display), 'python')
    _space_for_code = st.empty()
