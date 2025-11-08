# Rule: Generating a Task List from a PRD

## Goal

To guide an AI assistant in creating a detailed, step-by-step task list in Markdown format based on an existing Product Requirements Document (PRD). The task list should guide a developer through implementation.

## Output

- **Format:** Markdown (`.md`)
- **Location:** `/tasks/`
- **Filename:** `tasks-[prd-file-name].md` (e.g., `tasks-prd-user-profile-editing.md`)

## Process

1.  **Receive PRD Reference:** The user points the AI to a specific PRD file
2.  **Analyze PRD:** The AI reads and analyzes the functional requirements, user stories, and other sections of the specified PRD.
3.  **Assess Current State:** Review the existing codebase to understand existing infrastructre, architectural patterns and conventions. Also, identify any existing components or features that already exist and could be relevant to the PRD requirements. Then, identify existing related files, components, and utilities that can be leveraged or need modification.
4.  **Phase 1: Generate Parent Tasks:** Based on the PRD analysis and current state assessment, create the file and generate the main, high-level tasks required to implement the feature. Use your judgement on how many high-level tasks to use. It's likely to be about 5. Present these tasks to the user in the specified format (without sub-tasks yet). Inform the user: "I have generated the high-level tasks based on the PRD. Ready to generate the sub-tasks? Respond with 'Go' to proceed."
5.  **Wait for Confirmation:** Pause and wait for the user to respond with "Go".
6.  **Phase 2: Generate Sub-Tasks:** Once the user confirms, break down each parent task into smaller, actionable sub-tasks necessary to complete the parent task. Ensure sub-tasks logically follow from the parent task, cover the implementation details implied by the PRD, and consider existing codebase patterns where relevant without being constrained by them.
7.  **Identify Relevant Files:** Based on the tasks and PRD, identify potential files that will need to be created or modified. List these under the `Relevant Files` section, including corresponding test files if applicable.
8.  **Generate Final Output:** Combine the parent tasks, sub-tasks, relevant files, and notes into the final Markdown structure.
9.  **Save Task List:** Save the generated document in the `/tasks/` directory with the filename `tasks-[prd-file-name].md`, where `[prd-file-name]` matches the base name of the input PRD file (e.g., if the input was `prd-user-profile-editing.md`, the output is `tasks-prd-user-profile-editing.md`).
10. **Generate Tasks in Jira:**
    - **Check Jira MCP Availability:** First, check if Jira MCP (Model Context Protocol) is available by attempting to access Jira-related tools or checking available MCP resources.
    - **Connect to Jira:** If Jira MCP is available, connect to Jira by:
      - Getting accessible Atlassian resources using `getAccessibleAtlassianResources`
      - Retrieving user information to verify connection using `atlassianUserInfo`
      - Getting visible Jira projects using `getVisibleJiraProjects` with the appropriate cloud ID
    - **Determine Issue Type:** Based on the scope and complexity of the PRD:
      - Use **Epic** if the feature is large, spans multiple sprints, or contains multiple major components
      - Use **Story** if the feature is a single, cohesive user-facing feature that can be completed in one sprint
      - Generally, if there are 5+ parent tasks or the feature is substantial, prefer Epic; otherwise, use Story
    - **Create Main Issue (Epic or Story):**
      - Create the main issue using `createJiraIssue` with:
        - Appropriate issue type (Epic or Story)
        - Summary: Brief feature name from PRD
        - Description: Include PRD overview, goals, key features, and link to the task list file
        - Reference the PRD and task list files in the description
    - **Create Sub-Tasks for Each Parent Task:**
      - For each parent task (e.g., 1.0, 2.0, 3.0), create a sub-task using `createJiraIssue`:
        - Issue type: **Subtask**
        - Parent issue key: Use the `parentIssueKey` parameter with the key of the main Epic/Story created above (e.g., "SCRUM-6")
        - Summary: Parent task title (e.g., "1.0 Project Setup & Dependencies")
        - Description: Include the parent task description and list all sub-tasks (1.1, 1.2, etc.) as a checklist in markdown format
        - Link to the relevant section in the task list markdown file
        - Note: Each parent task from the markdown task list becomes one Jira sub-task, with all its sub-tasks (1.1, 1.2, etc.) listed as a checklist in the description
    - **Link and Organize:**
      - Ensure all sub-tasks are properly linked to the parent Epic/Story
      - Add the Jira issue key(s) to the task list markdown file for reference
      - Update the task list with Jira links if possible
    - **If Jira MCP is Not Available:**
      - Inform the user that Jira integration is not available
      - Suggest manual creation of Jira issues using the task list as a guide
      - Provide a summary of what should be created (main Epic/Story and sub-tasks for each parent task)

## Output Format

The generated task list _must_ follow this structure:

```markdown
## Relevant Files

- `path/to/potential/file1.ts` - Brief description of why this file is relevant (e.g., Contains the main component for this feature).
- `path/to/file1.test.ts` - Unit tests for `file1.ts`.
- `path/to/another/file.tsx` - Brief description (e.g., API route handler for data submission).
- `path/to/another/file.test.tsx` - Unit tests for `another/file.tsx`.
- `lib/utils/helpers.ts` - Brief description (e.g., Utility functions needed for calculations).
- `lib/utils/helpers.test.ts` - Unit tests for `helpers.ts`.

### Notes

- Unit tests should typically be placed alongside the code files they are testing (e.g., `MyComponent.tsx` and `MyComponent.test.tsx` in the same directory).
- Use `npx jest [optional/path/to/test/file]` to run tests. Running without a path executes all tests found by the Jest configuration.

## Tasks

- [ ] 1.0 Parent Task Title
  - [ ] 1.1 [Sub-task description 1.1]
  - [ ] 1.2 [Sub-task description 1.2]
- [ ] 2.0 Parent Task Title
  - [ ] 2.1 [Sub-task description 2.1]
- [ ] 3.0 Parent Task Title (may not require sub-tasks if purely structural or configuration)
```

## Interaction Model

The process explicitly requires a pause after generating parent tasks to get user confirmation ("Go") before proceeding to generate the detailed sub-tasks. This ensures the high-level plan aligns with user expectations before diving into details.

## Target Audience

Assume the primary reader of the task list is a **junior developer** who will implement the feature with awareness of the existing codebase context.
