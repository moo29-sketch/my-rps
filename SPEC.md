# Rock, Paper, Scissors

## RPS-001: Play a round

**Purpose:** one person plays a quick round against the computer.

- Choose rock, paper, or scissors. The computer chooses one move for that round.
- Display both choices and the result: **You win!**, **Computer wins**, or **It’s a tie**.
- Choosing again starts an independent round. No score or saved history.
- Keep the supplied interface and server. Name/color changes can wait until the rules work.

### Expected results

Results are from the **player’s perspective**. `determine_winner(player, computer)` in `game.py` returns `win`, `lose`, or `tie`. Inputs are the lowercase moves below; the supplied server rejects other choices.

| Player | Computer | Expected return |
| --- | --- | --- |
| rock | rock | tie |
| rock | paper | lose |
| rock | scissors | win |
| paper | rock | win |
| paper | paper | tie |
| paper | scissors | lose |
| scissors | rock | lose |
| scissors | paper | win |
| scissors | scissors | tie |

### Agreed plan

**Working plan (reviewed with AI; student should confirm their prediction):**

- Prediction to discuss: if the player chooses **rock** and the computer chooses **paper**, the player **loses**, because paper covers rock.
- Build only the missing `determine_winner(player, computer)` rules while retaining the supplied Flask server and interface.
- Use all nine matchups above for unit tests. Test a **valid loss** (rock against paper) as normal game behavior, not an invalid request.
- Test an **unsupported input** such as `lizard` and a missing choice: both must produce HTTP 400 and a helpful message without running the rules.
- Test a real Flask request with a deterministic computer move, then a real Chromium round and replay with deterministic computer choices but the **real** winner function.
- Run the full checker, review the changes, manually play and use keyboard controls, then document actual evidence. Do not add scores, persistence, or a framework.

**Student confirmation/prediction:** Not recorded yet. Replace the draft wording only after the student reviews it.

### Checks

Before coding, agree this small test plan with AI:

| Level | Cases and evidence |
| --- | --- |
| Unit — positive | All nine literal expected results above, including valid losses and ties. |
| Integration — positive | A submitted round uses the real rule function and displays both choices and the correct result. Fix the computer choice for the test. |
| Integration — negative | Reuse supplied missing/unsupported-move tests: HTTP 400 and a helpful explanation, without calling the rules. A crash is not the intended result. |
| E2E — positive | Add a real-browser round and replay in tests/e2e/test_round.py using the supplied live_server/page fixtures. Fix only the computer choice; use real rules and real HTTP. |

Use `unit`, `integration`, and `e2e` pytest markers. Run `.venv/bin/python check.py` for Black, Pylint, fast tests, and browser checks; then review the diff. Keep shared settings and meaningful assertions intact. The student still plays, inspects a rule and its test, and gives feedback. Browser automation does not establish every aspect of usability or application performance.

### Work record

- **Issue:** https://github.com/moo29-sketch/my-rps/issues/1
- **Pull request (merged):** [Add actual merged PR URL after merge]. Use `Closes #ISSUE_NUMBER` in the PR description.
- **Final CI run:** [Add the actual GitHub Actions run URL for the final PR commit] (not available in this offline workpack).
- **Code:** [game.py](game.py) — implements real `determine_winner` rules with no server/framework changes.
- **Unit and request tests:** [tests/test_game.py](tests/test_game.py) — nine explicit outcome combinations and one real Flask request/result check.
- **Browser test:** [tests/e2e/test_round.py](tests/e2e/test_round.py) — real HTTP/browser round and replay with a deterministic computer move. The supplied negative request tests in [tests/test_shell.py](tests/test_shell.py) remain unchanged.
- **Earlier local check on Windows before these feature tests were copied in:** Python 3.12.10; Black PASS; Pylint PASS; 13 non-browser tests PASS; 5 Chromium tests PASS. These were starter-baseline results and **do not** verify the added RPS-001 tests. Run the full `.\.venv\Scripts\python.exe check.py` again after copying these files, and replace this entry with the actual final counts and statuses. The Windows-only test cleanup change lets the spawned development server exit after browser tests. A prior test log showed hanging cleanup; do not claim a final feature-test pass until verified.
- **One test and the mistake it catches (draft for student review):** `test_all_nine_outcomes` has the literal case `("rock", "paper", "lose")`; it would catch a reversed paper/rock winner rule. Student explanation: [record student's own explanation].
- **Manual browser round:** Player [actual move], computer [actual move], displayed result [actual result], explanation [student's observation]. Not yet observed; do not fill with a made-up round.
- **Replay and keyboard:** [record actual replay and Tab/Enter observations]. Not yet manually verified.
- **Help received:** ChatGPT assisted with the game function, tests, Windows test-process cleanup, and this evidence index. The student reviews, runs checks, plays and observes a round, and performs the GitHub issue/PR/CI steps.
- **Final GitHub status:** [after pushing SPEC.md update, verify last PR commit CI passes, merge, check issue closes and `main` contains changes].
