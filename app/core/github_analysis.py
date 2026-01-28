# app/core/github_analysis.py

from collections import Counter
from datetime import datetime
from statistics import mean


async def summarize_commits(commits: list[dict]) -> dict:
    if not commits:
        return {
            "total_commits": 0,
            "activity": {},
            "time": {},
            "commit_quality": {},
            "insights": ["No commits available for analysis"]
        }

    # -----------------------------
    # 1. BASIC EXTRACTION
    # -----------------------------
    authors = []
    commit_dates = []
    messages = []

    for c in commits:
        commit_data = c.get("commit", {})
        author_data = commit_data.get("author", {})

        author = author_data.get("name", "Unknown")
        date_str = author_data.get("date")
        message = commit_data.get("message", "")

        authors.append(author)
        messages.append(message)

        if date_str:
            commit_dates.append(
                datetime.fromisoformat(date_str.replace("Z", "+00:00"))
            )

    total_commits = len(commits)

    # -----------------------------
    # 2. ACTIVITY METRICS
    # -----------------------------
    author_counts = Counter(authors)
    primary_contributor = author_counts.most_common(1)[0][0]
    solo_project = len(author_counts) == 1

    activity = {
        "total_commits": total_commits,
        "commits_per_author": dict(author_counts),
        "primary_contributor": primary_contributor,
        "solo_project": solo_project
    }

    # -----------------------------
    # 3. TIME-BASED METRICS
    # -----------------------------
    commit_dates.sort()

    first_commit = commit_dates[0]
    latest_commit = commit_dates[-1]

    active_days = len({d.date() for d in commit_dates})
    commits_per_day = round(total_commits / active_days, 2) if active_days else 0

    if commits_per_day < 2:
        pace = "sporadic"
    elif commits_per_day <= 5:
        pace = "steady"
    else:
        pace = "intense"

    time_metrics = {
        "first_commit": first_commit.date().isoformat(),
        "latest_commit": latest_commit.date().isoformat(),
        "active_days": active_days,
        "commits_per_day": commits_per_day,
        "development_pace": pace
    }

    # -----------------------------
    # 4. COMMIT QUALITY METRICS
    # -----------------------------
    message_lengths = [len(m) for m in messages if m.strip()]
    avg_length = round(mean(message_lengths), 2) if message_lengths else 0

    vague_keywords = {"update", "stuff", "changes", "fix", "work"}
    vague_commits = sum(
        1 for m in messages if m.lower().strip() in vague_keywords
    )

    descriptive_ratio = round(
        (total_commits - vague_commits) / total_commits, 2
    ) if total_commits else 0

    if descriptive_ratio > 0.8:
        quality_score = "high"
    elif descriptive_ratio > 0.5:
        quality_score = "medium"
    else:
        quality_score = "low"

    commit_quality = {
        "avg_message_length": avg_length,
        "vague_commits": vague_commits,
        "descriptive_commit_ratio": descriptive_ratio,
        "quality_score": quality_score
    }

    # -----------------------------
    # 5. DERIVED INSIGHTS
    # -----------------------------
    insights = []

    if solo_project:
        insights.append("This appears to be a solo-developed project")

    insights.append(f"Development activity is {pace} over time")

    if quality_score == "high":
        insights.append("Commit messages are descriptive and well-structured")
    elif quality_score == "low":
        insights.append("Commit messages are often vague and may lack clarity")

    if active_days >= 5:
        insights.append("The repository shows consistent development activity")

    return {
        "total_commits": total_commits,
        "activity": activity,
        "time": time_metrics,
        "commit_quality": commit_quality,
        "insights": insights
    }
