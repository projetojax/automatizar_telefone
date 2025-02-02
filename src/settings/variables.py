from .paths import (
    documentation_directory,
    output_directory,
    fonts_directory,
    source_code_directory,
    log_directory
)

required_directories : list = [
    documentation_directory,
    output_directory,
    fonts_directory,
    source_code_directory,
    log_directory
]

required_packages : list = [
    'pandas',
    'logging',
    'os',
    'subprocess',
    'sys',
    'requests',
    'bs4',
    're',
    'flask'
]

