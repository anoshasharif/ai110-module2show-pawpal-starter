# PawPal+ Project Reflection

## 1. System Design

**a. Initial design**

- Briefly describe your initial UML design.
- What classes did you include, and what responsibilities did you assign to each?

My initial design includes four main classes: `Owner`, `Pet`, `Task`, and `Scheduler`. The `Owner` class stores the owner's name and their pets. The `Pet` class stores basic pet information and the tasks connected to that pet. The `Task` class represents care tasks like feeding, walks, medication, grooming, or appointments. The `Scheduler` class organizes those tasks into a daily plan based on priority, duration, and available time.

The three main actions users should be able to perform are:
1. Add and manage pets.
2. Add or edit pet care tasks.
3. Generate a daily schedule for the pet's care.

**b. Design changes**

- Did your design change during implementation?
- If yes, describe at least one change and why you made it.

During implementation, I added features like task times, due dates, conflict detection, and recurring tasks. These changes made the scheduler more useful and better matched the project requirements.

---

## 2. Scheduling Logic and Tradeoffs

**a. Constraints and priorities**

- What constraints does your scheduler consider (for example: time, priority, preferences)?
- How did you decide which constraints mattered most?
My scheduler considers task priority, scheduled time, completion status, and recurring tasks. I focused on these because they are the most important for organizing a daily pet care schedule.

**b. Tradeoffs**

- Describe one tradeoff your scheduler makes.
- Why is that tradeoff reasonable for this scenario?

My scheduler only checks if two tasks have the exact same start time. It does not check whether tasks overlap based on their duration. This keeps the algorithm simple but may miss some scheduling conflicts.

---

## 3. AI Collaboration

**a. How you used AI**

- How did you use AI tools during this project (for example: design brainstorming, debugging, refactoring)?
- What kinds of prompts or questions were most helpful?

I used AI to brainstorm my UML design, generate class skeletons, implement methods, debug errors, and write tests. The most helpful prompts asked AI to explain or improve specific parts of my code.

**b. Judgment and verification**

- Describe one moment where you did not accept an AI suggestion as-is.
- How did you evaluate or verify what the AI suggested?

I did not accept every AI suggestion without checking it. I tested the code myself using main.py, Streamlit, and pytest to make sure everything worked correctly.
---

## 4. Testing and Verification

**a. What you tested**

- What behaviors did you test?
- Why were these tests important?

I tested task completion, adding tasks, sorting by time, recurring tasks, and conflict detection. These tests confirmed that the main features of the scheduler worked correctly.

**b. Confidence**

- How confident are you that your scheduler works correctly?
- What edge cases would you test next if you had more time?

I am fairly confident that my scheduler works correctly because all of my tests passed. If I had more time, I would test overlapping task durations and more complex scheduling situations.

---

## 5. Reflection

**a. What went well**

- What part of this project are you most satisfied with?

I am most satisfied with connecting my backend logic to the Streamlit app and seeing the scheduler work.

**b. What you would improve**

- If you had another iteration, what would you improve or redesign?

I would improve the conflict detection by checking for overlapping task durations instead of only matching start times.

**c. Key takeaway**

- What is one important thing you learned about designing systems or working with AI on this project?

I learned that AI is a helpful tool, but I still needed to review, test, and verify the code to make sure it met the project requirements.
