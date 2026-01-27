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
---------------
Backend:
---------------
Python
FastAPI
Github REST API
API-Key Authentication
Rate Limiting (SlowAPI)
CORS Middleware
Async Service Architecture
---------------
Frontend:
---------------
React (Vite)
TypeScript
<!-- TanStack React Query -->
Tailwind CSS
<!-- ShadCN UI -->
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

Backend Setup:
---------------
1) Copy and paste this in your terminal:

git clone https://github.com/mchip48/game-tape-git-backend-fastapi
cd game-tape-git-backend-fastapi
python -m venv .venv
source .venv/bin/activate
uv pip install -r requirements.txt

2) Create a .env file: 

GITHUB_TOKEN=your_github_token
API_KEY=your_own_demo_api_key
ENV=dev

3) Run the server:

uvicorn main:app --reload
---------------

Backend runs at:
http://127.0.0.1:8000

...............

Frontend Setup:
---------------

1) Copy and paste this in your terminal:

git clone https://github.com/YOUR_USERNAME/game-tape-frontend
cd game-tape-frontend
npm install

2) Create a .env.local file and copy and paste this into there: 

VITE_API_BASE_URL=http://127.0.0.1:8000

3) Run frontend:

npm run dev
---------------

Frontend runs at:
http://localhost:8080

...............

Demo Instructions:

- Open the frontend

- Paste a provided API key into the API key input field

- Select a repository or enter a repo name

- View live analysis and scoring
---------------
Project Architecture:

backend/
├── app/
│   ├── api/
│   ├── core/
│   ├── services/
│   ├── security/
│   └── analysis/
│
frontend/
├── src/
│   ├── components/
│   ├── lib/
│   ├── pages/
│   └── api/

Each layer is intentionally separated to support:

- AI/ML pipelines

- OAuth

- User accounts

- Background jobs

- Scalable data storage

---------------

Future Roadmap:

- AI-powered commit summarization

- GitHub OAuth login

- Multi-user accounts

- Historical repo tracking

- Commit embeddings & clustering

- Exportable reports (PDF / JSON)

---------------

📝 License

MIT License

---------------

Built by Matthew Chipkin 

---------------
