

def check_value(value: bytearray, size_value: int) -> bool:
    result = True
    if (not isinstance(value, (bytes, bytearray))) or len(value) != size_value:
        result = False
    return result


def msb(value: bytearray) -> int:
    return value[-1] & 0x80


def add_xor(op_a: bytearray, op_b: bytearray) -> bytearray:
    op_a = bytearray(op_a)
    op_b = bytearray(op_b)
    result_len = min(len(op_a), len(op_b))
    result = bytearray(result_len)
    for i in range(result_len):
        result[i] = op_a[i] ^ op_b[i]
    return result


def zero_fill(value: bytearray) -> bytearray:
    result = b''
    if isinstance(value, (bytes, bytearray)):
        result = b'/x00' * len(value)
        result = bytearray(result)
    return result


def bytearray_to_int(value: bytearray) -> int:
    return int.from_bytes(value, byteorder='big')


def int_to_bytearray(value: int, num_byte: int) -> bytearray:
    return bytearray(
        [(value & (0xff << pos * 8)) >> pos * 8 for pos in range(num_byte - 1, -1, -1)]
    )


def compare(op_a: bytearray, op_b: bytearray) -> bool:
    op_a = bytearray(op_a)
    op_b = bytearray(op_b)
    res_check = 0
    if len(op_a) != len(op_b):
        return False
    for i in enumerate(op_a):
        check = op_a[i[0]] ^ op_b[i[0]]
        res_check = res_check + check
    return not res_check


def compare_to_zero(value: bytearray) -> bool:
    value = bytearray(value)
    res_check = 0
    for i in enumerate(value):
        check = value[i[0]] ^ 0x00
        res_check = res_check + check
    return not res_check
