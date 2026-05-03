# Webgame Data Tracker

A personal Python backend/data project for parsing, validating, storing and later presenting alliance data from the online strategy game Webgame.

The project is currently focused on processing HTML exports from the game, validating their structure and consistency, and storing valid data in a database. In the future, the stored historical data should be used for user-friendly presentation, comparison of snapshots and basic statistics.

---

## Why I built this project

I wanted to practice backend-oriented Python development on a realistic data problem.

The input data comes from HTML files, which means it cannot be trusted automatically. The application has to parse the data, validate the structure, check consistency between files and store only data that makes sense.

This helps me practice:

- HTML parsing,
- data validation,
- database modeling,
- pipeline-style processing,
- error handling,
- separating parser, validation and database logic,
- preparing data for later analysis and presentation.

---

## Current focus

The current backend flow is:

1. Upload or load HTML files from Webgame.
2. Parse alliance overview data.
3. Parse country snapshot/detail data.
4. Validate expected structure and required fields.
5. Check consistency between related files.
6. Detect the current game age/round.
7. Compute a snapshot hash.
8. Store valid normalized data in the database.

---

## Planned direction

The next goal is to use stored historical data for:

- clearer presentation of alliance and country data,
- tracking changes over time,
- comparing snapshots,
- deriving useful statistics,
- improving the user interface.

---

## Tech stack

- Python
- Flask
- SQLAlchemy
- BeautifulSoup
- HTML parsing
- Relational database
- Git / GitHub

---

## What this project demonstrates

This project demonstrates my current focus on Python backend and data-oriented development:

- working with semi-structured input data,
- validating data before saving,
- thinking about consistency and error states,
- designing a pipeline-style processing flow,
- using SQLAlchemy models,
- preparing data for future analysis.

The project is work in progress and is used as a practical learning project.
