"""Lightweight lexical retrieval across existing blog posts."""

from dataclasses import dataclass
from pathlib import Path
import tomllib

from app.const import WORKSPACE


@dataclass(frozen=True)
class RetrievedPost:
    slug: str
    title: str
    summary: str
    excerpt: str
    score: int


def _tokenize(text: str) -> set[str]:
    return {
        word
        for word in ''.join(ch.lower() if ch.isalnum() else ' ' for ch in text).split()
        if len(word) > 2
    }


def _read_post(path: Path) -> tuple[dict, str]:
    front_matter_raw = []
    content = []
    is_front_matter = False

    with path.open("r") as file:
        for line in file:
            if line.startswith("+++"):
                is_front_matter = not is_front_matter
                continue

            if is_front_matter:
                front_matter_raw.append(line)
            else:
                content.append(line)

    front_matter = tomllib.loads(''.join(front_matter_raw)) if front_matter_raw else {}
    return front_matter, ''.join(content).strip()


def _best_excerpt(content: str, query_tokens: set[str]) -> str:
    paragraphs = [paragraph.strip() for paragraph in content.split("\n\n") if paragraph.strip()]
    if not paragraphs:
        return ""

    best_paragraph = paragraphs[0]
    best_score = -1
    for paragraph in paragraphs:
        score = len(query_tokens & _tokenize(paragraph))
        if score > best_score:
            best_paragraph = paragraph
            best_score = score

    return best_paragraph[:500]


def search_related_posts(query: str, current_post_slug: str = None, limit: int = 3) -> list[RetrievedPost]:
    query_tokens = _tokenize(query)
    if not query_tokens:
        return []

    posts_dir = Path(WORKSPACE) / "content" / "posts"
    results = []
    for path in sorted(posts_dir.glob("*.md")):
        slug = path.stem
        if slug == "_index" or slug == current_post_slug:
            continue

        front_matter, content = _read_post(path)
        title = str(front_matter.get("title", slug.replace("-", " ").title()))
        summary = str(front_matter.get("summary", ""))

        title_score = len(query_tokens & _tokenize(title)) * 5
        summary_score = len(query_tokens & _tokenize(summary)) * 3
        content_score = len(query_tokens & _tokenize(content))
        score = title_score + summary_score + content_score
        if score <= 0:
            continue

        results.append(RetrievedPost(
            slug=slug,
            title=title,
            summary=summary,
            excerpt=_best_excerpt(content, query_tokens),
            score=score,
        ))

    results.sort(key=lambda post: (-post.score, post.slug))
    return results[:limit]


def format_related_posts_context(query: str, current_post_slug: str = None, limit: int = 3) -> str:
    matches = search_related_posts(query, current_post_slug=current_post_slug, limit=limit)
    if not matches:
        return ""

    lines = []
    for match in matches:
        lines.append(f"- {match.title} ({match.slug})")
        if match.summary:
            lines.append(f"  Summary: {match.summary}")
        if match.excerpt:
            lines.append(f"  Excerpt: {match.excerpt}")

    return "\n".join(lines)
