import re
import unittest
from pathlib import Path
from urllib.parse import unquote, urlsplit


ROOT = Path(__file__).resolve().parents[1]
MARKDOWN_LINK = re.compile(r"(?<!!)\[[^\]]+\]\(([^)]+)\)")


class DocumentationTests(unittest.TestCase):
    def test_local_markdown_links_resolve(self) -> None:
        markdown_files = sorted(ROOT.rglob("*.md"))
        broken_links = []

        for source in markdown_files:
            if ".git" in source.parts:
                continue
            content = source.read_text(encoding="utf-8")
            for raw_target in MARKDOWN_LINK.findall(content):
                target = urlsplit(raw_target)
                if target.scheme or target.netloc or not target.path:
                    continue
                resolved = (source.parent / unquote(target.path)).resolve()
                if not resolved.exists():
                    broken_links.append(
                        f"{source.relative_to(ROOT).as_posix()}: {raw_target}"
                    )

        self.assertEqual(broken_links, [])
