# AP Atlas

A dependency-free, independent AP concept-review web application for the 2027 course lineup. Open `index.html` locally or deploy to GitHub Pages.

## Features
- 42 subjects, including AP Cybersecurity and Business with Personal Finance.
- 2,352 question variants generated from 588 original concept/definition pairs (14 per course, four forms per concept). These are not 2,352 independently authored AP-level problems.
- 84 timed review sets (two per subject, 28 questions and 35 minutes each). Sets use distinct variant IDs but share underlying concepts. They are not full-length official-format mock exams.
- Untimed practice, immediate feedback, exam navigation, countdown/auto-submit, answer review and local progress storage.
- Portfolio courses have concept review rather than simulated official exams.

## Deployment
1. Create a new GitHub repository named `AP-Atlas`.
2. Upload the contents of this folder to its main branch.
3. Under Settings → Pages, select Deploy from a branch, main, /(root), then Save.

## Content development
Edit `bank.txt` and run `python build.py` to regenerate `data.js`. All prompts and definitions were written for this project. The course list follows https://apstudents.collegeboard.org/courses and https://apstudents.collegeboard.org/ap-exams-what-to-know/digital-testing-exam-modes.

This is a starter bank, not a comprehensive AP course or a validated exam predictor. Future releases should add independently authored scenario, calculation, passage, listening and free-response items, reviewed by subject experts, with course-specific timing and assessment blueprints. No affiliation with College Board.