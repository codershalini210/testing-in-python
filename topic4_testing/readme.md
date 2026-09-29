# Exercise 4.1B – Test a Small Task Component with Reusable Setup

## Objective

Extend your automated testing skills by using a simple pytest fixture
to provide repeatable test data.

You will test a small task-management component using fictional task
records.

---

## Learning Outcomes

By completing this activity, you should be able to:

1. Identify functional requirements from a small Python component.
2. Write basic pytest tests.
3. Understand the structure of test data.
4. Create and use a simple pytest fixture.
5. Test normal and no-match situations.
6. Explain why reusable test setup improves repeatability.
7. Understand when mocking is unnecessary.
8. Introduce a controlled defect and confirm that a test detects it.
9. Inspect individual test failures.
10. Explain your testing decisions in your own words.

---

# Part A – Understand the Component

Open:

    task_manager.py

Read all three functions.

Do not change the component yet.

Complete `student_notes.md`.

---

# Part B – Write a Direct Test

Open:

    test_task_manager_direct.py

Run:

    pytest test_task_manager_direct.py

Confirm that the test passes.

Study how the task data is created inside the test.

---

# Part C – Identify Repeated Setup

Look at the test data.

Consider:

- Is the same task data likely to be needed by multiple tests?
- Would copying the same list into every test be useful?
- What problems could occur if the data had to be changed later?

Record your observations in your notes.

---

# Part D – Create a Fixture

Open:

    conftest.py

Study the supplied `sample_tasks` fixture.

Understand:

    @pytest.fixture

and:

    def sample_tasks():

The fixture returns the fictional task dataset.

---

# Part E – Write Tests Using the Fixture

Open:

    test_task_manager.py

Complete the five tests.

You must test:

1. Counting completed tasks.
2. Finding an existing task.
3. Finding a missing task.
4. Updating an existing task.
5. Attempting to update a missing task.

---

# Part F – Run the Test Suite

Run:

    pytest

Inspect the output.

Do not only look at the number of passed tests.

If a test fails:

1. Identify which test failed.
2. Read the failure message.
3. Identify the expected result.
4. Identify the actual result.
5. Decide whether the problem is in the test or the component.
6. Correct the problem.
7. Run the tests again.

---

# Part G – Controlled Defect

Make a copy of `task_manager.py`.

Call it:

    task_manager_defective.py

Introduce ONE simple defect.

For example, change:

    return sum(1 for task in tasks if task["status"] == "completed")

to:

    return sum(1 for task in tasks if task["status"] == "pending")

Do not introduce multiple defects.

Change your test import temporarily so that it tests the defective version.

Run the tests.

Record:

- Which test failed?
- What was expected?
- What was actually returned?
- Why did the test detect the defect?

---

# Part H – Restore the Correct Component

Restore the original correct component.

Run:

    pytest

Confirm that all tests pass again.

---

# Part I – AI Explanation

Ask an AI assistant:

"Explain why using a pytest fixture improves repeatability in
this specific task-management test suite."

Record the main points from the AI response.

Then compare them with your own observations.

Answer:

Did the AI explanation match your understanding?

Why or why not?

---

# Part J – Reflection

Write a short reflection of approximately 150–250 words.

Your reflection should answer:

1. How did the fixture help your tests?
2. What repeated setup did it remove?
3. What happened when the controlled defect was introduced?
4. Which test detected the defect?
5. Why is it important to inspect individual failures?
6. Why was complicated mocking unnecessary for this exercise?
7. When might reusable setup become useful in a larger project?

---

# Submission

Submit the following files:

- task_manager.py
- conftest.py
- test_task_manager_direct.py
- test_task_manager.py
- student_notes.md
- README.md or completed activity record
- defective component copy, if requested by your tutor
- reflection

Your tests must run successfully against the corrected component.
