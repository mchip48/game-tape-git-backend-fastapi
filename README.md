Game Tape Gitty — GitHub Repository Analysis Platform

Game Tape is a full-stack web application that analyzes GitHub repositories and generates meaningful insights about development activity, commit quality, and project consistency.

It is designed as a secure, extensible platform that can later support AI/ML analysis, OAuth, and multi-user accounts, while remaining simple enough to demo and use immediately.

Core Features:

- Analyze GitHub repositories by name

- Repo-level scoring (activity, quality, consistency, collaboration)

- Commit insight generation

- API key–based authentication

- Rate limiting for abuse prevention

- CORS-safe frontend/backend integration

- Health & security test endpoints

- Modern React frontend (Vite + React Query)

- Clean FastAPI service architecture

Tech Stack -
----------
Backend:
----------
Python
FastAPI
Github REST API
API-Key Authentication
Rate Limiting (SlowAPI)
CORS Middleware
Async Service Architecture
----------
Frontend:
----------
React (Vite)
TypeScript
TanStack React Query
Tailwind CSS
ShadCN UI
LocalStorage API key handling


Security Overview:

Game Tape was built with security as a priority:

- API keys required for all GitHub endpoints

- Rate limiting enforced globally

- No secrets exposed to frontend

- API keys stored only in browser localStorage

- CORS restricted via environment configuration

- Safe for public demo use


Getting Started (Locally):

1) Backend Setup:

