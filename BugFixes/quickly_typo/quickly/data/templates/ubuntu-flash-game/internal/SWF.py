import struct, zlib

class SWFNotASWF(Exception): pass
class SWFNoDimensions(Exception): pass

def parse(input):
    """Parses the header information from an SWF file.
    Code from http://pypi.python.org/pypi/hexagonit.swfheader, GPL licenced."""
    if hasattr(input, 'read'):
        input.seek(0)
    else:
        input = open(input, 'rb')

    def read_ui8(c):
        return struct.unpack('<B', c)[0]
    def read_ui16(c):
        return struct.unpack('<H', c)[0]
    def read_ui32(c):
        return struct.unpack('<I', c)[0]

    header = {}

    # Read the 3-byte signature field
    signature = ''.join(struct.unpack('<3c', input.read(3)))
    if signature not in ('FWS', 'CWS'):
        raise ValueError('Invalid SWF signature: %s' % signature)

    # Compression
    header['compressed'] = signature.startswith('C')

    # Version
    header['version'] = read_ui8(input.read(1))

    # File size (stored as a 32-bit integer)
    header['size'] = read_ui32(input.read(4))

    # Payload
    buffer = input.read(header['size'])
    if header['compressed']:
        # Unpack the zlib compression
        buffer = zlib.decompress(buffer)

    # Containing rectangle (struct RECT)

    # The number of bits used to store the each of the RECT values are
    # stored in first five bits of the first byte.
    nbits = read_ui8(buffer[0]) >> 3

    current_byte, buffer = read_ui8(buffer[0]), buffer[1:]
    bit_cursor = 5

    for item in 'xmin', 'xmax', 'ymin', 'ymax':
        value = 0
        for value_bit in range(nbits-1, -1, -1): # == reversed(range(nbits))
            if (current_byte << bit_cursor) & 0x80:
                value |= 1 << value_bit
            # Advance the bit cursor to the next bit
            bit_cursor += 1

            if bit_cursor > 7:
                # We've exhausted the current byte, consume the next one
                # from the buffer.
                current_byte, buffer = read_ui8(buffer[0]), buffer[1:]
                bit_cursor = 0

        # Convert value from TWIPS to a pixel value
        header[item] = value / 20

    header['width'] = header['xmax'] - header['xmin']
    header['height'] = header['ymax'] - header['ymin']
    
    header['frames'] = read_ui16(buffer[0:2])
    header['fps'] = read_ui16(buffer[2:4])

    input.close()
    return header


def dimensions(swf):
    """Read the dimensions of a SWF, as per the Adobe spec.
       Spec downloaded from http://www.adobe.com/devnet/swf.html."""
    try:
        details = parse(swf)
    except:
        raise SWFNotASWF
    try:
        return (details["width"], details["height"])
    except:
        raise SWFNoDimensions
