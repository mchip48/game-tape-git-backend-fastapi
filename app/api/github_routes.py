# # app/api/github_routes.py
# from fastapi import APIRouter, HTTPException
# from app.core.github_services import get_user, get_repos, get_commits
# from app.core.github_analysis import summarize_commits
# import os
# import httpx

# router = APIRouter(prefix="/github", tags=["GitHub"])

# @router.get("/user")
# async def github_user():
#     try:
#         return await get_user()
#     except Exception as e:
#         raise HTTPException(status_code=500, detail=str(e))

# @router.get("/repos")
# async def github_repos():
#     try:
#         return await get_repos()
#     except Exception as e:
#         raise HTTPException(status_code=500, detail=str(e))

# @router.get("/commits/{repo_name}")
# async def github_commits(repo_name: str, per_page: int = 10):
#     """Fetch recent commits for a given repo"""
#     username = os.getenv("GITHUB_USERNAME")  # store your GitHub username in .env

#     try:
#         commits = await get_commits(username=username, repo_name=repo_name, per_page=per_page)
#         return {"repo": repo_name, "commits": commits}
#     except Exception as e:
#         raise HTTPException(status_code=500, detail=str(e))
    
    
# @router.get("/my-repos")
# async def my_repos():
#     """
#     Returns list of your GitHub repos to copy exact names
#     """
#     try:
#         repos = await get_repos()
#         # Return owner/repo format
#         return [f"{r['owner']['login']}/{r['name']}" for r in repos]
#     except Exception as e:
#         raise HTTPException(status_code=500, detail=str(e))


# # @router.get("/highlights/{repo_name}")
# # async def github_highlights(repo_name: str):
# #     """
# #     Return summarized highlights for a repo's commits
# #     """
# #     try:
# #         commits = await get_commits(repo_name)
# #         highlights = await summarize_commits(commits)
# #         return {"repo": repo_name, "highlights": highlights}
# #     except Exception as e:
# #         raise HTTPException(status_code=500, detail=str(e))

# @router.get("/highlights/{repo_name}")
# async def github_highlights(repo_name: str):
#     # Ensure correct format
#     if "/" not in repo_name:
#         raise HTTPException(
#             status_code=400,
#             detail="Repo name must be in 'owner/repo' format. Use /github/my-repos to see the correct format."
#         )
#     try:
#         commits = await get_commits(repo_name)
#         # Placeholder for real highlights logic
#         highlights = [{"sha": c["sha"], "message": c["commit"]["message"]} for c in commits]
#         return highlights
#     except httpx.HTTPStatusError as e:
#         if e.response.status_code == 404:
#             raise HTTPException(
#                 status_code=404,
#                 detail=f"Repo '{repo_name}' not found. Check spelling and format."
#             )
#         elif e.response.status_code == 401:
#             raise HTTPException(
#                 status_code=401,
#                 detail="Unauthorized: GitHub token may be invalid or missing required permissions."
#             )
#         else:
#             raise HTTPException(status_code=500, detail=str(e))

# app/api/github_routes.py
# from fastapi import APIRouter, HTTPException
# from app.core.github_services import get_user, get_repos, get_commits
# import os
# from typing import List, Dict
# import httpx

# router = APIRouter(prefix="/github", tags=["GitHub"])

# @router.get("/user")
# async def github_user() -> Dict:
#     try:
#         return await get_user()
#     except Exception as e:
#         raise HTTPException(status_code=500, detail=str(e))

# @router.get("/my-repos")
# async def github_my_repos() -> List[str]:
#     """
#     Return list of your GitHub repos in owner/repo format
#     """
#     try:
#         repos = await get_repos()
#         return [f"{r['owner']['login']}/{r['name']}" for r in repos]
#     except Exception as e:
#         raise HTTPException(status_code=500, detail=str(e))

# @router.get("/commits/{repo_full_name}")
# async def github_commits(repo_full_name: str, per_page: int = 10) -> Dict:
#     """
#     Fetch recent commits for a repo.
#     repo_full_name: "owner/repo_name" exactly as returned by /my-repos
#     """
#     try:
#         commits = await get_commits(repo_full_name=repo_full_name, per_page=per_page)
#         # Return commits nicely for Swagger
#         return {
#             "repo": repo_full_name,
#             "commits": [
#                 {
#                     "sha": c["sha"],
#                     "message": c["commit"]["message"],
#                     "author": c["commit"]["author"]["name"],
#                     "date": c["commit"]["author"]["date"],
#                     "url": c["html_url"]
#                 }
#                 for c in commits
#             ]
#         }
#     except httpx.HTTPStatusError as e:
#         if e.response.status_code == 404:
#             raise HTTPException(status_code=404, detail="Repository not found")
#         elif e.response.status_code == 401:
#             raise HTTPException(status_code=401, detail="Unauthorized: check GitHub token")
#         else:
#             raise HTTPException(status_code=500, detail=str(e))
#     except Exception as e:
#         raise HTTPException(status_code=500, detail=str(e))

# @router.get("/commits/{repo_name}")
# async def github_commits(repo_name: str, per_page: int = 10):
#     """
#     Fetch recent commits for a given repo (just use the repo name)
#     """
#     try:
#         commits = await get_commits(repo_name=repo_name, per_page=per_page)
#         return {"repo": repo_name, "commits": commits}
#     except httpx.HTTPStatusError as e:
#         # Provide more helpful debug info
#         raise HTTPException(
#             status_code=e.response.status_code,
#             detail=f"GitHub API error: {e.response.json()}"
#         )
#     except Exception as e:
#         raise HTTPException(status_code=500, detail=str(e))

# app/api/github_routes.py
from fastapi import APIRouter, HTTPException
from app.core.github_services import get_user, get_repos, get_commits
import os

router = APIRouter(prefix="/github", tags=["GitHub"])

@router.get("/user")
async def github_user():
    try:
        return await get_user()
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.get("/my-repos")
async def my_repos():
    try:
        repos = await get_repos()
        # Return only repo names (to pass to commits route)
        return [r["name"] for r in repos]
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

# @router.get("/commits/{repo_name}")
# async def github_commits(repo_name: str, per_page: int = 10):
#     try:
#         commits_summary = await get_commits(repo_name=repo_name, per_page=per_page)
#         return {"repo": repo_name, "summary": commits_summary}
#     except httpx.HTTPStatusError as e:
#         raise HTTPException(
#             status_code=e.response.status_code,
#             detail=f"GitHub API error: {e.response.json()}"
#         )
#     except Exception as e:
#         raise HTTPException(status_code=500, detail=str(e))

@router.get("/commits/{repo_name}")
async def github_commits(repo_name: str, per_page: int = 10):
    try:
        return await get_commits(repo_name=repo_name, per_page=per_page)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))