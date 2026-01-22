# app/core/github_analysis.py
# from typing import List

# async def summarize_commits(commits: List[dict]):
#     """
#     Summarize GitHub commits for a repo.
#     Input: list of commit JSON objects from GitHub API
#     Output: list of dicts with key info (author, date, message snippet, files changed)
#     """
#     highlights = []
#     for commit in commits:
#         commit_info = commit.get("commit", {})
#         author_info = commit_info.get("author", {})
#         highlights.append({
#             "author": author_info.get("name"),
#             "date": author_info.get("date"),
#             "message": commit_info.get("message", "")[:50],  # snippet
#             # 'files' key may not exist in GitHub API commit list endpoint; optional
#             "files_changed": len(commit.get("files", [])) if "files" in commit else None
#         })
#     return highlights

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