from copy2hash import copy2hash
import hashlib as hashlib

__refargs__ = {
    "infile": [],
    "report": ["json"],
    "report_name": "copy_report",
    "sha": ["sha256"],
    "directory": None,
    "move": False,
    "file_extension": False,
    "file_suffix": False,
    "no_file_extension": False,
    "verbose": False,
    "version": False,
}


class TestSHA(object):
    fpath = "sha_key_test"

    def test_sha1(self):
        hashlib_result = hashlib.sha1(self.fpath.encode("utf-8")).hexdigest()
        copy2hash_result = copy2hash.HashTag(args={}).fpath2hash(self.fpath, key="sha1")
        assert hashlib_result == copy2hash_result

    def test_sha224(self):
        hashlib_result = hashlib.sha224(self.fpath.encode("utf-8")).hexdigest()
        copy2hash_result = copy2hash.HashTag(args={}).fpath2hash(
            self.fpath, key="sha224"
        )
        assert hashlib_result == copy2hash_result

    def test_sha256(self):
        hashlib_result = hashlib.sha256(self.fpath.encode("utf-8")).hexdigest()
        copy2hash_result = copy2hash.HashTag(args={}).fpath2hash(
            self.fpath, key="sha256"
        )
        assert hashlib_result == copy2hash_result

    def test_sha512(self):
        hashlib_result = hashlib.sha512(self.fpath.encode("utf-8")).hexdigest()
        copy2hash_result = copy2hash.HashTag(args={}).fpath2hash(
            self.fpath, key="sha512"
        )
        assert hashlib_result == copy2hash_result

    def test_blake2b(self):
        hashlib_result = hashlib.blake2b(self.fpath.encode("utf-8")).hexdigest()
        copy2hash_result = copy2hash.HashTag(args={}).fpath2hash(
            self.fpath, key="blake2b"
        )
        assert hashlib_result == copy2hash_result

    def test_blake2s(self):
        hashlib_result = hashlib.blake2s(self.fpath.encode("utf-8")).hexdigest()
        copy2hash_result = copy2hash.HashTag(args={}).fpath2hash(
            self.fpath, key="blake2s"
        )
        assert hashlib_result == copy2hash_result

    def test_md5(self):
        hashlib_result = hashlib.md5(self.fpath.encode("utf-8")).hexdigest()
        copy2hash_result = copy2hash.HashTag(args={}).fpath2hash(self.fpath, key="md5")
        assert hashlib_result == copy2hash_result

    def test_sha3_224(self):
        hashlib_result = hashlib.sha3_224(self.fpath.encode("utf-8")).hexdigest()
        copy2hash_result = copy2hash.HashTag(args={}).fpath2hash(
            self.fpath, key="sha3_224"
        )
        assert hashlib_result == copy2hash_result

    def test_sha3_256(self):
        hashlib_result = hashlib.sha3_256(self.fpath.encode("utf-8")).hexdigest()
        copy2hash_result = copy2hash.HashTag(args={}).fpath2hash(
            self.fpath, key="sha3_256"
        )
        assert hashlib_result == copy2hash_result

    def test_sha3_512(self):
        hashlib_result = hashlib.sha3_512(self.fpath.encode("utf-8")).hexdigest()
        copy2hash_result = copy2hash.HashTag(args={}).fpath2hash(
            self.fpath, key="sha3_512"
        )
        assert hashlib_result == copy2hash_result

    def test_shake_128(self):
        hashlib_result = hashlib.shake_128(self.fpath.encode("utf-8")).hexdigest(32)
        copy2hash_result = copy2hash.HashTag(args={}).fpath2hash(
            self.fpath, key="shake_128"
        )
        assert hashlib_result == copy2hash_result

    def test_shake_256(self):
        hashlib_result = hashlib.shake_256(self.fpath.encode("utf-8")).hexdigest(32)
        copy2hash_result = copy2hash.HashTag(args={}).fpath2hash(
            self.fpath, key="shake_256"
        )
        assert hashlib_result == copy2hash_result


class TestSHANames(object):
    fname = "test_example_1.txt"

    def test_normal_file(self):
        args = __refargs__

        hashlib_result = hashlib.sha256(self.fname.encode("utf-8")).hexdigest()
        copy2hash_result = copy2hash.HashTag(args=args).generate_hashname(
            fname=self.fname, suffix=".txt", sha_key="sha256"
        )
        assert copy2hash_result == f"{hashlib_result}.txt"

    def test_new_ending_file(self):
        args = __refargs__
        args["file_extension"] = True

        hashlib_result = hashlib.sha256(self.fname.encode("utf-8")).hexdigest()
        copy2hash_result = copy2hash.HashTag(args=args).generate_hashname(
            fname=self.fname, suffix=".txt", sha_key="sha256"
        )
        assert copy2hash_result == f"{hashlib_result}.sha256"

    def test_new_suffix_file(self):
        args = __refargs__
        args["file_suffix"] = True
        args["file_extension"] = False

        hashlib_result = hashlib.sha256(self.fname.encode("utf-8")).hexdigest()
        copy2hash_result = copy2hash.HashTag(args=args).generate_hashname(
            fname=self.fname, suffix=".txt", sha_key="sha256"
        )

        assert copy2hash_result == f"sha256-{hashlib_result}"

    def test_new_suffix_ending_file(self):
        args = __refargs__
        args["file_extension"] = True
        args["file_suffix"] = True

        hashlib_result = hashlib.sha256(self.fname.encode("utf-8")).hexdigest()
        copy2hash_result = copy2hash.HashTag(args=args).generate_hashname(
            fname=self.fname, suffix=".txt", sha_key="sha256"
        )
        assert copy2hash_result == f"sha256-{hashlib_result}.sha256"
