# QiCode — Personal Legal Code

QiCode is your **personal legal code** — the immutable principles and statutes by which you live and work.

## Quick Start

1. **Browse Titles** — Review the 10 Title directories to see the domain structure
2. **Read Principles** — Each Principle is a binding statute with specific applications
3. **Add New Principles** — Use `_TEMPLATE_Principle.md` as a starting point
4. **Update Title Indexes** — Always update the Title index when adding Principles

## Structure

```
1.20_QiCode/
├── 1.20.00_QiCode_Index.md          # Master overview
├── _TEMPLATE_Principle.md            # Template for new Principles
├── 1.21_Title_Foundations/           # Title I
│   ├── 1.21.00_Title_Index.md
│   ├── 1.21.1_Principle_of_Awareness.md
│   └── 1.21.2_Principle_of_Presence.md
├── 1.22_Title_Self_and_Inner_Work/  # Title II
│   └── 1.22.00_Title_Index.md
├── 1.23_Title_Work_and_Creation/     # Title III
│   └── 1.23.00_Title_Index.md
├── [8 more Titles...]
└── 1.30_Title_Legacy_and_Design/     # Title X
    └── 1.30.00_Title_Index.md
```

## Adding a New Principle

1. Copy `_TEMPLATE_Principle.md` to the appropriate Title directory
2. Name it: `1.XX.Y_Principle_of_[Name].md` (increment Y from existing Principles)
3. Fill in the template with:
   - **Statute**: The core law in bold statement form
   - **Application**: Where and when it applies
   - **Exceptions**: Any edge cases (or "None")
   - **Related Principles**: Cross-references to other Principles
4. Update the Title's index file (`1.XX.00_Title_Index.md`) to include the new Principle
5. Update `1.50_Meta/QiCodex.csv` with the new QiDecimal ID

## Principle Format

Each Principle follows this structure:
- **YAML Front Matter** with metadata (qi_decimal, parent, etc.)
- **Statute** section — the core law
- **Application** section — where it applies
- **Exceptions** section — edge cases
- **Related Principles** section — cross-references

## QiDecimal IDs

- `1.XX` = Title number (21-30)
- `1.XX.Y` = Principle number within Title
- Always increment sequentially — no gaps or reuse

## Amendment Process

Principles are **immutable by default**. To change:
1. Create new version or amendment proposal
2. Review for conflicts with existing Principles
3. Ratify by updating indexes and QiCodex
4. Archive superseded versions in `1.90_ARCH/`

## Next Steps

- Review Title I (Foundations) to see example Principles
- Draft Principles for Titles relevant to current needs
- Reference QiCode in workflows and SOPs as "governing law"

