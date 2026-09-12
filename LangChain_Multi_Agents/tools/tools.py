import os
from dotenv import load_dotenv
load_dotenv()
TAVILY_API_KEY = os.getenv('TAVILY_API_KEY')
os.environ["TAVILY_API_KEY"] = TAVILY_API_KEY
from langchain_tavily import TavilySearch
from langchain.tools import tool
from bs4 import BeautifulSoup
from readability import Document
import trafilatura
import re
import requests
import json


tools = TavilySearch(max_results=2)
MAX_SCRAPE_CHARS = 1200
MAX_SEARCH_CHARS = 600

@tool
def web_search(query: str) -> str:
    """Search web using Tavily."""
    results = tools.invoke({"query": query})
    
    # ✅ DEBUG: Check type
    print(f"DEBUG - Type: {type(results)}")
    
    # ✅ Handle string (JSON) response
    if isinstance(results, str):
        try:
            results = json.loads(results)
        except json.JSONDecodeError:
            # Plain string, return as is
            return results[:MAX_SEARCH_CHARS]
    
    # ✅ Now handle dict
    if isinstance(results, dict) and 'results' in results:
        out = []
        for item in results['results']:
            out.append(
                f"URL: {item.get('url', 'N/A')}\n"
                f"Title: {item.get('title', 'N/A')}\n"
                f"Content: {item.get('content', '')[:150]}..."
            )
        text = "\n\n---\n\n".join(out)
        return text[:MAX_SEARCH_CHARS]
    
    # Fallback
    return str(results)[:MAX_SEARCH_CHARS]


@tool
def scrape_webpage(url: str) -> str:
    """Scrape a webpage and return clean text content.
    
    Args:
        url: The webpage URL to scrape
        
    Returns:
        Clean text content as a string (max 1200 chars)
    """
    headers = {
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) "
                      "AppleWebKit/537.36 (KHTML, like Gecko) "
                      "Chrome/120.0.0.0 Safari/537.36"
    }
    
    # Fetch page
    try:
        response = requests.get(url, headers=headers, timeout=15)
        response.raise_for_status()
        html = response.text
    except Exception as e:
        return f"❌ Failed to fetch {url}: {e}"
    
    content = ""
    method = ""
    
    # ============================================================
    # STRATEGY 1: trafilatura (Best for articles)
    # ============================================================
    try:
        extracted = trafilatura.extract(
            html,
            include_comments=False,
            include_tables=True,
            include_links=True,
            favor_precision=True,
            url=url
        )
        if extracted and len(extracted.strip()) > 100:
            content = clean_text(extracted, max_chars=MAX_SCRAPE_CHARS)
            method = "trafilatura"
    except Exception:
        pass
    
    # ============================================================
    # STRATEGY 2: readability-lxml
    # ============================================================
    if not content:
        try:
            doc = Document(html)
            summary_html = doc.summary()
            soup = BeautifulSoup(summary_html, "lxml")
            
            for tag in soup(["script", "style", "noscript", "template"]):
                tag.decompose()
            
            text = soup.get_text(separator="\n", strip=True)
            if text and len(text.strip()) > 100:
                content = clean_text(text, max_chars=MAX_SCRAPE_CHARS)
                method = "readability"
        except Exception:
            pass
    
    # ============================================================
    # STRATEGY 3: BeautifulSoup (Fallback)
    # ============================================================
    if not content:
        try:
            soup = BeautifulSoup(html, "lxml")
            
            for tag in soup(["script", "style", "noscript", "template",
                             "header", "footer", "nav", "aside"]):
                tag.decompose()
            
            text = soup.get_text(separator="\n", strip=True)
            if text and len(text.strip()) > 50:
                content = clean_text(text, max_chars=MAX_SCRAPE_CHARS)
                method = "beautifulsoup"
        except Exception as e:
            return f"❌ All extraction methods failed: {e}"
    
    # ✅ Return as STRING
    if content:
        return f"📄 URL: {url}\n🔧 Method: {method}\n\n{content}"
    else:
        return f"❌ Could not extract content from {url}"


def clean_text(text: str, max_chars: int = MAX_SCRAPE_CHARS) -> str:
    """Clean and truncate text.
    
    Args:
        text: Raw text to clean
        max_chars: Maximum characters to keep (default: MAX_SCRAPE_CHARS)
        
    Returns:
        Cleaned and truncated text
    """
    # Collapse extra whitespace
    text = re.sub(r"\s\s+", " ", text)
    
    # Remove empty lines
    lines = [line.strip() for line in text.split("\n") if line.strip()]
    text = "\n".join(lines)
    
    # Remove noise patterns
    text = re.sub(r"\[edit\]", "", text)
    text = re.sub(r"\[\d+\]", "", text)   # [1], [2] citations
    text = re.sub(r"Advertisement", "", text, flags=re.IGNORECASE)
    
    # ✅ Hard truncate
    if len(text) > max_chars:
        text = text[:max_chars] + "...[truncated]"
    
    return text.strip()