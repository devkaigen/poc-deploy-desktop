import sys
from cx_Freeze import setup, Executable

pyhtondll_path = "C:\Program Files\WindowsApps\PythonSoftwareFoundation.Python.3.10_3.10.2800.0_x64__qbz5n2kfra8p0"

# Dependencies are automatically detected, but it might need fine tuning.
build_exe_options = {
    "packages": ["tkinter"],
    "include_files": ["calc.py", "window.py", r"C:\\Program Files\\WindowsApps\\PythonSoftwareFoundation.Python.3.10_3.10.2800.0_x64__qbz5n2kfra8p0\\python310.dll"],
    'include_msvcr': True
}

# GUI applications require a different base on Windows (the default is for a console application).
base = None
if sys.platform == "win32":
    base = "Win32GUI"

setup(
    name="Calculator",
    version="0.1",
    description="A simple calculator app",
    options={"build_exe": build_exe_options},
    executables=[Executable("window.py", base=base)],
)
