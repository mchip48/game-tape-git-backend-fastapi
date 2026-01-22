# app/core/github_analysis.py

async def summarize_commits(commits: list[dict]) -> dict:
    """
    Summarize recent commits for display / analysis
    """
    if not commits:
        return {"summary": "No commits found"}

    return {
        "total_commits": len(commits),
        "latest_commit": commits[0]["commit"]["message"],
        "authors": list(
            {c["commit"]["author"]["name"] for c in commits if c.get("commit")}
        ),
    }