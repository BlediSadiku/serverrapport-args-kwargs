import contextlib
import importlib.util
import io
from pathlib import Path
import subprocess
import sys
import unittest


SCRIPT = Path(__file__).with_name("03_serverrapport_args_kwargs.py")
EXPECTED = (
    "Server: web-01\nStatussen:\n- online\n- back-up voltooid\n"
    "- updates beschikbaar\nDetails:\nlocatie: Brussel\nbeheerder: Demo\n"
)


def load_module():
    spec = importlib.util.spec_from_file_location("serverrapport", SCRIPT)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


class ServerrapportTests(unittest.TestCase):
    def test_import_has_no_output(self):
        output = io.StringIO()
        with contextlib.redirect_stdout(output):
            load_module()
        self.assertEqual(output.getvalue(), "")

    def test_example_output(self):
        module = load_module()
        output = io.StringIO()
        with contextlib.redirect_stdout(output):
            module.maak_serverrapport(module.servernaam, *module.statussen, **module.details)
        self.assertEqual(output.getvalue(), EXPECTED)

    def test_no_optional_arguments(self):
        output = io.StringIO()
        with contextlib.redirect_stdout(output):
            load_module().maak_serverrapport("test-01")
        self.assertEqual(output.getvalue(), "Server: test-01\nStatussen:\nDetails:\n")

    def test_custom_arguments(self):
        output = io.StringIO()
        with contextlib.redirect_stdout(output):
            load_module().maak_serverrapport("test-02", "offline", poort=8080)
        self.assertEqual(output.getvalue(),
                         "Server: test-02\nStatussen:\n- offline\nDetails:\npoort: 8080\n")

    def test_script_output(self):
        result = subprocess.run([sys.executable, "-B", str(SCRIPT)],
                                check=True, capture_output=True, text=True)
        self.assertEqual(result.stdout, EXPECTED)
        self.assertEqual(result.stderr, "")


if __name__ == "__main__":
    unittest.main(verbosity=2)
