print(repr(('%#x' % 255, '%x' % 255, '%X' % 255)))
print(repr((format(255, '#x'), format(255, 'x'), format(255, 'X'))))
print(repr((f'{255:#x}', f'{255:x}', f'{255:X}')))
