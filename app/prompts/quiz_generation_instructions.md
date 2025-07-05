## Quiz Generation Format Instructions

> ⚠️ **Important:**  
Ensure that all content is written **strictly** in the specified target language. Do **not** mix languages under any circumstances.  
All internal labels such as `"True"`, `"False"`, `"Correct"`, and `"Incorrect"` must also be translated to match the selected language.

### 🧩 Quiz Structure

Each quiz must include:

- A **title**: A short, descriptive title summarizing the quiz topic.
- A **description**: A brief overview of what the quiz covers.
- A list of **questions**, where each question must contain:

  - `questionType`: Either `"MULTIPLE_CHOICE"` or `"TRUE_OR_FALSE"`.
  - `statement`: The main question prompt.
  - `hint`: A short hint to assist the user.
  - `explanation`: A concise explanation of the correct answer.
  - `correctAnswer`: A string representing the correct option.
  - `options`: A list of 4 answer choices (for multiple choice or true/false), written in the same language as the rest of the quiz.
    - **Note:** Do **not** include option markers such as `a)`, `1)`, `a-`, or `1-`.

### 📦 Output Format

The final output must **strictly follow the structure defined by the `QuizResponse` schema**.  
Ensure that all required fields are present and correctly labeled.
