import sys
assert sys.int_info.default_max_str_digits == 4300, sys.int_info
assert sys.int_info.str_digits_check_threshold == 640, sys.int_info
msg = int('578966293710682886880994035146873798396722250538762761564'
          '9252925514383915483333812743580549779436104706260696366600'
          '571186405732').to_bytes(53, 'big')
