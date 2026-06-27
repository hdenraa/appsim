# Decisions

This file documents reviewed and approved decisions for the appsim project.

AI may propose, analyze and validate recommendations, but the project team owns all final decisions.

## Decision log

| ID | Date | Decision | Status | Related artefacts |
| --- | --- | --- | --- | --- |
| DEC-001 | 2026-06-27 | Use ChatGPT Business/Enterprise as the external AI for cross-documentation and code analysis support. | Approved | README.md, recommendations.md, Google Drive documentation |

## DEC-001: External AI for documentation and code analysis

### Decision

The external AI in the project workflow is ChatGPT Business/Enterprise.

### Context

The project uses GitHub repositories for code and markdown artefacts, GitHub Copilot for daily development support, and Google Drive for solution documentation, design descriptions, technical material, presentations and pitch material.

The workflow requires an external AI that can support cross-checking between:

- repository code and structure
- README.md files
- recommendations.md
- decisions.md
- Google Drive documentation

### Rationale

ChatGPT Business/Enterprise is selected because the project needs a broad analysis and documentation assistant, not only an IDE coding assistant. The external AI must help validate consistency between documentation and code, identify recommendations, and support decision material for human review.

GitHub Copilot remains the primary tool for daily coding assistance in the development environment.

### Consequences

- AI-generated or AI-assisted recommendations should be documented in `recommendations.md`.
- Reviewed and approved team decisions should be documented in `decisions.md`.
- Humans remain responsible for prioritization, approval and final decisions.
- The external AI should be treated as analysis, documentation and decision support, not as the decision owner.

### Alternatives considered

- GitHub Copilot: retained for daily development support, but not used as the independent external reviewer.
- Claude Code: strong for deep code analysis, but less suited as the primary cross-documentation and decision-support AI in this workflow.
- Gemini for Workspace: strong for Google Workspace documents, but less suited as the primary cross-GitHub and code-analysis AI in this workflow.
