import hashlib
import os
import tempfile

from communal.hashing import checksum, crc32_unsigned


def test_crc32_unsigned():
    result1 = crc32_unsigned("test string")
    result2 = crc32_unsigned("test string")
    result3 = crc32_unsigned("different string")

    assert isinstance(result1, int)
    assert result1 == result2
    assert result1 != result3
    assert result1 >= 0


def test_checksum_md5():
    with tempfile.NamedTemporaryFile(mode="w", delete=False) as f:
        f.write("test content")
        temp_path = f.name

    try:
        md5_hash = checksum(temp_path, "md5")
        assert isinstance(md5_hash, str)
        assert len(md5_hash) == 32

        # Verify it matches hashlib
        with open(temp_path, "rb") as f:
            expected = hashlib.md5(f.read()).hexdigest()
        assert md5_hash == expected
    finally:
        os.unlink(temp_path)


def test_checksum_sha1():
    with tempfile.NamedTemporaryFile(mode="w", delete=False) as f:
        f.write("test content")
        temp_path = f.name

    try:
        sha1_hash = checksum(temp_path, "sha1")
        assert isinstance(sha1_hash, str)
        assert len(sha1_hash) == 40
    finally:
        os.unlink(temp_path)


def test_checksum_invalid_hashfunc():
    with tempfile.NamedTemporaryFile(mode="w", delete=False) as f:
        f.write("test")
        temp_path = f.name

    try:
        try:
            checksum(temp_path, "invalid_hash")
            raise AssertionError("Should have raised ValueError")
        except ValueError:
            pass
    finally:
        os.unlink(temp_path)
