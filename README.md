# Leadership Coach Wiki

A compounding leadership knowledge system: an Obsidian vault of structured markdown pages, maintained and queried via Python CLI scripts backed by the Claude API.

## Setup

```bash
# 1. Clone or copy this directory
cd leadership-wiki

# 2. Install Python dependencies
pip install -r requirements.txt

# 3. Install system dependency (PDF fallback only — optional)
sudo apt install poppler-utils   # Ubuntu/Debian
brew install poppler              # macOS

# 4. Configure API key
cp .env.template .env
# Edit .env and set ANTHROPIC_API_KEY=sk-ant-...

# 5. Open vault in Obsidian
# File → Open folder as vault → select leadership-wiki/
# Recommended community plugins: Dataview, Templater
```

## Usage

### Step 1: Convert PDFs (if needed)

```bash
python scripts/convert.py raw/articles/
# Output: raw/articles/markdown/*.md
```

### Step 2: Ingest a source

```bash
python scripts/ingest.py raw/articles/hbr-article.md
python scripts/ingest.py raw/articles/report.pdf        # auto-converts PDF
python scripts/ingest.py raw/meeting-notes/             # ingest folder
```

### Step 3: Ask a coaching question

```bash
python scripts/coach.py "My engineer is smart but keeps undermining the project in meetings"
python scripts/coach.py "How do I delegate without losing quality control?"
python scripts/coach.py "I get frustrated when people haven't done the thinking"
```

### Step 4: Health-check the wiki periodically

```bash
python scripts/lint.py
python scripts/lint.py --report-only
```

## Interactive Mode (Claude Code)

Open `leadership-wiki/` in Claude Code. The `CLAUDE.md` file instructs Claude Code to act as a leadership coach directly — ask coaching questions, request ingestion, or ask for a lint pass in the chat.

## Directory Structure

```
leadership-wiki/
├── raw/          # Drop sources here — immutable, LLM reads only
├── wiki/         # LLM-maintained knowledge pages (also your Obsidian vault)
│   ├── index.md  # Master content map
│   ├── log.md    # Chronological change record
│   ├── principles/, management/, communication/, organization/, coaching/
│   ├── cases/    # Real situations filed from coaching sessions
│   └── sources/  # Source summary pages
├── schemas/      # Agent operating instructions and page templates
├── scripts/      # convert.py, ingest.py, coach.py, lint.py, utils.py
└── tests/        # pytest test suite
```

## Running Tests

```bash
pytest tests/ -v
```

## Optional: Use a cheaper model for quick queries

```bash
python scripts/coach.py "question" --model claude-haiku-4-5-20251001
python scripts/ingest.py raw/articles/article.md --model claude-sonnet-4-6
```
