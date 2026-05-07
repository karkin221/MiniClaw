
from pathlib import Path


class RetrievalEngine:

    @staticmethod
    def retrieve(query):

        snippets = []

        for path in Path(".").glob("*.md"):

            try:
                text = path.read_text()[:1000]

                snippets.append(
                    f"FILE: {path.name}\n{text}"
                )

            except:
                pass

        return "\n\n".join(snippets[:3])
