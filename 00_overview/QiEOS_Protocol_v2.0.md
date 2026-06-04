---
title: QiEOS Protocol v2.0
type: governance
author: QiAlly Systems (C. Rice-Velasquez)
created: 2025-11-01
last_updated: 2025-11-01
status: active
---

# 🜂 The QiEOS Protocol v2.0
_The governing charter of the QiOne™ ecosystem (Unified Decimal Edition)._

---

## PREAMBLE
QiEOS defines the unified structure of **QiOne**, integrating personal, business, and client systems into one modular, traceable framework.  
Each entity in QiOne holds a unique **QiDecimal ID** (x.xx.xx format), ensuring order, interoperability, and consistency across all knowledge realms.  
QiEOS governs structure, QiCode defines law, and QiKBs embody practice.

---

## ARTICLE I — Realm Structure

```

QiOne/
├── 0_Inbox/                 → Temporary intake area
├── 1_QiEos/                 → Governance Realm (Constitution + Law)
│   ├── 1.10_Protocol/
│   │   └── QiEOS_Protocol_v2.0.md
│   ├── 1.20_QiCode/
│   │   ├── 1.21_Title_Foundations/
│   │   │   ├── 1.21.1_Principle_of_Awareness.md
│   │   │   └── 1.21.2_Principle_of_Presence.md
│   │   ├── 1.22_Title_Self_and_Inner_Work/
│   │   ├── 1.23_Title_Work_and_Creation/
│   │   ├── 1.24_Title_Relations_and_Exchange/
│   │   ├── 1.25_Title_Action_and_Automation/
│   │   ├── 1.26_Title_Identity_and_Integrity/
│   │   ├── 1.27_Title_Mind_and_Will/
│   │   ├── 1.28_Title_Cycles_and_Closure/
│   │   ├── 1.29_Title_Ethics_and_Evolution/
│   │   └── 1.30_Title_Legacy_and_Design/
│   ├── 1.30_Templates/
│   ├── 1.40_RAG/
│   ├── 1.50_Meta/
│   └── 1.90_ARCH/
│
├── 2_QsKb/                  → Personal Knowledge Base (QiSelf)
│   ├── 2.10_START/
│   ├── 2.20_ABOUT/
│   ├── 2.30_LIFE/
│   ├── 2.40_OPS/
│   ├── 2.50_DOCS/
│   ├── 2.60_MEDIA/
│   ├── 2.70_TECH/
│   └── 2.90_ARCH/
│
├── 3_QiKb/                  → Business Knowledge Base (QiAlly)
│   ├── 3.10_START/
│   ├── 3.20_ABOUT/
│   ├── 3.30_OFFER/
│   ├── 3.40_OPS/
│   ├── 3.50_DOCS/
│   ├── 3.60_MEDIA/
│   ├── 3.70_TECH/
│   └── 3.90_ARCH/
│
├── 4_Clients/               → Client Ecosystems
│   ├── 4.10_<slug>/
│   │   ├── 4.11_EOS/
│   │   ├── 4.12_KB/
│   │   └── 4.13_SITE/
│   └── 4.90_ARCH/
│
├── 5_Apps/                  → Application Layer
│   ├── 5.10_dev/
│   ├── 5.20_staging/
│   ├── 5.30_live/
│   └── 5.90_ARCH/
│
├── 6_Data/                  → Datasets and Indexes
│   ├── 6.10_qi_index/
│   ├── 6.20_vector/
│   ├── 6.30_datasets/
│   └── 6.90_ARCH/
│
├── 7_Tools/                 → Scripts and Utilities
│   ├── 7.10_python/
│   ├── 7.20_node/
│   ├── 7.30_shell/
│   └── 7.90_ARCH/
│
├── 8_Docs/                  → Manuals and Publications
│   ├── 8.10_Manuals/
│   ├── 8.20_Brand/
│   ├── 8.30_Publications/
│   └── 8.90_ARCH/
│
└── 9_ARCH/                  → Global Cold Storage

```

---

## ARTICLE II — QiDecimal System

Each folder or file carries a **QiDecimal ID** that denotes:
- Its **realm** (first digit, 0–9)
- Its **subrealm** or **category** (first decimal)
- Its **atomic entry** (second decimal)

Example:  
`1.21.1` → QiEOS → QiCode → Title 1 → §1 “Principle of Awareness”

The QiDecimal Registry is maintained in `/1_QiEos/1.50_Meta/QiCodex.csv`.

---

## ARTICLE III — Hierarchy & Authority

| Layer | Function | Type |
|--------|-----------|------|
| **QiOne** | Universe (root realm) | Whole ecosystem |
| **QiEOS** | Constitution | Governance |
| **QiCode** | Law | Statutes & Principles |
| **QiKBs** | Practice | SOPs & Workflows |
| **Clients** | Application | Implementation |
| **Apps / Tools** | Automation | Execution |
| **Data / Docs** | Memory | Records & Communication |

---

## ARTICLE IV — Versioning & Continuity

- Every update increments by minor version (v2.1, v2.2, etc.)
- Deprecated files move to `x.90_ARCH/`
- No deletion without archival entry in `/1.50_Meta/INDEX.csv`
- The QiCodex must reflect all assigned QiDecimal IDs — no ad-hoc numbering.

---

## ARTICLE V — Privacy & Sovereignty

| Realm | Default Privacy | Description |
|--------|-----------------|--------------|
| `2_QsKb` | Private | Personal thoughts & reflections |
| `3_QiKb` | Shared | QiAlly operations & business data |
| `4_Clients` | Isolated | One per client; strict data boundaries |
| `5_Apps` | Public / Controlled | Deployments, codebases |
| `6_Data` | Controlled | Indexes, vectors, exports |
| `7_Tools` | Shared | Code utilities |
| `8_Docs` | Public | Published content |

---

## ARTICLE VI — AI Governance

- All AI agents are indexed in `/1.40_RAG/bots/*.yaml`
- Agents inherit scope from their QiDecimal parent realm.
- Private materials are excluded unless explicitly authorized.

---

## ARTICLE VII — Updates & Ratification

1. Propose draft under `/1.10_Protocol/Drafts/`
2. Review via Qi-Master or manual audit.
3. Ratify → rename to `QiEOS_Protocol_vX.Y.md`
4. Log update in `/1.50_Meta/QiCodex.csv`
5. Archive prior versions under `/1.10_Protocol/Archive/`

---

## ARTICLE VIII — Founding Principles

> Flat over nested.  
> Linked over duplicated.  
> Documented over remembered.  
> Modular over massive.

QiOne remains a living system: coherent, portable, and recursively self-governing.

---

**QiEOS Protocol v2.0 — Ratified 2025-11-01**  
_Stewarded by QiAlly Systems (C. Rice-Velasquez)._
```

---

## 📘 **QiCodex.csv — Global Decimal Registry**

The QiCodex is maintained as a CSV file at `/1_QiEos/1.50_Meta/QiCodex.csv`. Below is a markdown reference format:

```markdown
---
title: QiCodex Registry
version: 2.0
maintainer: QiAlly Systems (C. Rice-Velasquez)
updated: 2025-11-01
---

# 📘 QiCodex — Unified Decimal Registry
_All folders, files, and modules in QiOne share a single QiDecimal namespace._

| ID | Name | Description | Owner | Status |
|----|------|--------------|--------|--------|
| 0 | Inbox | Temporary workspace for uncategorized input | CRV | active |
| 1 | QiEOS | Governance Realm (Constitution + Law) | CRV | active |
| 1.10 | Protocol | QiEOS governance & update process | QiEOS | active |
| 1.20 | QiCode | Life Code (Statutes of System & Self) | QiEOS | active |
| 1.21 | Title I — Foundations | Core principles & structure | QiCode | active |
| 1.21.1 | §1 Principle of Awareness | Law of observation & reflection | QiCode | active |
| 1.21.2 | §2 Principle of Presence | Law of now & embodiment | QiCode | active |
| 1.22 | Title II — Self & Inner Work | Awareness, habits, emotional systems | QiCode | active |
| 1.23 | Title III — Work & Creation | Productivity, flow, and manifestation | QiCode | active |
| 1.24 | Title IV — Relations & Exchange | Boundaries, reciprocity, and connection | QiCode | active |
| 1.25 | Title V — Action & Automation | Execution, energy management, movement | QiCode | active |
| 1.26 | Title VI — Identity & Integrity | Authenticity, naming, and alignment | QiCode | active |
| 1.27 | Title VII — Mind & Will | Decision-making, thought hygiene | QiCode | active |
| 1.28 | Title VIII — Cycles & Closure | Endings, transitions, forgiveness | QiCode | active |
| 1.29 | Title IX — Ethics & Evolution | Moral systems, feedback, growth | QiCode | active |
| 1.30 | Title X — Legacy & Design | Purpose, continuity, vision | QiCode | active |
| 1.30_Templates | Templates | Master templates (App/KB/Client) | QiEOS | active |
| 1.40 | RAG | AI bots, embeddings, and automation layer | QiEOS | active |
| 1.50 | Meta | Indexes, QiCodex, and registry data | QiEOS | active |
| 1.90 | ARCH | Archive of retired QiEOS components | QiEOS | active |
| 2 | QiSelf KB | Personal Knowledge Base | CRV | active |
| 2.10 | START | Overview, system map | CRV | active |
| 2.20 | ABOUT | Story, identity | CRV | active |
| 2.30 | LIFE | Habits, goals, and reflections | CRV | active |
| 2.40 | OPS | Personal workflows and routines | CRV | active |
| 2.50 | DOCS | Personal writings, letters, thoughts | CRV | active |
| 2.60 | MEDIA | Visuals, recordings, transcripts | CRV | active |
| 2.70 | TECH | Automations, scripts, prompts | CRV | active |
| 2.90 | ARCH | Archived personal data | CRV | active |
| 3 | QiAlly KB | Business Knowledge Base | QiAlly | active |
| 3.10 | START | Mission, purpose, branding | QiAlly | active |
| 3.20 | ABOUT | Structure, team, org identity | QiAlly | active |
| 3.30 | OFFER | Services, pricing, strategy | QiAlly | active |
| 3.40 | OPS | SOPs, process docs | QiAlly | active |
| 3.50 | DOCS | Contracts, reports, deliverables | QiAlly | active |
| 3.60 | MEDIA | Design, marketing, assets | QiAlly | active |
| 3.70 | TECH | APIs, automations, integrations | QiAlly | active |
| 3.90 | ARCH | Archived business content | QiAlly | active |
| 4 | Clients | Client Ecosystems | QiAlly | active |
| 4.10 | <slug> | Individual client container | QiAlly | active |
| 4.11 | EOS | Agreements & scope | QiAlly | active |
| 4.12 | KB | Client-specific knowledge base | QiAlly | active |
| 4.13 | SITE | Client site or PWA | QiAlly | active |
| 4.90 | ARCH | Archived client data | QiAlly | active |
| 5 | Apps | Application Layer | QiSuite | active |
| 5.10 | dev | Development environment | QiSuite | active |
| 5.20 | staging | Testing environment | QiSuite | active |
| 5.30 | live | Production environment | QiSuite | active |
| 5.90 | ARCH | Archived deployments | QiSuite | active |
| 6 | Data | Datasets & Indexes | QiSuite | active |
| 6.10 | qi_index | Core knowledge index | QiSuite | active |
| 6.20 | vector | Embeddings & RAG data | QiSuite | active |
| 6.30 | datasets | External datasets | QiSuite | active |
| 6.90 | ARCH | Archived data | QiSuite | active |
| 7 | Tools | Scripts & Utilities | QiSuite | active |
| 7.10 | python | Python utilities | QiSuite | active |
| 7.20 | node | Node.js utilities | QiSuite | active |
| 7.30 | shell | Shell scripts | QiSuite | active |
| 7.90 | ARCH | Archived tools | QiSuite | active |
| 8 | Docs | Manuals & Publications | QiAlly | active |
| 8.10 | Manuals | Guides, handbooks | QiAlly | active |
| 8.20 | Brand | Logos, templates, style | QiAlly | active |
| 8.30 | Publications | External reports | QiAlly | active |
| 8.90 | ARCH | Archived documents | QiAlly | active |
| 9 | ARCH | Global Archive | QiOne | active |
```

---

✅ **What This Achieves**

* Unified numbering from root to law section.
* No padding above 9 — visually minimal and calm.
* All sub-realms and laws predictable (`x.10`, `x.20`, `x.21.1`, etc.).
* One codex to rule all numbering — no improvising IDs ever again.

---

The **QiCodex.csv** file serves as the machine-readable registry for all QiDecimal IDs, ready for `/1.50_Meta/` index automation and future AI lookups.
