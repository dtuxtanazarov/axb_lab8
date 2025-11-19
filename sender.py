#   python sender.py "Hello world!" --file covert.tmp --bit-duration 0.6
import os
import time
import argparse

def bytes_to_bits(b: bytes) -> str:
    return ''.join(f'{byte:08b}' for byte in b)

def send_bit(path: str, bit: str):
    if bit == '1':
        with open(path, 'wb') as f:
            f.write(b'1')
            f.flush()
            os.fsync(f.fileno())
    else:
        try:
            os.remove(path)
        except FileNotFoundError:
            pass

def send_message(message: str, path: str, bit_duration: float):
    data = message.encode('utf-8')
    preamble = '1' * 8
    length = len(data)
    if length > 65535:
        raise ValueError('xabar juda uzun (>65535 bayt)')
    length_bits = f'{length:016b}'
    payload_bits = bytes_to_bits(data)
    bits = preamble + length_bits + payload_bits
    print(f'Sending: preamble + length({length}) + payload ({len(payload_bits)} bits) = total {len(bits)} bits')
    for i, bit in enumerate(bits, start=1):
        send_bit(path, bit)
        print(f'Sent bit {i}/{len(bits)}: {bit}')
        time.sleep(bit_duration)
    try:
        os.remove(path)
    except FileNotFoundError:
        pass
    print('Done sending.')

def main():
    p = argparse.ArgumentParser()
    p.add_argument('message')
    p.add_argument('--file', default='covert_channel.tmp')
    p.add_argument('--bit-duration', type=float, default=0.6)
    args = p.parse_args()
    send_message(args.message, args.file, args.bit_duration)

if __name__ == '__main__':
    main()
