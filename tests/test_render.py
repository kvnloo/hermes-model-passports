import importlib.util
import json
import pathlib
import unittest

ROOT = pathlib.Path(__file__).parents[1]
spec = importlib.util.spec_from_file_location("render", ROOT / "src/render.py")
module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)

class RenderTests(unittest.TestCase):
    def setUp(self):
        self.rows = json.loads((ROOT / "catalog/examples.json").read_text())

    def test_examples_separate_model_and_route_identity(self):
        for row in self.rows:
            self.assertIn("canonical_id", row["identity"])
            self.assertIn("provider", row["route"])

    def test_svg_is_accessible_and_escapes_content(self):
        row = json.loads(json.dumps(self.rows[0]))
        row["identity"]["display_name"] = "A&B <Model>"
        svg = module.render(row)
        self.assertIn('role="img"', svg)
        self.assertIn("A&amp;B &lt;Model&gt;", svg)

    def test_route_is_secondary_tab(self):
        self.assertIn("VIA OPENROUTER", module.render(self.rows[1]))

    def test_unknown_capabilities_are_not_false(self):
        row = json.loads(json.dumps(self.rows[0]))
        row["capabilities"] = {"vision": None}
        self.assertIn("CAPABILITIES UNKNOWN", module.render(row))

if __name__ == "__main__":
    unittest.main()
