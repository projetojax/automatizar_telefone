import os

base_directory = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

documentation_directory = os.path.join(base_directory, 'doc')
output_directory = os.path.join(base_directory, 'out')
fonts_directory = os.path.join(base_directory, 'fonts')
source_code_directory = os.path.join(base_directory, 'src')
log_directory = os.path.join(base_directory, 'logs')

input_csv = os.path.join(fonts_directory, 'empresas.csv')
output_csv = os.path.join(output_directory, 'empresas.csv')
