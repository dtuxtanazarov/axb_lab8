#   python receiver.py --file covert.tmp --bit-duration 0.6 --timeout 30
import os
import time
import argparse

def bits_to_bytes(bits: str) -> bytes:
    pad = (8 - (len(bits) % 8)) % 8
    bits += '0' * pad
    b = bytearray()
    for i in range(0, len(bits), 8):
        b.append(int(bits[i:i+8], 2))
    return bytes(b)

def sample_bit(path: str) -> str:
    return '1' if os.path.exists(path) else '0'

def receive(path: str, bit_duration: float, timeout: float):
    window = ''
    start_time = time.monotonic()
    last_activity = start_time
    print('Listening for preamble...')
    while True:
        bit = sample_bit(path)
        window = (window + bit)[-8:]
        if window == '1' * 8:
            print('Preamble detected.')
            break
        time.sleep(bit_duration)
        if timeout is not None and (time.monotonic() - start_time) > timeout:
            print('Timeout waiting for preamble.')
            return None
    length_bits = ''
    for i in range(16):
        time.sleep(bit_duration)
        b = sample_bit(path)
        length_bits += b
        print(f'Read length bit {i+1}/16: {b}')
    length = int(length_bits, 2)
    print(f'Payload length (bytes): {length}')
    payload_bits = ''
    total_bits = length * 8
    for i in range(total_bits):
        time.sleep(bit_duration)
        b = sample_bit(path)
        payload_bits += b
        if (i+1) % 8 == 0:
            print(f'Read payload byte {(i+1)//8}/{length}')
    data = bits_to_bytes(payload_bits)
    try:
        message = data.decode('utf-8')
    except UnicodeDecodeError:
        message = data.decode('utf-8', errors='replace')
    print('Received message:', message)
    return message

def main():
    p = argparse.ArgumentParser()
    p.add_argument('--file', default='covert_channel.tmp')
    p.add_argument('--bit-duration', type=float, default=0.6)
    p.add_argument('--timeout', type=float, default=60.0)
    args = p.parse_args()
    print('Start receiver. Make sure to run receiver BEFORE sender.')
    receive(args.file, args.bit_duration, args.timeout)

if __name__ == '__main__':
    main()
