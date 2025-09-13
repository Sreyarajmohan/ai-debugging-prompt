# AI Debugging Prompt for FOSSEE Internship

This repository contains my submission for the AI Debugging Assistant internship task by FOSSEE.

## Files Included

- ai_debug_prompt.md: The AI prompt designed to guide the assistant in helping students debug Python code.
- reasoning.md: Explanation of the approach, tone, and adaptability of the prompt.
- design_choices.md: The reasoning behind key decisions made while crafting the prompt.
- demo: Example Python scripts demonstrating AI hints in action.
- 
## Setup Instructions
1. Clone the Repository
git clone https://github.com/FOSSEE/workshop_booking.git

cd workshop_booking

3. Open the Project in a Code Editor

4. Run the Website
Option A: Open index.html Directly

Go to the project folder

Double-click index.html to open it in your browser

Option B: Use Live Server (VS Code)

Install "Live Server" extension in VS Code

Right-click index.html → Open with Live Server

## Purpose

The goal of this prompt is to help students identify bugs in their Python code by receiving hints and questions from the AI without giving away direct answers. The assistant encourages critical thinking and adapts to the learner’s level.
This project provides an AI assistant that:

- Analyzes Python code for potential bugs
- Gives helpful hints and guiding questions
- Encourages step-by-step problem-solving
- Adapts hints to the learner’s skill level
- Avoids revealing the correct solution

The goal is to help students think critically and learn from mistakes independently.

## How It Works
1. A student writes Python code that may contain bugs.  
2. The AI prompt analyzes the code and identifies potential issues.  
3. The AI provides hints and guiding questions to help the student bug.  
4. The student uses these hints to correct their code.  
5. Hints are adaptive:  
   - Beginners receive simpler, more direct guidance  
   - Advanced learners receive probing questions to challenge their logic

##  Reasoning Summary

- Tone & Style: Friendly, encouraging
- Avoids Solutions: Only hints/questions; no direct code fixes
- Balancing Guidance: Highlights bugs while nudging the student to think
- Skill-Level Adaptation: Simple hints for beginners, deeper questions for advanced learners
  
##  Demo

Example scripts are included in the demo/ folder:
```bash
demo/eg_1.py
demo/eg_2.py
demo/eg_3.py
```
Thank you for reviewing my submission.
