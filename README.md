# CS50P — Introduction to Programming with Python

My solutions to all problem sets from [CS50's Introduction to Programming with Python](https://cs50.harvard.edu/python/).

---

## 📚 Course Structure

| Week | Topic | Files |
|------|-------|-------|
| Week 0 | Functions, Variables | `indoor`, `playback`, `faces`, `einstein`, `tip` |
| Week 1 | Conditionals | `deep`, `bank`, `meal`, `extensions`, `interpreter` |
| Week 2 | Loops | `camel`, `coke`, `twttr`, `nutrition`, `plates` |
| Week 3 | Exceptions | `fuel`, `grocery`, `outdated`, `taqueria` |
| Week 4 | Libraries | `emojize`, `figlet`, `adieu`, `game`, `professor` |
| Week 5 | Unit Tests | `test_twttr`, `test_bank`, `test_fuel`, `test_plates` |
| Week 6 | File I/O | `lines`, `pizza`, `scourgify`, `shirt` |
| Week 7 | Regular Expressions | `numb3rs`, `watch`, `um`, `working`, `response` |
| Week 8 | Object-Oriented Programming | `jar`, `seasons`, `shirtificate` |
| Week 9 | Final Project | `project` |

---

## 🗂️ Problem Set Descriptions

### Week 0 — Functions & Variables

**`indoor.py`**
Converts any user input to lowercase — simulating the idea that typing in all caps online is like shouting.

**`playback.py`**
Replaces every space in user input with `...`, mimicking a slow-playback effect.

**`faces.py`**
Converts text emoticons `:)` and `:(` into their corresponding emoji 🙂 🙁.

**`einstein.py`**
Implements Einstein's mass-energy equivalence formula E = mc², prompting the user for a mass in kg and outputting energy in Joules.

**`tip.py`**
A tip calculator: takes a meal cost and desired tip percentage, strips the `$` and `%` symbols, and prints the tip amount formatted to 2 decimal places.

---

### Week 1 — Conditionals

**`deep.py`**
Asks the user for the answer to life, the universe, and everything. Accepts `42`, `forty-two`, or `forty two` (case-insensitive) as correct answers.

**`bank.py`**
A greeting-based cash machine: returns $0 for "hello", $20 for any other "h" greeting, and $100 for anything else. Uses string methods for case-insensitive matching.

**`meal.py`**
Given a time in HH:MM format, determines whether it is breakfast (7–8), lunch (12–13), or dinner (18–19) time.

**`extensions.py`**
Maps a filename's extension to its MIME type (e.g. `.jpg` → `image/jpeg`), defaulting to `application/octet-stream` for unknown types.

**`interpreter.py`**
A basic arithmetic interpreter: parses an expression like `3 + 4` split by spaces and computes the result, printed to 1 decimal place.

---

### Week 2 — Loops

**`camel.py`**
Converts a camelCase variable name to snake_case by iterating character by character and inserting underscores before uppercase letters.

**`coke.py`**
Simulates a Coke vending machine that costs 50 cents. Accepts coins of 5, 10, or 25 cents in a loop until the balance is met, then returns change.

**`twttr.py`**
Strips all vowels from a string, inspired by Twitter's old character limits. The core logic is in a `shorten()` function for testability.

**`nutrition.py`**
Looks up the calorie count of a fruit entered by the user using a dictionary of FDA nutrition data.

**`plates.py`**
Validates Massachusetts vanity licence plates: must start with 2 letters, be 2–6 characters long, contain no leading zeros in numbers, and no letters after numbers.

---

### Week 3 — Exceptions

**`fuel.py`**
Converts a fraction (e.g. `3/4`) to a fuel gauge percentage. Handles `ZeroDivisionError` and `ValueError`, displaying `E` for ≤1% and `F` for ≥99%.

**`grocery.py`**
Builds a sorted, deduplicated grocery list from user input (one item per line). Counts duplicate entries and prints each item with its quantity, all uppercased.

**`outdated.py`**
Converts dates in either `Month DD, YYYY` or `MM/DD/YYYY` format to ISO 8601 (`YYYY-MM-DD`), rejecting invalid input and re-prompting.

**`taqueria.py`**
An interactive ordering system for a taqueria menu. Keeps a running total and updates it after each valid item, handling `EOFError` to finish the order.

---

### Week 4 — Libraries

**`emojize.py`**
Uses the `emoji` library to convert emoji aliases (e.g. `:thumbs_up:`) into actual emoji characters.

**`figlet.py`**
Renders user input as ASCII art using `pyfiglet`. Accepts an optional `-f <font>` argument; otherwise picks a random font.

**`adieu.py`**
Collects names from the user one per line, then bids farewell using grammatically correct English list joining via the `inflect` library (e.g. "Adieu, adieu, to Hermione, Harry, and Ron").

**`game.py`**
A number-guessing game. The user sets a difficulty level, and the program picks a random integer in that range. Gives "Too small" / "Too large" hints until the player guesses correctly.

**`professor.py`**
A maths quiz generator for levels 1–3 (single, double, and triple digit addition). Gives 3 attempts per question before revealing the answer, then prints a score out of 10.

---

### Week 5 — Unit Tests

**`test_twttr.py` / `twttr.py`**
Unit tests for the `shorten()` function: covers lowercase input, uppercase input, numbers, and special characters.

**`test_bank.py` / `bank.py`**
Unit tests for the `value()` greeting function: tests the "hello", "h-word", and other greeting categories.

**`test_fuel.py` / `fuel.py`**
Unit tests for `convert()` and `gauge()`: checks correct percentage conversion, edge cases (0%, 100%, rounding), and that exceptions are raised for invalid fractions.

**`test_plates.py` / `plates.py`**
Unit tests for `is_valid()`: checks valid plates, plates that are too short/long, wrong starting characters, letters after numbers, leading zeros, and invalid symbols.

---

### Week 6 — File I/O

**`lines.py`**
Counts the lines of actual code in a `.py` file, ignoring blank lines and comments. Takes the filename as a command-line argument.

**`pizza.py`**
Reads a CSV pizza menu and renders it as a formatted ASCII grid table using the `tabulate` library.

**`scourgify.py`**
Cleans a CSV of student records: splits a `name` column in `"Last, First"` format into separate `first` and `last` columns and writes to a new CSV.

**`shirt.py`**
Overlays a CS50 shirt graphic onto a user-provided photo using `Pillow`. Crops and resizes the photo to match the shirt dimensions before compositing.

---

### Week 7 — Regular Expressions

**`numb3rs.py`**
Validates IPv4 addresses using `re.fullmatch`, checking both format (four dot-separated groups) and value range (0–255 each), rejecting leading zeros.

**`watch.py`**
Extracts a YouTube video ID from an HTML `<iframe>` embed tag using regex and returns the equivalent `youtu.be` short URL.

**`um.py`**
Counts the number of times the word "um" appears as a standalone word in a string (not as part of "yummy" or "album"), using `\b` word boundary anchors.

**`working.py`**
Converts a work hours string like `"9 AM to 5 PM"` (with optional minutes) to 24-hour format `"09:00 to 17:00"`, raising `ValueError` for invalid input.

**`response.py`**
Validates an email address using the `validators` library.

---

### Week 8 — Object-Oriented Programming

**`jar.py`**
A `Jar` class modelling a cookie jar with a fixed capacity. Implements `__str__`, `deposit()`, and `withdraw()` with proper validation, plus `capacity` and `size` properties.

**`seasons.py`**
Takes a date of birth in ISO format and prints the number of minutes lived as English words (e.g. "Five hundred twenty-five thousand, six hundred minutes"), using `inflect`.

**`shirtificate.py`**
Generates a personalised CS50 "Shirtificate" PDF using `fpdf2`, overlaying the user's name on a shirt graphic with proper font and colour settings.

---

### Week 9 — Final Project

**`project.py` — Simple Moving Average Crossover Backtest**

A quantitative trading backtester that simulates the classic MA crossover strategy on real historical stock data from Yahoo Finance.

- **`load_prices(ticker, start, end)`** — Downloads daily closing prices using `yfinance`
- **`moving_average(prices, window)`** — Computes a simple rolling average over a sliding window
- **`backtest(prices, short_ma, long_ma)`** — Simulates Golden Cross (buy) and Death Cross (sell) signals day by day
- **`max_drawdown(equity)`** — Computes the worst peak-to-trough portfolio decline
- **`sharpe_ratio(equity)`** — Computes the annualised risk-adjusted return

**Outputs:** Strategy Return, Buy & Hold Return, Max Drawdown, Sharpe Ratio, Total Trades

---

## 🛠️ Requirements

```bash
pip install yfinance inflect emoji pyfiglet tabulate fpdf2 Pillow validators
```

---

## 📝 Notes

- All solutions were written independently as part of my studies.
- This repository is for personal learning and reference only.
- Course: [CS50P — Harvard / edX](https://cs50.harvard.edu/python/)
