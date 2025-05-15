

# README.md Sample: Setup Instructions

---

## Project Setup Instructions

Welcome to the **solar-challenge-week1** project! Follow the steps below to set up your development environment:

### 1. Clone the repository

```bash
git clone https://github.com/your-username/solar-challenge-week1.git
cd solar-challenge-week1
```

### 2. Create and activate a Python virtual environment

For **venv**:

```bash
python3 -m venv .venv
source .venv/bin/activate      # On Windows: .venv\Scripts\activate
```

For **conda**:

```bash
conda create --name solar-env python=3.12
conda activate solar-env
```

### 3. Install dependencies

Make sure you have the `requirements.txt` file, then run:

```bash
pip install -r requirements.txt
```

### 4. Verify Python version

```bash
python --version
```

Make sure it shows Python 3.12.x.

### 5. Run tests (if applicable)

```bash
pytest
```

---

## Project Structure

* `.github/workflows/` — Contains GitHub Actions workflow files for CI/CD
* `src/` — Main source code
* `notebooks/` — Jupyter notebooks for exploration and analysis
* `tests/` — Unit and integration tests
* `scripts/` — Utility scripts and helpers

---

## Notes

* Remember to activate your virtual environment each time before working on the project.
* This setup ensures consistent development environments across the team.
* CI workflow runs on every push and PR to `main` and `setup-task` branches.

---

