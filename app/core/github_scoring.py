# app/core/github_scoring.py

from datetime import datetime

def clamp(value: float, min_value=0, max_value=100) -> int:
    return max(min_value, min(int(value), max_value))


def score_repo(analysis: dict) -> dict:
    activity = analysis["activity"]
    time = analysis["time"]
    quality = analysis["commit_quality"]

    total_commits = activity["total_commits"]
    commits_per_day = time["commits_per_day"]
    active_days = time["active_days"]
    solo_project = activity["solo_project"]

    descriptive_ratio = quality["descriptive_commit_ratio"]
    avg_msg_length = quality["avg_message_length"]

    # --- Scores ---
    activity_score = clamp(commits_per_day * 10)
    consistency_score = clamp((active_days / max(active_days, 7)) * 100)
    quality_score = clamp((descriptive_ratio * 70) + (avg_msg_length / 100 * 30))
    collaboration_score = 100 if solo_project else 70

    overall_score = clamp(
        (activity_score * 0.3) +
        (consistency_score * 0.25) +
        (quality_score * 0.3) +
        (collaboration_score * 0.15)
    )

    # --- Signals ---
    signals = []

    if commits_per_day > 3:
        signals.append("High sustained development activity")
    if solo_project:
        signals.append("Solo-developed repository")
    if descriptive_ratio > 0.8:
        signals.append("Consistently descriptive commit messages")
    if active_days >= 5:
        signals.append("Work spread across multiple days")

    return {
        "overall": overall_score,
        "activity": activity_score,
        "consistency": consistency_score,
        "commit_quality": quality_score,
        "collaboration": collaboration_score,
        "signals": signals
    }
