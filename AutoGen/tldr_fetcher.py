"""
Fetch and parse TLDR AI newsletter for research articles.
"""
import re
from dataclasses import dataclass
from typing import List

import requests
from bs4 import BeautifulSoup

TLDR_AI_URL = "https://tldr.tech/api/latest/ai"

# Section headers that typically contain research / GenAI articles
RESEARCH_SECTION_HEADERS = (
    "Engineering & Research",
    "Deep Dives & Analysis",
    "Deep Dives",
    "Research",
)


@dataclass
class TLDRArticle:
    """A single article from TLDR AI."""
    title: str
    url: str
    summary: str
    section: str
    read_time: str = ""


def fetch_tldr_ai_html() -> str:
    """Fetch raw HTML from TLDR AI latest newsletter."""
    resp = requests.get(TLDR_AI_URL, timeout=15)
    resp.raise_for_status()
    return resp.text


def _parse_read_time(text: str) -> str:
    """Extract read time like '(18 minute read)' from text."""
    m = re.search(r"\((\d+\s*minute\s*read)\)", text, re.IGNORECASE)
    return m.group(0) if m else ""


def _is_research_section(section: str) -> bool:
    """True if this section typically contains research/GenAI articles."""
    s = section.lower()
    return (
        "research" in s
        or "deep dive" in s
        or "engineering" in s
        or "analysis" in s
    )


def _is_likely_research(url: str, title: str) -> bool:
    """Heuristic: arxiv, GitHub repos, or GenAI keywords."""
    u, t = url.lower(), title.lower()
    if "arxiv.org" in u:
        return True
    if "github.com" in u and any(k in t for k in ("agent", "llm", "model", "ai")):
        return True
    keywords = ("llm", "model", "agent", "reinforcement", "rlms", "benchmark")
    return any(k in t for k in keywords)


def parse_tldr_ai_research(html: str) -> List[TLDRArticle]:
    """
    Parse TLDR AI HTML and return research-oriented articles from
    'Engineering & Research' and 'Deep Dives & Analysis' sections,
    plus any arxiv/GenAI-looking links.
    """
    soup = BeautifulSoup(html, "html.parser")
    articles: List[TLDRArticle] = []
    seen_urls: set[str] = set()
    current_section = ""

    for elem in soup.find_all(["h1", "h2", "h3", "h4", "a", "p"]):
        if elem.name in ("h1", "h2", "h3", "h4"):
            current_section = elem.get_text(strip=True)
            continue

        if elem.name == "a" and elem.get("href"):
            href = (elem.get("href") or "").strip()
            if not href or href.startswith("#") or "tldr.tech" in href:
                continue
            href = href.split("?")[0]
            if href in seen_urls:
                continue
            title = elem.get_text(strip=True)
            if not title or len(title) < 8:
                continue
            # Skip sponsor/ad links
            if "sponsor" in title.lower() or "subscribe" in title.lower():
                continue
            in_research_section = _is_research_section(current_section)
            if not in_research_section and not _is_likely_research(href, title):
                continue
            seen_urls.add(href)
            summary = ""
            read_time = ""
            for n in (elem.find_next_sibling(), elem.parent):
                if n and getattr(n, "name", None) == "p":
                    raw = n.get_text(strip=True)
                    summary = raw[:500] if raw else ""
                    read_time = _parse_read_time(raw)
                    break
            if not summary and elem.parent:
                summary = elem.parent.get_text(strip=True).replace(title, "").strip()[:500]
                read_time = _parse_read_time(summary)
            articles.append(
                TLDRArticle(
                    title=title,
                    url=href,
                    summary=summary or "(No summary)",
                    section=current_section or "General",
                    read_time=read_time,
                )
            )

    return articles


def get_latest_tldr_ai_research() -> str:
    """
    Fetch TLDR AI and return a formatted string of the latest research/GenAI articles.
    Used as the AutoGen tool implementation.
    """
    try:
        html = fetch_tldr_ai_html()
        articles = parse_tldr_ai_research(html)
    except Exception as e:
        return f"Error fetching TLDR AI: {e}"

    if not articles:
        return "No research articles found in the latest TLDR AI edition."

    lines = [
        "Latest TLDR AI – Research & GenAI-related articles:",
        "",
    ]
    for i, a in enumerate(articles[:15], 1):
        lines.append(f"{i}. **{a.title}**")
        lines.append(f"   Section: {a.section}")
        if a.read_time:
            lines.append(f"   {a.read_time}")
        lines.append(f"   URL: {a.url}")
        lines.append(f"   Summary: {a.summary}")
        lines.append("")

    return "\n".join(lines).strip()
