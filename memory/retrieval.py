
from pathlib import Path

class RetrievalEngine:

    @staticmethod
    def retrieve(query):

        chunks = []

        for path in Path(".").rglob("*.py"):

            try:

                text = path.read_text()[:500]

                chunks.append(
                    f"FILE: {path}\n{text}"
                )

            except:
                pass

        return "\n\n".join(chunks[:5])
