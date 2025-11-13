import os
import tempfile

from communal.files import cd, copy_file, ensure_dir, remove_file


def test_ensure_dir():
    with tempfile.TemporaryDirectory() as tmpdir:
        test_dir = os.path.join(tmpdir, "test", "nested", "dir")
        ensure_dir(test_dir)
        assert os.path.exists(test_dir)
        assert os.path.isdir(test_dir)


def test_copy_file():
    with tempfile.TemporaryDirectory() as tmpdir:
        source = os.path.join(tmpdir, "source.txt")
        dest = os.path.join(tmpdir, "dest.txt")

        with open(source, "w") as f:
            f.write("test content")

        result = copy_file(source, dest)
        assert result == dest
        assert os.path.exists(dest)

        with open(dest) as f:
            assert f.read() == "test content"


def test_remove_file():
    with tempfile.TemporaryDirectory() as tmpdir:
        test_file = os.path.join(tmpdir, "test.txt")
        with open(test_file, "w") as f:
            f.write("test")

        assert os.path.exists(test_file)
        remove_file(test_file)
        assert not os.path.exists(test_file)


def test_cd_context_manager():
    original_cwd = os.getcwd()
    with tempfile.TemporaryDirectory() as tmpdir:
        with cd(tmpdir):
            assert os.path.realpath(os.getcwd()) == os.path.realpath(tmpdir)
        assert os.getcwd() == original_cwd
