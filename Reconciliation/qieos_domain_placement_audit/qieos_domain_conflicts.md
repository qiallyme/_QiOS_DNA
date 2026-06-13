# QiEOS Domain Placement Audit: Reference Risks and Conflicts

This report highlights files that present a reference risk (linked or imported by other files) or have potential naming conflicts during migration.

## 1. High Reference Risk Files
The following files are explicitly referenced in index configurations (`docs.json`, `file-index.json`, `build.js`) or other Markdown documents. Moving these files will break existing links unless reference indexes are updated:

### File: `_index.md`
- **Current Path**: `00_QiEOS/10_governance/10_principles/_index.md`
- **Proposed Move**: `00_QiEOS/_index.md`
- **Referenced in**:
  * `[_index.md](file:///C:/QiLabs/_QiOS_DNA/00_QiEOS/_index.md)`
  * `[_index.md](file:///C:/QiLabs/_QiOS_DNA/00_QiEOS/10_governance/_index.md)`
  * `[blueprint_map.md](file:///C:/QiLabs/_QiOS_DNA/00_QiEOS/60_assets/diagrams/blueprint_map.md)`
  * `[qilabs_structure_check.md](file:///C:/QiLabs/_QiOS_DNA/00_QiEOS/90_receipts/50_generated_reports/qilabs_structure_check.md)`
  * `[wiki_publish_plan.md](file:///C:/QiLabs/_QiOS_DNA/60_QiApps/qiaccess_start/wiki_publish_plan.md)`
  * `[QiIngest_Pipeline.md](file:///C:/QiLabs/_QiOS_DNA/70_QiConnect/06_workflows/QiIngest_Pipeline.md)`
  * `[ADR-0013_folder_documentation_model.md](file:///C:/QiLabs/_QiOS_DNA/decisions/ADR-0013_folder_documentation_model.md)`
  * `[2026-06-10_qidna_implementation_reconciliation.md](file:///C:/QiLabs/_QiOS_DNA/Reconciliation/2026-06-10_qidna_implementation_reconciliation.md)`

### File: `_index.md`
- **Current Path**: `00_QiEOS/10_governance/20_rules/_index.md`
- **Proposed Move**: `00_QiEOS/_index.md`
- **Referenced in**:
  * `[_index.md](file:///C:/QiLabs/_QiOS_DNA/00_QiEOS/_index.md)`
  * `[_index.md](file:///C:/QiLabs/_QiOS_DNA/00_QiEOS/10_governance/_index.md)`
  * `[blueprint_map.md](file:///C:/QiLabs/_QiOS_DNA/00_QiEOS/60_assets/diagrams/blueprint_map.md)`
  * `[qilabs_structure_check.md](file:///C:/QiLabs/_QiOS_DNA/00_QiEOS/90_receipts/50_generated_reports/qilabs_structure_check.md)`
  * `[wiki_publish_plan.md](file:///C:/QiLabs/_QiOS_DNA/60_QiApps/qiaccess_start/wiki_publish_plan.md)`
  * `[QiIngest_Pipeline.md](file:///C:/QiLabs/_QiOS_DNA/70_QiConnect/06_workflows/QiIngest_Pipeline.md)`
  * `[ADR-0013_folder_documentation_model.md](file:///C:/QiLabs/_QiOS_DNA/decisions/ADR-0013_folder_documentation_model.md)`
  * `[2026-06-10_qidna_implementation_reconciliation.md](file:///C:/QiLabs/_QiOS_DNA/Reconciliation/2026-06-10_qidna_implementation_reconciliation.md)`

### File: `_index.md`
- **Current Path**: `00_QiEOS/10_governance/30_standards/_index.md`
- **Proposed Move**: `00_QiEOS/_index.md`
- **Referenced in**:
  * `[_index.md](file:///C:/QiLabs/_QiOS_DNA/00_QiEOS/_index.md)`
  * `[_index.md](file:///C:/QiLabs/_QiOS_DNA/00_QiEOS/10_governance/_index.md)`
  * `[blueprint_map.md](file:///C:/QiLabs/_QiOS_DNA/00_QiEOS/60_assets/diagrams/blueprint_map.md)`
  * `[qilabs_structure_check.md](file:///C:/QiLabs/_QiOS_DNA/00_QiEOS/90_receipts/50_generated_reports/qilabs_structure_check.md)`
  * `[wiki_publish_plan.md](file:///C:/QiLabs/_QiOS_DNA/60_QiApps/qiaccess_start/wiki_publish_plan.md)`
  * `[QiIngest_Pipeline.md](file:///C:/QiLabs/_QiOS_DNA/70_QiConnect/06_workflows/QiIngest_Pipeline.md)`
  * `[ADR-0013_folder_documentation_model.md](file:///C:/QiLabs/_QiOS_DNA/decisions/ADR-0013_folder_documentation_model.md)`
  * `[2026-06-10_qidna_implementation_reconciliation.md](file:///C:/QiLabs/_QiOS_DNA/Reconciliation/2026-06-10_qidna_implementation_reconciliation.md)`

### File: `content_metadata_profile.yaml`
- **Current Path**: `00_QiEOS/10_governance/30_standards/content_metadata_profile.yaml`
- **Proposed Move**: `00_QiEOS/content_metadata_profile.yaml`
- **Referenced in**:
  * `[ADR-0007_unified_front_matter_and_progressive_doc_topology.md](file:///C:/QiLabs/_QiOS_DNA/00_QiEOS/10_governance/50_decisions/ADR-0007_unified_front_matter_and_progressive_doc_topology.md)`
  * `[100_metadata.md](file:///C:/QiLabs/_QiOS_DNA/00_QiEOS/10_governance/60_registry/100_metadata.md)`
  * `[110_front_matter.md](file:///C:/QiLabs/_QiOS_DNA/00_QiEOS/10_governance/60_registry/110_front_matter.md)`
  * `[50_legacy_salvage.md](file:///C:/QiLabs/_QiOS_DNA/00_QiEOS/50_knowledge/50_legacy_salvage.md)`
  * `[blueprint_map.md](file:///C:/QiLabs/_QiOS_DNA/00_QiEOS/60_assets/diagrams/blueprint_map.md)`

### File: `metadata_rules.yaml`
- **Current Path**: `00_QiEOS/10_governance/30_standards/metadata_rules.yaml`
- **Proposed Move**: `00_QiEOS/metadata_rules.yaml`
- **Referenced in**:
  * `[ADR-0007_unified_front_matter_and_progressive_doc_topology.md](file:///C:/QiLabs/_QiOS_DNA/00_QiEOS/10_governance/50_decisions/ADR-0007_unified_front_matter_and_progressive_doc_topology.md)`
  * `[60_directory_tree.md](file:///C:/QiLabs/_QiOS_DNA/00_QiEOS/10_governance/60_registry/60_directory_tree.md)`
  * `[2026-05-18_qios_namespace_registry_merged_v2.md](file:///C:/QiLabs/_QiOS_DNA/00_QiEOS/10_governance/60_registry/namespace_registry/2026-05-18_qios_namespace_registry_merged_v2.md)`
  * `[blueprint_map.md](file:///C:/QiLabs/_QiOS_DNA/00_QiEOS/60_assets/diagrams/blueprint_map.md)`

### File: `naming_rules.yaml`
- **Current Path**: `00_QiEOS/10_governance/30_standards/naming_rules.yaml`
- **Proposed Move**: `00_QiEOS/naming_rules.yaml`
- **Referenced in**:
  * `[60_directory_tree.md](file:///C:/QiLabs/_QiOS_DNA/00_QiEOS/10_governance/60_registry/60_directory_tree.md)`
  * `[2026-05-18_qios_namespace_registry_merged_v2.md](file:///C:/QiLabs/_QiOS_DNA/00_QiEOS/10_governance/60_registry/namespace_registry/2026-05-18_qios_namespace_registry_merged_v2.md)`
  * `[blueprint_map.md](file:///C:/QiLabs/_QiOS_DNA/00_QiEOS/60_assets/diagrams/blueprint_map.md)`

### File: `pdf_standards.yaml`
- **Current Path**: `00_QiEOS/10_governance/30_standards/pdf_standards.yaml`
- **Proposed Move**: `00_QiEOS/pdf_standards.yaml`
- **Referenced in**:
  * `[blueprint_map.md](file:///C:/QiLabs/_QiOS_DNA/00_QiEOS/60_assets/diagrams/blueprint_map.md)`

### File: `repo_rules.yaml`
- **Current Path**: `00_QiEOS/10_governance/30_standards/repo_rules.yaml`
- **Proposed Move**: `00_QiEOS/repo_rules.yaml`
- **Referenced in**:
  * `[60_directory_tree.md](file:///C:/QiLabs/_QiOS_DNA/00_QiEOS/10_governance/60_registry/60_directory_tree.md)`
  * `[blueprint_map.md](file:///C:/QiLabs/_QiOS_DNA/00_QiEOS/60_assets/diagrams/blueprint_map.md)`

### File: `_index.md`
- **Current Path**: `00_QiEOS/10_governance/40_policies/_index.md`
- **Proposed Move**: `00_QiEOS/_index.md`
- **Referenced in**:
  * `[_index.md](file:///C:/QiLabs/_QiOS_DNA/00_QiEOS/_index.md)`
  * `[_index.md](file:///C:/QiLabs/_QiOS_DNA/00_QiEOS/10_governance/_index.md)`
  * `[blueprint_map.md](file:///C:/QiLabs/_QiOS_DNA/00_QiEOS/60_assets/diagrams/blueprint_map.md)`
  * `[qilabs_structure_check.md](file:///C:/QiLabs/_QiOS_DNA/00_QiEOS/90_receipts/50_generated_reports/qilabs_structure_check.md)`
  * `[wiki_publish_plan.md](file:///C:/QiLabs/_QiOS_DNA/60_QiApps/qiaccess_start/wiki_publish_plan.md)`
  * `[QiIngest_Pipeline.md](file:///C:/QiLabs/_QiOS_DNA/70_QiConnect/06_workflows/QiIngest_Pipeline.md)`
  * `[ADR-0013_folder_documentation_model.md](file:///C:/QiLabs/_QiOS_DNA/decisions/ADR-0013_folder_documentation_model.md)`
  * `[2026-06-10_qidna_implementation_reconciliation.md](file:///C:/QiLabs/_QiOS_DNA/Reconciliation/2026-06-10_qidna_implementation_reconciliation.md)`

### File: `agent_governance_policy.md`
- **Current Path**: `00_QiEOS/10_governance/40_policies/agents/agent_governance_policy.md`
- **Proposed Move**: `00_QiEOS/agent_governance_policy.md`
- **Referenced in**:
  * `[_index.md](file:///C:/QiLabs/_QiOS_DNA/00_QiEOS/10_governance/40_policies/_index.md)`

### File: `active_runtime_policy.md`
- **Current Path**: `00_QiEOS/10_governance/40_policies/architecture/active_runtime_policy.md`
- **Proposed Move**: `00_QiEOS/active_runtime_policy.md`
- **Referenced in**:
  * `[_index.md](file:///C:/QiLabs/_QiOS_DNA/00_QiEOS/10_governance/40_policies/_index.md)`

### File: `placement_policy.md`
- **Current Path**: `00_QiEOS/10_governance/40_policies/architecture/placement_policy.md`
- **Proposed Move**: `00_QiEOS/placement_policy.md`
- **Referenced in**:
  * `[_index.md](file:///C:/QiLabs/_QiOS_DNA/00_QiEOS/10_governance/40_policies/_index.md)`

### File: `registry_policy.md`
- **Current Path**: `00_QiEOS/10_governance/40_policies/architecture/registry_policy.md`
- **Proposed Move**: `00_QiEOS/registry_policy.md`
- **Referenced in**:
  * `[_index.md](file:///C:/QiLabs/_QiOS_DNA/00_QiEOS/10_governance/40_policies/_index.md)`

### File: `root_navigation_policy.md`
- **Current Path**: `00_QiEOS/10_governance/40_policies/architecture/root_navigation_policy.md`
- **Proposed Move**: `00_QiEOS/root_navigation_policy.md`
- **Referenced in**:
  * `[_index.md](file:///C:/QiLabs/_QiOS_DNA/00_QiEOS/10_governance/40_policies/_index.md)`

### File: `bootstrap_policy.md`
- **Current Path**: `00_QiEOS/10_governance/40_policies/development/bootstrap_policy.md`
- **Proposed Move**: `00_QiEOS/bootstrap_policy.md`
- **Referenced in**:
  * `[_index.md](file:///C:/QiLabs/_QiOS_DNA/00_QiEOS/10_governance/40_policies/_index.md)`

### File: `contribution_policy.md`
- **Current Path**: `00_QiEOS/10_governance/40_policies/development/contribution_policy.md`
- **Proposed Move**: `00_QiEOS/contribution_policy.md`
- **Referenced in**:
  * `[_index.md](file:///C:/QiLabs/_QiOS_DNA/00_QiEOS/10_governance/40_policies/_index.md)`

### File: `merge_policy.md`
- **Current Path**: `00_QiEOS/10_governance/40_policies/development/merge_policy.md`
- **Proposed Move**: `00_QiEOS/merge_policy.md`
- **Referenced in**:
  * `[_index.md](file:///C:/QiLabs/_QiOS_DNA/00_QiEOS/10_governance/40_policies/_index.md)`

### File: `legacy_quarantine_policy.md`
- **Current Path**: `00_QiEOS/10_governance/40_policies/operations/legacy_quarantine_policy.md`
- **Proposed Move**: `00_QiEOS/legacy_quarantine_policy.md`
- **Referenced in**:
  * `[_index.md](file:///C:/QiLabs/_QiOS_DNA/00_QiEOS/10_governance/40_policies/_index.md)`

### File: `lifecycle_policy.md`
- **Current Path**: `00_QiEOS/10_governance/40_policies/operations/lifecycle_policy.md`
- **Proposed Move**: `00_QiEOS/lifecycle_policy.md`
- **Referenced in**:
  * `[_index.md](file:///C:/QiLabs/_QiOS_DNA/00_QiEOS/10_governance/40_policies/_index.md)`

### File: `qinexus_freeze_policy.md`
- **Current Path**: `00_QiEOS/10_governance/40_policies/operations/qinexus_freeze_policy.md`
- **Proposed Move**: `00_QiEOS/qinexus_freeze_policy.md`
- **Referenced in**:
  * `[_index.md](file:///C:/QiLabs/_QiOS_DNA/00_QiEOS/10_governance/40_policies/_index.md)`

### File: `security_data_access_policy.md`
- **Current Path**: `00_QiEOS/10_governance/40_policies/security/security_data_access_policy.md`
- **Proposed Move**: `00_QiEOS/security_data_access_policy.md`
- **Referenced in**:
  * `[_index.md](file:///C:/QiLabs/_QiOS_DNA/00_QiEOS/10_governance/40_policies/_index.md)`

### File: `ADR-0000_template.md`
- **Current Path**: `00_QiEOS/10_governance/50_decisions/ADR-0000_template.md`
- **Proposed Move**: `00_QiEOS/ADR-0000_template.md`
- **Referenced in**:
  * `[file-index.json](file:///C:/QiLabs/_QiOS_DNA/00_QiEOS/file-index.json)`
  * `[_index.md](file:///C:/QiLabs/_QiOS_DNA/00_QiEOS/10_governance/50_decisions/_index.md)`
  * `[blueprint_map.md](file:///C:/QiLabs/_QiOS_DNA/00_QiEOS/60_assets/diagrams/blueprint_map.md)`

### File: `ADR-0001_blueprint_scope.md`
- **Current Path**: `00_QiEOS/10_governance/50_decisions/ADR-0001_blueprint_scope.md`
- **Proposed Move**: `00_QiEOS/ADR-0001_blueprint_scope.md`
- **Referenced in**:
  * `[file-index.json](file:///C:/QiLabs/_QiOS_DNA/00_QiEOS/file-index.json)`
  * `[_index.md](file:///C:/QiLabs/_QiOS_DNA/00_QiEOS/10_governance/50_decisions/_index.md)`
  * `[blueprint_map.md](file:///C:/QiLabs/_QiOS_DNA/00_QiEOS/60_assets/diagrams/blueprint_map.md)`

### File: `ADR-0002_single_domain_rule.md`
- **Current Path**: `00_QiEOS/10_governance/50_decisions/ADR-0002_single_domain_rule.md`
- **Proposed Move**: `00_QiEOS/ADR-0002_single_domain_rule.md`
- **Referenced in**:
  * `[file-index.json](file:///C:/QiLabs/_QiOS_DNA/00_QiEOS/file-index.json)`
  * `[_index.md](file:///C:/QiLabs/_QiOS_DNA/00_QiEOS/10_governance/50_decisions/_index.md)`
  * `[blueprint_map.md](file:///C:/QiLabs/_QiOS_DNA/00_QiEOS/60_assets/diagrams/blueprint_map.md)`

### File: `ADR-0003_band_model.md`
- **Current Path**: `00_QiEOS/10_governance/50_decisions/ADR-0003_band_model.md`
- **Proposed Move**: `00_QiEOS/ADR-0003_band_model.md`
- **Referenced in**:
  * `[file-index.json](file:///C:/QiLabs/_QiOS_DNA/00_QiEOS/file-index.json)`
  * `[_index.md](file:///C:/QiLabs/_QiOS_DNA/00_QiEOS/10_governance/50_decisions/_index.md)`
  * `[blueprint_map.md](file:///C:/QiLabs/_QiOS_DNA/00_QiEOS/60_assets/diagrams/blueprint_map.md)`

### File: `ADR-0004_single_account_modular_mode.md`
- **Current Path**: `00_QiEOS/10_governance/50_decisions/ADR-0004_single_account_modular_mode.md`
- **Proposed Move**: `00_QiEOS/ADR-0004_single_account_modular_mode.md`
- **Referenced in**:
  * `[file-index.json](file:///C:/QiLabs/_QiOS_DNA/00_QiEOS/file-index.json)`
  * `[_index.md](file:///C:/QiLabs/_QiOS_DNA/00_QiEOS/10_governance/50_decisions/_index.md)`
  * `[blueprint_map.md](file:///C:/QiLabs/_QiOS_DNA/00_QiEOS/60_assets/diagrams/blueprint_map.md)`

### File: `ADR-0005_fleet_orchestration.md`
- **Current Path**: `00_QiEOS/10_governance/50_decisions/ADR-0005_fleet_orchestration.md`
- **Proposed Move**: `00_QiEOS/ADR-0005_fleet_orchestration.md`
- **Referenced in**:
  * `[file-index.json](file:///C:/QiLabs/_QiOS_DNA/00_QiEOS/file-index.json)`
  * `[_index.md](file:///C:/QiLabs/_QiOS_DNA/00_QiEOS/10_governance/50_decisions/_index.md)`
  * `[blueprint_map.md](file:///C:/QiLabs/_QiOS_DNA/00_QiEOS/60_assets/diagrams/blueprint_map.md)`

### File: `ADR-0006_narrative_and_knowledge_consolidation.md`
- **Current Path**: `00_QiEOS/10_governance/50_decisions/ADR-0006_narrative_and_knowledge_consolidation.md`
- **Proposed Move**: `00_QiEOS/ADR-0006_narrative_and_knowledge_consolidation.md`
- **Referenced in**:
  * `[file-index.json](file:///C:/QiLabs/_QiOS_DNA/00_QiEOS/file-index.json)`
  * `[_index.md](file:///C:/QiLabs/_QiOS_DNA/00_QiEOS/10_governance/50_decisions/_index.md)`
  * `[blueprint_map.md](file:///C:/QiLabs/_QiOS_DNA/00_QiEOS/60_assets/diagrams/blueprint_map.md)`

### File: `ADR-0007_unified_front_matter_and_progressive_doc_topology.md`
- **Current Path**: `00_QiEOS/10_governance/50_decisions/ADR-0007_unified_front_matter_and_progressive_doc_topology.md`
- **Proposed Move**: `00_QiEOS/ADR-0007_unified_front_matter_and_progressive_doc_topology.md`
- **Referenced in**:
  * `[file-index.json](file:///C:/QiLabs/_QiOS_DNA/00_QiEOS/file-index.json)`
  * `[_index.md](file:///C:/QiLabs/_QiOS_DNA/00_QiEOS/10_governance/50_decisions/_index.md)`
  * `[blueprint_map.md](file:///C:/QiLabs/_QiOS_DNA/00_QiEOS/60_assets/diagrams/blueprint_map.md)`

### File: `ADR-0008_qilabs_root.md`
- **Current Path**: `00_QiEOS/10_governance/50_decisions/ADR-0008_qilabs_root.md`
- **Proposed Move**: `00_QiEOS/ADR-0008_qilabs_root.md`
- **Referenced in**:
  * `[file-index.json](file:///C:/QiLabs/_QiOS_DNA/00_QiEOS/file-index.json)`
  * `[_index.md](file:///C:/QiLabs/_QiOS_DNA/00_QiEOS/10_governance/50_decisions/_index.md)`
  * `[blueprint_map.md](file:///C:/QiLabs/_QiOS_DNA/00_QiEOS/60_assets/diagrams/blueprint_map.md)`

### File: `ADR-0009_backup_server_control_plane_and_public_edge_pattern.md`
- **Current Path**: `00_QiEOS/10_governance/50_decisions/ADR-0009_backup_server_control_plane_and_public_edge_pattern.md`
- **Proposed Move**: `00_QiEOS/ADR-0009_backup_server_control_plane_and_public_edge_pattern.md`
- **Referenced in**:
  * `[_index.md](file:///C:/QiLabs/_QiOS_DNA/00_QiEOS/10_governance/50_decisions/_index.md)`
  * `[blueprint_map.md](file:///C:/QiLabs/_QiOS_DNA/00_QiEOS/60_assets/diagrams/blueprint_map.md)`

### File: `ADR-0010_qios_namespace_as_routing_metadata_layer.md`
- **Current Path**: `00_QiEOS/10_governance/50_decisions/ADR-0010_qios_namespace_as_routing_metadata_layer.md`
- **Proposed Move**: `00_QiEOS/ADR-0010_qios_namespace_as_routing_metadata_layer.md`
- **Referenced in**:
  * `[2026-05-18_qios_namespace_registry_merged_v2.md](file:///C:/QiLabs/_QiOS_DNA/00_QiEOS/10_governance/60_registry/namespace_registry/2026-05-18_qios_namespace_registry_merged_v2.md)`

### File: `_index.md`
- **Current Path**: `00_QiEOS/10_governance/50_decisions/_index.md`
- **Proposed Move**: `00_QiEOS/_index.md`
- **Referenced in**:
  * `[_index.md](file:///C:/QiLabs/_QiOS_DNA/00_QiEOS/_index.md)`
  * `[_index.md](file:///C:/QiLabs/_QiOS_DNA/00_QiEOS/10_governance/_index.md)`
  * `[blueprint_map.md](file:///C:/QiLabs/_QiOS_DNA/00_QiEOS/60_assets/diagrams/blueprint_map.md)`
  * `[qilabs_structure_check.md](file:///C:/QiLabs/_QiOS_DNA/00_QiEOS/90_receipts/50_generated_reports/qilabs_structure_check.md)`
  * `[wiki_publish_plan.md](file:///C:/QiLabs/_QiOS_DNA/60_QiApps/qiaccess_start/wiki_publish_plan.md)`
  * `[QiIngest_Pipeline.md](file:///C:/QiLabs/_QiOS_DNA/70_QiConnect/06_workflows/QiIngest_Pipeline.md)`
  * `[ADR-0013_folder_documentation_model.md](file:///C:/QiLabs/_QiOS_DNA/decisions/ADR-0013_folder_documentation_model.md)`
  * `[2026-06-10_qidna_implementation_reconciliation.md](file:///C:/QiLabs/_QiOS_DNA/Reconciliation/2026-06-10_qidna_implementation_reconciliation.md)`

### File: `100_metadata.md`
- **Current Path**: `00_QiEOS/10_governance/60_registry/100_metadata.md`
- **Proposed Move**: `00_QiEOS/100_metadata.md`
- **Referenced in**:
  * `[2026-05-18_qios_namespace_registry_merged_v2.md](file:///C:/QiLabs/_QiOS_DNA/00_QiEOS/10_governance/60_registry/namespace_registry/2026-05-18_qios_namespace_registry_merged_v2.md)`

### File: `110_front_matter.md`
- **Current Path**: `00_QiEOS/10_governance/60_registry/110_front_matter.md`
- **Proposed Move**: `00_QiEOS/110_front_matter.md`
- **Referenced in**:
  * `[ADR-0010_qios_namespace_as_routing_metadata_layer.md](file:///C:/QiLabs/_QiOS_DNA/00_QiEOS/10_governance/50_decisions/ADR-0010_qios_namespace_as_routing_metadata_layer.md)`
  * `[2026-05-18_qios_namespace_registry_merged_v2.md](file:///C:/QiLabs/_QiOS_DNA/00_QiEOS/10_governance/60_registry/namespace_registry/2026-05-18_qios_namespace_registry_merged_v2.md)`

### File: `130_placement_rules.md`
- **Current Path**: `00_QiEOS/10_governance/60_registry/130_placement_rules.md`
- **Proposed Move**: `00_QiEOS/130_placement_rules.md`
- **Referenced in**:
  * `[2026-05-18_qios_namespace_registry_merged_v2.md](file:///C:/QiLabs/_QiOS_DNA/00_QiEOS/10_governance/60_registry/namespace_registry/2026-05-18_qios_namespace_registry_merged_v2.md)`

### File: `20_bands.md`
- **Current Path**: `00_QiEOS/10_governance/60_registry/20_bands.md`
- **Proposed Move**: `00_QiEOS/20_bands.md`
- **Referenced in**:
  * `[2026-05-18_qios_namespace_registry_merged_v2.md](file:///C:/QiLabs/_QiOS_DNA/00_QiEOS/10_governance/60_registry/namespace_registry/2026-05-18_qios_namespace_registry_merged_v2.md)`

### File: `30_domains.md`
- **Current Path**: `00_QiEOS/10_governance/60_registry/30_domains.md`
- **Proposed Move**: `00_QiEOS/30_domains.md`
- **Referenced in**:
  * `[2026-05-18_qios_namespace_registry_merged_v2.md](file:///C:/QiLabs/_QiOS_DNA/00_QiEOS/10_governance/60_registry/namespace_registry/2026-05-18_qios_namespace_registry_merged_v2.md)`

### File: `40_subdomains.md`
- **Current Path**: `00_QiEOS/10_governance/60_registry/40_subdomains.md`
- **Proposed Move**: `00_QiEOS/40_subdomains.md`
- **Referenced in**:
  * `[2026-05-18_qios_namespace_registry_merged_v2.md](file:///C:/QiLabs/_QiOS_DNA/00_QiEOS/10_governance/60_registry/namespace_registry/2026-05-18_qios_namespace_registry_merged_v2.md)`

### File: `70_object_model.md`
- **Current Path**: `00_QiEOS/10_governance/60_registry/70_object_model.md`
- **Proposed Move**: `00_QiEOS/70_object_model.md`
- **Referenced in**:
  * `[ADR-0010_qios_namespace_as_routing_metadata_layer.md](file:///C:/QiLabs/_QiOS_DNA/00_QiEOS/10_governance/50_decisions/ADR-0010_qios_namespace_as_routing_metadata_layer.md)`
  * `[2026-05-18_qios_namespace_registry_merged_v2.md](file:///C:/QiLabs/_QiOS_DNA/00_QiEOS/10_governance/60_registry/namespace_registry/2026-05-18_qios_namespace_registry_merged_v2.md)`

### File: `_index.md`
- **Current Path**: `00_QiEOS/10_governance/60_registry/_index.md`
- **Proposed Move**: `00_QiEOS/_index.md`
- **Referenced in**:
  * `[_index.md](file:///C:/QiLabs/_QiOS_DNA/00_QiEOS/_index.md)`
  * `[_index.md](file:///C:/QiLabs/_QiOS_DNA/00_QiEOS/10_governance/_index.md)`
  * `[blueprint_map.md](file:///C:/QiLabs/_QiOS_DNA/00_QiEOS/60_assets/diagrams/blueprint_map.md)`
  * `[qilabs_structure_check.md](file:///C:/QiLabs/_QiOS_DNA/00_QiEOS/90_receipts/50_generated_reports/qilabs_structure_check.md)`
  * `[wiki_publish_plan.md](file:///C:/QiLabs/_QiOS_DNA/60_QiApps/qiaccess_start/wiki_publish_plan.md)`
  * `[QiIngest_Pipeline.md](file:///C:/QiLabs/_QiOS_DNA/70_QiConnect/06_workflows/QiIngest_Pipeline.md)`
  * `[ADR-0013_folder_documentation_model.md](file:///C:/QiLabs/_QiOS_DNA/decisions/ADR-0013_folder_documentation_model.md)`
  * `[2026-06-10_qidna_implementation_reconciliation.md](file:///C:/QiLabs/_QiOS_DNA/Reconciliation/2026-06-10_qidna_implementation_reconciliation.md)`

### File: `band_registry.yaml`
- **Current Path**: `00_QiEOS/10_governance/60_registry/band_registry.yaml`
- **Proposed Move**: `00_QiEOS/band_registry.yaml`
- **Referenced in**:
  * `[ADR-0003_band_model.md](file:///C:/QiLabs/_QiOS_DNA/00_QiEOS/10_governance/50_decisions/ADR-0003_band_model.md)`
  * `[ADR-0010_qios_namespace_as_routing_metadata_layer.md](file:///C:/QiLabs/_QiOS_DNA/00_QiEOS/10_governance/50_decisions/ADR-0010_qios_namespace_as_routing_metadata_layer.md)`
  * `[20_bands.md](file:///C:/QiLabs/_QiOS_DNA/00_QiEOS/10_governance/60_registry/20_bands.md)`
  * `[2026-05-18_qios_namespace_registry_merged_v2.md](file:///C:/QiLabs/_QiOS_DNA/00_QiEOS/10_governance/60_registry/namespace_registry/2026-05-18_qios_namespace_registry_merged_v2.md)`
  * `[blueprint_map.md](file:///C:/QiLabs/_QiOS_DNA/00_QiEOS/60_assets/diagrams/blueprint_map.md)`

### File: `deprecation_registry.yaml`
- **Current Path**: `00_QiEOS/10_governance/60_registry/deprecation_registry.yaml`
- **Proposed Move**: `00_QiEOS/deprecation_registry.yaml`
- **Referenced in**:
  * `[blueprint_map.md](file:///C:/QiLabs/_QiOS_DNA/00_QiEOS/60_assets/diagrams/blueprint_map.md)`

### File: `domain_registry.yaml`
- **Current Path**: `00_QiEOS/10_governance/60_registry/domain_registry.yaml`
- **Proposed Move**: `00_QiEOS/domain_registry.yaml`
- **Referenced in**:
  * `[ADR-0002_single_domain_rule.md](file:///C:/QiLabs/_QiOS_DNA/00_QiEOS/10_governance/50_decisions/ADR-0002_single_domain_rule.md)`
  * `[40_subdomains.md](file:///C:/QiLabs/_QiOS_DNA/00_QiEOS/10_governance/60_registry/40_subdomains.md)`
  * `[blueprint_map.md](file:///C:/QiLabs/_QiOS_DNA/00_QiEOS/60_assets/diagrams/blueprint_map.md)`

### File: `folder_registry.yaml`
- **Current Path**: `00_QiEOS/10_governance/60_registry/folder_registry.yaml`
- **Proposed Move**: `00_QiEOS/folder_registry.yaml`
- **Referenced in**:
  * `[blueprint_map.md](file:///C:/QiLabs/_QiOS_DNA/00_QiEOS/60_assets/diagrams/blueprint_map.md)`

### File: `infrastructure_registry.yaml`
- **Current Path**: `00_QiEOS/10_governance/60_registry/infrastructure_registry.yaml`
- **Proposed Move**: `00_QiEOS/infrastructure_registry.yaml`
- **Referenced in**:
  * `[blueprint_map.md](file:///C:/QiLabs/_QiOS_DNA/00_QiEOS/60_assets/diagrams/blueprint_map.md)`

### File: `_index.md`
- **Current Path**: `00_QiEOS/10_governance/60_registry/namespace_registry/_index.md`
- **Proposed Move**: `00_QiEOS/_index.md`
- **Referenced in**:
  * `[_index.md](file:///C:/QiLabs/_QiOS_DNA/00_QiEOS/_index.md)`
  * `[_index.md](file:///C:/QiLabs/_QiOS_DNA/00_QiEOS/10_governance/_index.md)`
  * `[blueprint_map.md](file:///C:/QiLabs/_QiOS_DNA/00_QiEOS/60_assets/diagrams/blueprint_map.md)`
  * `[qilabs_structure_check.md](file:///C:/QiLabs/_QiOS_DNA/00_QiEOS/90_receipts/50_generated_reports/qilabs_structure_check.md)`
  * `[wiki_publish_plan.md](file:///C:/QiLabs/_QiOS_DNA/60_QiApps/qiaccess_start/wiki_publish_plan.md)`
  * `[QiIngest_Pipeline.md](file:///C:/QiLabs/_QiOS_DNA/70_QiConnect/06_workflows/QiIngest_Pipeline.md)`
  * `[ADR-0013_folder_documentation_model.md](file:///C:/QiLabs/_QiOS_DNA/decisions/ADR-0013_folder_documentation_model.md)`
  * `[2026-06-10_qidna_implementation_reconciliation.md](file:///C:/QiLabs/_QiOS_DNA/Reconciliation/2026-06-10_qidna_implementation_reconciliation.md)`

### File: `realms_registry.yaml`
- **Current Path**: `00_QiEOS/10_governance/60_registry/realms_registry.yaml`
- **Proposed Move**: `00_QiEOS/realms_registry.yaml`
- **Referenced in**:
  * `[blueprint_map.md](file:///C:/QiLabs/_QiOS_DNA/00_QiEOS/60_assets/diagrams/blueprint_map.md)`

### File: `band_registry.schema.json`
- **Current Path**: `00_QiEOS/10_governance/60_registry/schemas/band_registry.schema.json`
- **Proposed Move**: `00_QiEOS/band_registry.schema.json`
- **Referenced in**:
  * `[blueprint_map.md](file:///C:/QiLabs/_QiOS_DNA/00_QiEOS/60_assets/diagrams/blueprint_map.md)`

### File: `sensitivity_classification.yaml`
- **Current Path**: `00_QiEOS/10_governance/60_registry/sensitivity_classification.yaml`
- **Proposed Move**: `00_QiEOS/sensitivity_classification.yaml`
- **Referenced in**:
  * `[100_metadata.md](file:///C:/QiLabs/_QiOS_DNA/00_QiEOS/10_governance/60_registry/100_metadata.md)`
  * `[50_legacy_salvage.md](file:///C:/QiLabs/_QiOS_DNA/00_QiEOS/50_knowledge/50_legacy_salvage.md)`
  * `[blueprint_map.md](file:///C:/QiLabs/_QiOS_DNA/00_QiEOS/60_assets/diagrams/blueprint_map.md)`

### File: `subdomain_registry.yaml`
- **Current Path**: `00_QiEOS/10_governance/60_registry/subdomain_registry.yaml`
- **Proposed Move**: `00_QiEOS/subdomain_registry.yaml`
- **Referenced in**:
  * `[40_subdomains.md](file:///C:/QiLabs/_QiOS_DNA/00_QiEOS/10_governance/60_registry/40_subdomains.md)`
  * `[blueprint_map.md](file:///C:/QiLabs/_QiOS_DNA/00_QiEOS/60_assets/diagrams/blueprint_map.md)`

### File: `workspace_realms.yaml`
- **Current Path**: `00_QiEOS/10_governance/60_registry/workspace_realms.yaml`
- **Proposed Move**: `00_QiEOS/workspace_realms.yaml`
- **Referenced in**:
  * `[100_metadata.md](file:///C:/QiLabs/_QiOS_DNA/00_QiEOS/10_governance/60_registry/100_metadata.md)`
  * `[50_legacy_salvage.md](file:///C:/QiLabs/_QiOS_DNA/00_QiEOS/50_knowledge/50_legacy_salvage.md)`
  * `[blueprint_map.md](file:///C:/QiLabs/_QiOS_DNA/00_QiEOS/60_assets/diagrams/blueprint_map.md)`

### File: `_index.md`
- **Current Path**: `00_QiEOS/10_governance/_index.md`
- **Proposed Move**: `00_QiEOS/_index.md`
- **Referenced in**:
  * `[_index.md](file:///C:/QiLabs/_QiOS_DNA/00_QiEOS/_index.md)`
  * `[blueprint_map.md](file:///C:/QiLabs/_QiOS_DNA/00_QiEOS/60_assets/diagrams/blueprint_map.md)`
  * `[qilabs_structure_check.md](file:///C:/QiLabs/_QiOS_DNA/00_QiEOS/90_receipts/50_generated_reports/qilabs_structure_check.md)`
  * `[wiki_publish_plan.md](file:///C:/QiLabs/_QiOS_DNA/60_QiApps/qiaccess_start/wiki_publish_plan.md)`
  * `[QiIngest_Pipeline.md](file:///C:/QiLabs/_QiOS_DNA/70_QiConnect/06_workflows/QiIngest_Pipeline.md)`
  * `[ADR-0013_folder_documentation_model.md](file:///C:/QiLabs/_QiOS_DNA/decisions/ADR-0013_folder_documentation_model.md)`
  * `[2026-06-10_qidna_implementation_reconciliation.md](file:///C:/QiLabs/_QiOS_DNA/Reconciliation/2026-06-10_qidna_implementation_reconciliation.md)`

### File: `10_identity.md`
- **Current Path**: `00_QiEOS/20_structure/10_identity.md`
- **Proposed Move**: `00_QiEOS/10_identity.md`
- **Referenced in**:
  * `[file-index.json](file:///C:/QiLabs/_QiOS_DNA/00_QiEOS/file-index.json)`
  * `[_index.md](file:///C:/QiLabs/_QiOS_DNA/00_QiEOS/20_structure/_index.md)`

### File: `20_system_model.md`
- **Current Path**: `00_QiEOS/20_structure/20_system_model.md`
- **Proposed Move**: `00_QiEOS/20_system_model.md`
- **Referenced in**:
  * `[_index.md](file:///C:/QiLabs/_QiOS_DNA/00_QiEOS/20_structure/_index.md)`

### File: `30_component_map.md`
- **Current Path**: `00_QiEOS/20_structure/30_component_map.md`
- **Proposed Move**: `00_QiEOS/30_component_map.md`
- **Referenced in**:
  * `[_index.md](file:///C:/QiLabs/_QiOS_DNA/00_QiEOS/20_structure/_index.md)`

### File: `40_service_boundaries.md`
- **Current Path**: `00_QiEOS/20_structure/40_service_boundaries.md`
- **Proposed Move**: `00_QiEOS/40_service_boundaries.md`
- **Referenced in**:
  * `[_index.md](file:///C:/QiLabs/_QiOS_DNA/00_QiEOS/20_structure/_index.md)`

### File: `50_data_flow.md`
- **Current Path**: `00_QiEOS/20_structure/50_data_flow.md`
- **Proposed Move**: `00_QiEOS/50_data_flow.md`
- **Referenced in**:
  * `[_index.md](file:///C:/QiLabs/_QiOS_DNA/00_QiEOS/20_structure/_index.md)`

### File: `60_device_model.md`
- **Current Path**: `00_QiEOS/20_structure/60_device_model.md`
- **Proposed Move**: `00_QiEOS/60_device_model.md`
- **Referenced in**:
  * `[_index.md](file:///C:/QiLabs/_QiOS_DNA/00_QiEOS/20_structure/_index.md)`

### File: `70_runtime_zones.md`
- **Current Path**: `00_QiEOS/20_structure/70_runtime_zones.md`
- **Proposed Move**: `00_QiEOS/70_runtime_zones.md`
- **Referenced in**:
  * `[_index.md](file:///C:/QiLabs/_QiOS_DNA/00_QiEOS/20_structure/_index.md)`

### File: `_index.md`
- **Current Path**: `00_QiEOS/20_structure/_index.md`
- **Proposed Move**: `00_QiEOS/_index.md`
- **Referenced in**:
  * `[_index.md](file:///C:/QiLabs/_QiOS_DNA/00_QiEOS/_index.md)`
  * `[_index.md](file:///C:/QiLabs/_QiOS_DNA/00_QiEOS/10_governance/_index.md)`
  * `[blueprint_map.md](file:///C:/QiLabs/_QiOS_DNA/00_QiEOS/60_assets/diagrams/blueprint_map.md)`
  * `[qilabs_structure_check.md](file:///C:/QiLabs/_QiOS_DNA/00_QiEOS/90_receipts/50_generated_reports/qilabs_structure_check.md)`
  * `[wiki_publish_plan.md](file:///C:/QiLabs/_QiOS_DNA/60_QiApps/qiaccess_start/wiki_publish_plan.md)`
  * `[QiIngest_Pipeline.md](file:///C:/QiLabs/_QiOS_DNA/70_QiConnect/06_workflows/QiIngest_Pipeline.md)`
  * `[ADR-0013_folder_documentation_model.md](file:///C:/QiLabs/_QiOS_DNA/decisions/ADR-0013_folder_documentation_model.md)`
  * `[2026-06-10_qidna_implementation_reconciliation.md](file:///C:/QiLabs/_QiOS_DNA/Reconciliation/2026-06-10_qidna_implementation_reconciliation.md)`

### File: `_index.md`
- **Current Path**: `00_QiEOS/30_service_map/100_integrations/_index.md`
- **Proposed Move**: `00_QiEOS/_index.md`
- **Referenced in**:
  * `[_index.md](file:///C:/QiLabs/_QiOS_DNA/00_QiEOS/_index.md)`
  * `[_index.md](file:///C:/QiLabs/_QiOS_DNA/00_QiEOS/10_governance/_index.md)`
  * `[blueprint_map.md](file:///C:/QiLabs/_QiOS_DNA/00_QiEOS/60_assets/diagrams/blueprint_map.md)`
  * `[qilabs_structure_check.md](file:///C:/QiLabs/_QiOS_DNA/00_QiEOS/90_receipts/50_generated_reports/qilabs_structure_check.md)`
  * `[wiki_publish_plan.md](file:///C:/QiLabs/_QiOS_DNA/60_QiApps/qiaccess_start/wiki_publish_plan.md)`
  * `[QiIngest_Pipeline.md](file:///C:/QiLabs/_QiOS_DNA/70_QiConnect/06_workflows/QiIngest_Pipeline.md)`
  * `[ADR-0013_folder_documentation_model.md](file:///C:/QiLabs/_QiOS_DNA/decisions/ADR-0013_folder_documentation_model.md)`
  * `[2026-06-10_qidna_implementation_reconciliation.md](file:///C:/QiLabs/_QiOS_DNA/Reconciliation/2026-06-10_qidna_implementation_reconciliation.md)`

### File: `_index.md`
- **Current Path**: `00_QiEOS/30_service_map/10_infrastructure/_index.md`
- **Proposed Move**: `30_QiServer/_index.md`
- **Referenced in**:
  * `[_index.md](file:///C:/QiLabs/_QiOS_DNA/00_QiEOS/_index.md)`
  * `[_index.md](file:///C:/QiLabs/_QiOS_DNA/00_QiEOS/10_governance/_index.md)`
  * `[blueprint_map.md](file:///C:/QiLabs/_QiOS_DNA/00_QiEOS/60_assets/diagrams/blueprint_map.md)`
  * `[qilabs_structure_check.md](file:///C:/QiLabs/_QiOS_DNA/00_QiEOS/90_receipts/50_generated_reports/qilabs_structure_check.md)`
  * `[wiki_publish_plan.md](file:///C:/QiLabs/_QiOS_DNA/60_QiApps/qiaccess_start/wiki_publish_plan.md)`
  * `[QiIngest_Pipeline.md](file:///C:/QiLabs/_QiOS_DNA/70_QiConnect/06_workflows/QiIngest_Pipeline.md)`
  * `[ADR-0013_folder_documentation_model.md](file:///C:/QiLabs/_QiOS_DNA/decisions/ADR-0013_folder_documentation_model.md)`
  * `[2026-06-10_qidna_implementation_reconciliation.md](file:///C:/QiLabs/_QiOS_DNA/Reconciliation/2026-06-10_qidna_implementation_reconciliation.md)`

### File: `_index.md`
- **Current Path**: `00_QiEOS/30_service_map/10_infrastructure/cockpit/_index.md`
- **Proposed Move**: `30_QiServer/_index.md`
- **Referenced in**:
  * `[_index.md](file:///C:/QiLabs/_QiOS_DNA/00_QiEOS/_index.md)`
  * `[_index.md](file:///C:/QiLabs/_QiOS_DNA/00_QiEOS/10_governance/_index.md)`
  * `[blueprint_map.md](file:///C:/QiLabs/_QiOS_DNA/00_QiEOS/60_assets/diagrams/blueprint_map.md)`
  * `[qilabs_structure_check.md](file:///C:/QiLabs/_QiOS_DNA/00_QiEOS/90_receipts/50_generated_reports/qilabs_structure_check.md)`
  * `[wiki_publish_plan.md](file:///C:/QiLabs/_QiOS_DNA/60_QiApps/qiaccess_start/wiki_publish_plan.md)`
  * `[QiIngest_Pipeline.md](file:///C:/QiLabs/_QiOS_DNA/70_QiConnect/06_workflows/QiIngest_Pipeline.md)`
  * `[ADR-0013_folder_documentation_model.md](file:///C:/QiLabs/_QiOS_DNA/decisions/ADR-0013_folder_documentation_model.md)`
  * `[2026-06-10_qidna_implementation_reconciliation.md](file:///C:/QiLabs/_QiOS_DNA/Reconciliation/2026-06-10_qidna_implementation_reconciliation.md)`

### File: `_index.md`
- **Current Path**: `00_QiEOS/30_service_map/110_qiserver/_index.md`
- **Proposed Move**: `30_QiServer/_index.md`
- **Referenced in**:
  * `[_index.md](file:///C:/QiLabs/_QiOS_DNA/00_QiEOS/_index.md)`
  * `[_index.md](file:///C:/QiLabs/_QiOS_DNA/00_QiEOS/10_governance/_index.md)`
  * `[blueprint_map.md](file:///C:/QiLabs/_QiOS_DNA/00_QiEOS/60_assets/diagrams/blueprint_map.md)`
  * `[qilabs_structure_check.md](file:///C:/QiLabs/_QiOS_DNA/00_QiEOS/90_receipts/50_generated_reports/qilabs_structure_check.md)`
  * `[wiki_publish_plan.md](file:///C:/QiLabs/_QiOS_DNA/60_QiApps/qiaccess_start/wiki_publish_plan.md)`
  * `[QiIngest_Pipeline.md](file:///C:/QiLabs/_QiOS_DNA/70_QiConnect/06_workflows/QiIngest_Pipeline.md)`
  * `[ADR-0013_folder_documentation_model.md](file:///C:/QiLabs/_QiOS_DNA/decisions/ADR-0013_folder_documentation_model.md)`
  * `[2026-06-10_qidna_implementation_reconciliation.md](file:///C:/QiLabs/_QiOS_DNA/Reconciliation/2026-06-10_qidna_implementation_reconciliation.md)`

### File: `runtime.md`
- **Current Path**: `00_QiEOS/30_service_map/110_qiserver/runtime.md`
- **Proposed Move**: `30_QiServer/runtime.md`
- **Referenced in**:
  * `[file-index.json](file:///C:/QiLabs/_QiOS_DNA/00_QiEOS/file-index.json)`
  * `[blueprint_map.md](file:///C:/QiLabs/_QiOS_DNA/00_QiEOS/60_assets/diagrams/blueprint_map.md)`

### File: `runtime_profile.md`
- **Current Path**: `00_QiEOS/30_service_map/110_qiserver/runtime_profile.md`
- **Proposed Move**: `30_QiServer/runtime_profile.md`
- **Referenced in**:
  * `[blueprint_map.md](file:///C:/QiLabs/_QiOS_DNA/00_QiEOS/60_assets/diagrams/blueprint_map.md)`

### File: `_index.md`
- **Current Path**: `00_QiEOS/30_service_map/120_applications/CareLite/_index.md`
- **Proposed Move**: `60_QiApps/_index.md`
- **Referenced in**:
  * `[_index.md](file:///C:/QiLabs/_QiOS_DNA/00_QiEOS/_index.md)`
  * `[_index.md](file:///C:/QiLabs/_QiOS_DNA/00_QiEOS/10_governance/_index.md)`
  * `[blueprint_map.md](file:///C:/QiLabs/_QiOS_DNA/00_QiEOS/60_assets/diagrams/blueprint_map.md)`
  * `[qilabs_structure_check.md](file:///C:/QiLabs/_QiOS_DNA/00_QiEOS/90_receipts/50_generated_reports/qilabs_structure_check.md)`
  * `[wiki_publish_plan.md](file:///C:/QiLabs/_QiOS_DNA/60_QiApps/qiaccess_start/wiki_publish_plan.md)`
  * `[QiIngest_Pipeline.md](file:///C:/QiLabs/_QiOS_DNA/70_QiConnect/06_workflows/QiIngest_Pipeline.md)`
  * `[ADR-0013_folder_documentation_model.md](file:///C:/QiLabs/_QiOS_DNA/decisions/ADR-0013_folder_documentation_model.md)`
  * `[2026-06-10_qidna_implementation_reconciliation.md](file:///C:/QiLabs/_QiOS_DNA/Reconciliation/2026-06-10_qidna_implementation_reconciliation.md)`

### File: `_index.md`
- **Current Path**: `00_QiEOS/30_service_map/120_applications/_index.md`
- **Proposed Move**: `60_QiApps/_index.md`
- **Referenced in**:
  * `[_index.md](file:///C:/QiLabs/_QiOS_DNA/00_QiEOS/_index.md)`
  * `[_index.md](file:///C:/QiLabs/_QiOS_DNA/00_QiEOS/10_governance/_index.md)`
  * `[blueprint_map.md](file:///C:/QiLabs/_QiOS_DNA/00_QiEOS/60_assets/diagrams/blueprint_map.md)`
  * `[qilabs_structure_check.md](file:///C:/QiLabs/_QiOS_DNA/00_QiEOS/90_receipts/50_generated_reports/qilabs_structure_check.md)`
  * `[wiki_publish_plan.md](file:///C:/QiLabs/_QiOS_DNA/60_QiApps/qiaccess_start/wiki_publish_plan.md)`
  * `[QiIngest_Pipeline.md](file:///C:/QiLabs/_QiOS_DNA/70_QiConnect/06_workflows/QiIngest_Pipeline.md)`
  * `[ADR-0013_folder_documentation_model.md](file:///C:/QiLabs/_QiOS_DNA/decisions/ADR-0013_folder_documentation_model.md)`
  * `[2026-06-10_qidna_implementation_reconciliation.md](file:///C:/QiLabs/_QiOS_DNA/Reconciliation/2026-06-10_qidna_implementation_reconciliation.md)`

### File: `admin.md`
- **Current Path**: `00_QiEOS/30_service_map/120_applications/admin.md`
- **Proposed Move**: `60_QiApps/admin.md`
- **Referenced in**:
  * `[file-index.json](file:///C:/QiLabs/_QiOS_DNA/00_QiEOS/file-index.json)`
  * `[_index.md](file:///C:/QiLabs/_QiOS_DNA/00_QiEOS/30_service_map/120_applications/_index.md)`
  * `[blueprint_map.md](file:///C:/QiLabs/_QiOS_DNA/00_QiEOS/60_assets/diagrams/blueprint_map.md)`

### File: `carelite.md`
- **Current Path**: `00_QiEOS/30_service_map/120_applications/carelite.md`
- **Proposed Move**: `60_QiApps/carelite.md`
- **Referenced in**:
  * `[roadmap.md](file:///C:/QiLabs/_QiOS_DNA/00_QiEOS/30_service_map/120_applications/roadmap.md)`
  * `[_index.md](file:///C:/QiLabs/_QiOS_DNA/00_QiEOS/30_service_map/120_applications/_index.md)`

### File: `firefly.md`
- **Current Path**: `00_QiEOS/30_service_map/120_applications/firefly.md`
- **Proposed Move**: `60_QiApps/firefly.md`
- **Referenced in**:
  * `[roadmap.md](file:///C:/QiLabs/_QiOS_DNA/00_QiEOS/30_service_map/120_applications/roadmap.md)`
  * `[_index.md](file:///C:/QiLabs/_QiOS_DNA/00_QiEOS/30_service_map/120_applications/_index.md)`

### File: `portal.md`
- **Current Path**: `00_QiEOS/30_service_map/120_applications/portal.md`
- **Proposed Move**: `60_QiApps/portal.md`
- **Referenced in**:
  * `[file-index.json](file:///C:/QiLabs/_QiOS_DNA/00_QiEOS/file-index.json)`
  * `[roadmap.md](file:///C:/QiLabs/_QiOS_DNA/00_QiEOS/30_service_map/120_applications/roadmap.md)`
  * `[_index.md](file:///C:/QiLabs/_QiOS_DNA/00_QiEOS/30_service_map/120_applications/_index.md)`
  * `[blueprint_map.md](file:///C:/QiLabs/_QiOS_DNA/00_QiEOS/60_assets/diagrams/blueprint_map.md)`

### File: `roadmap.md`
- **Current Path**: `00_QiEOS/30_service_map/120_applications/roadmap.md`
- **Proposed Move**: `60_QiApps/roadmap.md`
- **Referenced in**:
  * `[_index.md](file:///C:/QiLabs/_QiOS_DNA/00_QiEOS/30_service_map/120_applications/_index.md)`
  * `[qinote_salvage_extract.md](file:///C:/QiLabs/_QiOS_DNA/00_QiEOS/30_service_map/120_applications/qinote/qinote_salvage_extract.md)`

### File: `_index.md`
- **Current Path**: `00_QiEOS/30_service_map/130_GINA/_index.md`
- **Proposed Move**: `60_QiApps/_index.md`
- **Referenced in**:
  * `[_index.md](file:///C:/QiLabs/_QiOS_DNA/00_QiEOS/_index.md)`
  * `[_index.md](file:///C:/QiLabs/_QiOS_DNA/00_QiEOS/10_governance/_index.md)`
  * `[blueprint_map.md](file:///C:/QiLabs/_QiOS_DNA/00_QiEOS/60_assets/diagrams/blueprint_map.md)`
  * `[qilabs_structure_check.md](file:///C:/QiLabs/_QiOS_DNA/00_QiEOS/90_receipts/50_generated_reports/qilabs_structure_check.md)`
  * `[wiki_publish_plan.md](file:///C:/QiLabs/_QiOS_DNA/60_QiApps/qiaccess_start/wiki_publish_plan.md)`
  * `[QiIngest_Pipeline.md](file:///C:/QiLabs/_QiOS_DNA/70_QiConnect/06_workflows/QiIngest_Pipeline.md)`
  * `[ADR-0013_folder_documentation_model.md](file:///C:/QiLabs/_QiOS_DNA/decisions/ADR-0013_folder_documentation_model.md)`
  * `[2026-06-10_qidna_implementation_reconciliation.md](file:///C:/QiLabs/_QiOS_DNA/Reconciliation/2026-06-10_qidna_implementation_reconciliation.md)`

### File: `_index.md`
- **Current Path**: `00_QiEOS/30_service_map/20_ai_compute/_index.md`
- **Proposed Move**: `30_QiServer/_index.md`
- **Referenced in**:
  * `[_index.md](file:///C:/QiLabs/_QiOS_DNA/00_QiEOS/_index.md)`
  * `[_index.md](file:///C:/QiLabs/_QiOS_DNA/00_QiEOS/10_governance/_index.md)`
  * `[blueprint_map.md](file:///C:/QiLabs/_QiOS_DNA/00_QiEOS/60_assets/diagrams/blueprint_map.md)`
  * `[qilabs_structure_check.md](file:///C:/QiLabs/_QiOS_DNA/00_QiEOS/90_receipts/50_generated_reports/qilabs_structure_check.md)`
  * `[wiki_publish_plan.md](file:///C:/QiLabs/_QiOS_DNA/60_QiApps/qiaccess_start/wiki_publish_plan.md)`
  * `[QiIngest_Pipeline.md](file:///C:/QiLabs/_QiOS_DNA/70_QiConnect/06_workflows/QiIngest_Pipeline.md)`
  * `[ADR-0013_folder_documentation_model.md](file:///C:/QiLabs/_QiOS_DNA/decisions/ADR-0013_folder_documentation_model.md)`
  * `[2026-06-10_qidna_implementation_reconciliation.md](file:///C:/QiLabs/_QiOS_DNA/Reconciliation/2026-06-10_qidna_implementation_reconciliation.md)`

### File: `_index.md`
- **Current Path**: `00_QiEOS/30_service_map/30_capture/_index.md`
- **Proposed Move**: `40_QiCapture/_index.md`
- **Referenced in**:
  * `[_index.md](file:///C:/QiLabs/_QiOS_DNA/00_QiEOS/_index.md)`
  * `[_index.md](file:///C:/QiLabs/_QiOS_DNA/00_QiEOS/10_governance/_index.md)`
  * `[blueprint_map.md](file:///C:/QiLabs/_QiOS_DNA/00_QiEOS/60_assets/diagrams/blueprint_map.md)`
  * `[qilabs_structure_check.md](file:///C:/QiLabs/_QiOS_DNA/00_QiEOS/90_receipts/50_generated_reports/qilabs_structure_check.md)`
  * `[wiki_publish_plan.md](file:///C:/QiLabs/_QiOS_DNA/60_QiApps/qiaccess_start/wiki_publish_plan.md)`
  * `[QiIngest_Pipeline.md](file:///C:/QiLabs/_QiOS_DNA/70_QiConnect/06_workflows/QiIngest_Pipeline.md)`
  * `[ADR-0013_folder_documentation_model.md](file:///C:/QiLabs/_QiOS_DNA/decisions/ADR-0013_folder_documentation_model.md)`
  * `[2026-06-10_qidna_implementation_reconciliation.md](file:///C:/QiLabs/_QiOS_DNA/Reconciliation/2026-06-10_qidna_implementation_reconciliation.md)`

### File: `_index.md`
- **Current Path**: `00_QiEOS/30_service_map/30_capture/paperless/_index.md`
- **Proposed Move**: `40_QiCapture/_index.md`
- **Referenced in**:
  * `[_index.md](file:///C:/QiLabs/_QiOS_DNA/00_QiEOS/_index.md)`
  * `[_index.md](file:///C:/QiLabs/_QiOS_DNA/00_QiEOS/10_governance/_index.md)`
  * `[blueprint_map.md](file:///C:/QiLabs/_QiOS_DNA/00_QiEOS/60_assets/diagrams/blueprint_map.md)`
  * `[qilabs_structure_check.md](file:///C:/QiLabs/_QiOS_DNA/00_QiEOS/90_receipts/50_generated_reports/qilabs_structure_check.md)`
  * `[wiki_publish_plan.md](file:///C:/QiLabs/_QiOS_DNA/60_QiApps/qiaccess_start/wiki_publish_plan.md)`
  * `[QiIngest_Pipeline.md](file:///C:/QiLabs/_QiOS_DNA/70_QiConnect/06_workflows/QiIngest_Pipeline.md)`
  * `[ADR-0013_folder_documentation_model.md](file:///C:/QiLabs/_QiOS_DNA/decisions/ADR-0013_folder_documentation_model.md)`
  * `[2026-06-10_qidna_implementation_reconciliation.md](file:///C:/QiLabs/_QiOS_DNA/Reconciliation/2026-06-10_qidna_implementation_reconciliation.md)`

### File: `_index.md`
- **Current Path**: `00_QiEOS/30_service_map/40_productivity/_index.md`
- **Proposed Move**: `60_QiApps/_index.md`
- **Referenced in**:
  * `[_index.md](file:///C:/QiLabs/_QiOS_DNA/00_QiEOS/_index.md)`
  * `[_index.md](file:///C:/QiLabs/_QiOS_DNA/00_QiEOS/10_governance/_index.md)`
  * `[blueprint_map.md](file:///C:/QiLabs/_QiOS_DNA/00_QiEOS/60_assets/diagrams/blueprint_map.md)`
  * `[qilabs_structure_check.md](file:///C:/QiLabs/_QiOS_DNA/00_QiEOS/90_receipts/50_generated_reports/qilabs_structure_check.md)`
  * `[wiki_publish_plan.md](file:///C:/QiLabs/_QiOS_DNA/60_QiApps/qiaccess_start/wiki_publish_plan.md)`
  * `[QiIngest_Pipeline.md](file:///C:/QiLabs/_QiOS_DNA/70_QiConnect/06_workflows/QiIngest_Pipeline.md)`
  * `[ADR-0013_folder_documentation_model.md](file:///C:/QiLabs/_QiOS_DNA/decisions/ADR-0013_folder_documentation_model.md)`
  * `[2026-06-10_qidna_implementation_reconciliation.md](file:///C:/QiLabs/_QiOS_DNA/Reconciliation/2026-06-10_qidna_implementation_reconciliation.md)`

### File: `qiledger.md`
- **Current Path**: `00_QiEOS/30_service_map/40_productivity/qiledger.md`
- **Proposed Move**: `60_QiApps/qiledger.md`
- **Referenced in**:
  * `[firefly.md](file:///C:/QiLabs/_QiOS_DNA/00_QiEOS/30_service_map/120_applications/firefly.md)`
  * `[roadmap.md](file:///C:/QiLabs/_QiOS_DNA/00_QiEOS/30_service_map/120_applications/roadmap.md)`
  * `[_index.md](file:///C:/QiLabs/_QiOS_DNA/00_QiEOS/30_service_map/120_applications/_index.md)`

### File: `_index.md`
- **Current Path**: `00_QiEOS/30_service_map/50_apis/_index.md`
- **Proposed Move**: `70_QiConnect/_index.md`
- **Referenced in**:
  * `[_index.md](file:///C:/QiLabs/_QiOS_DNA/00_QiEOS/_index.md)`
  * `[_index.md](file:///C:/QiLabs/_QiOS_DNA/00_QiEOS/10_governance/_index.md)`
  * `[blueprint_map.md](file:///C:/QiLabs/_QiOS_DNA/00_QiEOS/60_assets/diagrams/blueprint_map.md)`
  * `[qilabs_structure_check.md](file:///C:/QiLabs/_QiOS_DNA/00_QiEOS/90_receipts/50_generated_reports/qilabs_structure_check.md)`
  * `[wiki_publish_plan.md](file:///C:/QiLabs/_QiOS_DNA/60_QiApps/qiaccess_start/wiki_publish_plan.md)`
  * `[QiIngest_Pipeline.md](file:///C:/QiLabs/_QiOS_DNA/70_QiConnect/06_workflows/QiIngest_Pipeline.md)`
  * `[ADR-0013_folder_documentation_model.md](file:///C:/QiLabs/_QiOS_DNA/decisions/ADR-0013_folder_documentation_model.md)`
  * `[2026-06-10_qidna_implementation_reconciliation.md](file:///C:/QiLabs/_QiOS_DNA/Reconciliation/2026-06-10_qidna_implementation_reconciliation.md)`

### File: `_index.md`
- **Current Path**: `00_QiEOS/30_service_map/60_workers/_index.md`
- **Proposed Move**: `20_QiSystem/_index.md`
- **Referenced in**:
  * `[_index.md](file:///C:/QiLabs/_QiOS_DNA/00_QiEOS/_index.md)`
  * `[_index.md](file:///C:/QiLabs/_QiOS_DNA/00_QiEOS/10_governance/_index.md)`
  * `[blueprint_map.md](file:///C:/QiLabs/_QiOS_DNA/00_QiEOS/60_assets/diagrams/blueprint_map.md)`
  * `[qilabs_structure_check.md](file:///C:/QiLabs/_QiOS_DNA/00_QiEOS/90_receipts/50_generated_reports/qilabs_structure_check.md)`
  * `[wiki_publish_plan.md](file:///C:/QiLabs/_QiOS_DNA/60_QiApps/qiaccess_start/wiki_publish_plan.md)`
  * `[QiIngest_Pipeline.md](file:///C:/QiLabs/_QiOS_DNA/70_QiConnect/06_workflows/QiIngest_Pipeline.md)`
  * `[ADR-0013_folder_documentation_model.md](file:///C:/QiLabs/_QiOS_DNA/decisions/ADR-0013_folder_documentation_model.md)`
  * `[2026-06-10_qidna_implementation_reconciliation.md](file:///C:/QiLabs/_QiOS_DNA/Reconciliation/2026-06-10_qidna_implementation_reconciliation.md)`

### File: `_index.md`
- **Current Path**: `00_QiEOS/30_service_map/70_pipelines/_index.md`
- **Proposed Move**: `40_QiCapture/_index.md`
- **Referenced in**:
  * `[_index.md](file:///C:/QiLabs/_QiOS_DNA/00_QiEOS/_index.md)`
  * `[_index.md](file:///C:/QiLabs/_QiOS_DNA/00_QiEOS/10_governance/_index.md)`
  * `[blueprint_map.md](file:///C:/QiLabs/_QiOS_DNA/00_QiEOS/60_assets/diagrams/blueprint_map.md)`
  * `[qilabs_structure_check.md](file:///C:/QiLabs/_QiOS_DNA/00_QiEOS/90_receipts/50_generated_reports/qilabs_structure_check.md)`
  * `[wiki_publish_plan.md](file:///C:/QiLabs/_QiOS_DNA/60_QiApps/qiaccess_start/wiki_publish_plan.md)`
  * `[QiIngest_Pipeline.md](file:///C:/QiLabs/_QiOS_DNA/70_QiConnect/06_workflows/QiIngest_Pipeline.md)`
  * `[ADR-0013_folder_documentation_model.md](file:///C:/QiLabs/_QiOS_DNA/decisions/ADR-0013_folder_documentation_model.md)`
  * `[2026-06-10_qidna_implementation_reconciliation.md](file:///C:/QiLabs/_QiOS_DNA/Reconciliation/2026-06-10_qidna_implementation_reconciliation.md)`

### File: `_index.md`
- **Current Path**: `00_QiEOS/30_service_map/80_tools/_index.md`
- **Proposed Move**: `20_QiSystem/_index.md`
- **Referenced in**:
  * `[_index.md](file:///C:/QiLabs/_QiOS_DNA/00_QiEOS/_index.md)`
  * `[_index.md](file:///C:/QiLabs/_QiOS_DNA/00_QiEOS/10_governance/_index.md)`
  * `[blueprint_map.md](file:///C:/QiLabs/_QiOS_DNA/00_QiEOS/60_assets/diagrams/blueprint_map.md)`
  * `[qilabs_structure_check.md](file:///C:/QiLabs/_QiOS_DNA/00_QiEOS/90_receipts/50_generated_reports/qilabs_structure_check.md)`
  * `[wiki_publish_plan.md](file:///C:/QiLabs/_QiOS_DNA/60_QiApps/qiaccess_start/wiki_publish_plan.md)`
  * `[QiIngest_Pipeline.md](file:///C:/QiLabs/_QiOS_DNA/70_QiConnect/06_workflows/QiIngest_Pipeline.md)`
  * `[ADR-0013_folder_documentation_model.md](file:///C:/QiLabs/_QiOS_DNA/decisions/ADR-0013_folder_documentation_model.md)`
  * `[2026-06-10_qidna_implementation_reconciliation.md](file:///C:/QiLabs/_QiOS_DNA/Reconciliation/2026-06-10_qidna_implementation_reconciliation.md)`

### File: `_index.md`
- **Current Path**: `00_QiEOS/30_service_map/90_interfaces/_index.md`
- **Proposed Move**: `70_QiConnect/_index.md`
- **Referenced in**:
  * `[_index.md](file:///C:/QiLabs/_QiOS_DNA/00_QiEOS/_index.md)`
  * `[_index.md](file:///C:/QiLabs/_QiOS_DNA/00_QiEOS/10_governance/_index.md)`
  * `[blueprint_map.md](file:///C:/QiLabs/_QiOS_DNA/00_QiEOS/60_assets/diagrams/blueprint_map.md)`
  * `[qilabs_structure_check.md](file:///C:/QiLabs/_QiOS_DNA/00_QiEOS/90_receipts/50_generated_reports/qilabs_structure_check.md)`
  * `[wiki_publish_plan.md](file:///C:/QiLabs/_QiOS_DNA/60_QiApps/qiaccess_start/wiki_publish_plan.md)`
  * `[QiIngest_Pipeline.md](file:///C:/QiLabs/_QiOS_DNA/70_QiConnect/06_workflows/QiIngest_Pipeline.md)`
  * `[ADR-0013_folder_documentation_model.md](file:///C:/QiLabs/_QiOS_DNA/decisions/ADR-0013_folder_documentation_model.md)`
  * `[2026-06-10_qidna_implementation_reconciliation.md](file:///C:/QiLabs/_QiOS_DNA/Reconciliation/2026-06-10_qidna_implementation_reconciliation.md)`

### File: `_index.md`
- **Current Path**: `00_QiEOS/30_service_map/_index.md`
- **Proposed Move**: `00_QiEOS/_index.md`
- **Referenced in**:
  * `[_index.md](file:///C:/QiLabs/_QiOS_DNA/00_QiEOS/_index.md)`
  * `[_index.md](file:///C:/QiLabs/_QiOS_DNA/00_QiEOS/10_governance/_index.md)`
  * `[blueprint_map.md](file:///C:/QiLabs/_QiOS_DNA/00_QiEOS/60_assets/diagrams/blueprint_map.md)`
  * `[qilabs_structure_check.md](file:///C:/QiLabs/_QiOS_DNA/00_QiEOS/90_receipts/50_generated_reports/qilabs_structure_check.md)`
  * `[wiki_publish_plan.md](file:///C:/QiLabs/_QiOS_DNA/60_QiApps/qiaccess_start/wiki_publish_plan.md)`
  * `[QiIngest_Pipeline.md](file:///C:/QiLabs/_QiOS_DNA/70_QiConnect/06_workflows/QiIngest_Pipeline.md)`
  * `[ADR-0013_folder_documentation_model.md](file:///C:/QiLabs/_QiOS_DNA/decisions/ADR-0013_folder_documentation_model.md)`
  * `[2026-06-10_qidna_implementation_reconciliation.md](file:///C:/QiLabs/_QiOS_DNA/Reconciliation/2026-06-10_qidna_implementation_reconciliation.md)`

### File: `_index.md`
- **Current Path**: `00_QiEOS/40_operations/10_cases/_index.md`
- **Proposed Move**: `20_QiSystem/_index.md`
- **Referenced in**:
  * `[_index.md](file:///C:/QiLabs/_QiOS_DNA/00_QiEOS/_index.md)`
  * `[_index.md](file:///C:/QiLabs/_QiOS_DNA/00_QiEOS/10_governance/_index.md)`
  * `[blueprint_map.md](file:///C:/QiLabs/_QiOS_DNA/00_QiEOS/60_assets/diagrams/blueprint_map.md)`
  * `[qilabs_structure_check.md](file:///C:/QiLabs/_QiOS_DNA/00_QiEOS/90_receipts/50_generated_reports/qilabs_structure_check.md)`
  * `[wiki_publish_plan.md](file:///C:/QiLabs/_QiOS_DNA/60_QiApps/qiaccess_start/wiki_publish_plan.md)`
  * `[QiIngest_Pipeline.md](file:///C:/QiLabs/_QiOS_DNA/70_QiConnect/06_workflows/QiIngest_Pipeline.md)`
  * `[ADR-0013_folder_documentation_model.md](file:///C:/QiLabs/_QiOS_DNA/decisions/ADR-0013_folder_documentation_model.md)`
  * `[2026-06-10_qidna_implementation_reconciliation.md](file:///C:/QiLabs/_QiOS_DNA/Reconciliation/2026-06-10_qidna_implementation_reconciliation.md)`

### File: `_index.md`
- **Current Path**: `00_QiEOS/40_operations/20_qiserver/_index.md`
- **Proposed Move**: `20_QiSystem/_index.md`
- **Referenced in**:
  * `[_index.md](file:///C:/QiLabs/_QiOS_DNA/00_QiEOS/_index.md)`
  * `[_index.md](file:///C:/QiLabs/_QiOS_DNA/00_QiEOS/10_governance/_index.md)`
  * `[blueprint_map.md](file:///C:/QiLabs/_QiOS_DNA/00_QiEOS/60_assets/diagrams/blueprint_map.md)`
  * `[qilabs_structure_check.md](file:///C:/QiLabs/_QiOS_DNA/00_QiEOS/90_receipts/50_generated_reports/qilabs_structure_check.md)`
  * `[wiki_publish_plan.md](file:///C:/QiLabs/_QiOS_DNA/60_QiApps/qiaccess_start/wiki_publish_plan.md)`
  * `[QiIngest_Pipeline.md](file:///C:/QiLabs/_QiOS_DNA/70_QiConnect/06_workflows/QiIngest_Pipeline.md)`
  * `[ADR-0013_folder_documentation_model.md](file:///C:/QiLabs/_QiOS_DNA/decisions/ADR-0013_folder_documentation_model.md)`
  * `[2026-06-10_qidna_implementation_reconciliation.md](file:///C:/QiLabs/_QiOS_DNA/Reconciliation/2026-06-10_qidna_implementation_reconciliation.md)`

### File: `2026-05-17_open_loop_reset_paperless_ingestion_runbook.md`
- **Current Path**: `00_QiEOS/40_operations/30_dev_history/2026-05-17_open_loop_reset_paperless_ingestion_runbook.md`
- **Proposed Move**: `30_QiServer/2026-05-17_open_loop_reset_paperless_ingestion_runbook.md`
- **Referenced in**:
  * `[QiIngest_Pipeline.md](file:///C:/QiLabs/_QiOS_DNA/70_QiConnect/06_workflows/QiIngest_Pipeline.md)`

### File: `_index.md`
- **Current Path**: `00_QiEOS/40_operations/_index.md`
- **Proposed Move**: `20_QiSystem/_index.md`
- **Referenced in**:
  * `[_index.md](file:///C:/QiLabs/_QiOS_DNA/00_QiEOS/_index.md)`
  * `[_index.md](file:///C:/QiLabs/_QiOS_DNA/00_QiEOS/10_governance/_index.md)`
  * `[blueprint_map.md](file:///C:/QiLabs/_QiOS_DNA/00_QiEOS/60_assets/diagrams/blueprint_map.md)`
  * `[qilabs_structure_check.md](file:///C:/QiLabs/_QiOS_DNA/00_QiEOS/90_receipts/50_generated_reports/qilabs_structure_check.md)`
  * `[wiki_publish_plan.md](file:///C:/QiLabs/_QiOS_DNA/60_QiApps/qiaccess_start/wiki_publish_plan.md)`
  * `[QiIngest_Pipeline.md](file:///C:/QiLabs/_QiOS_DNA/70_QiConnect/06_workflows/QiIngest_Pipeline.md)`
  * `[ADR-0013_folder_documentation_model.md](file:///C:/QiLabs/_QiOS_DNA/decisions/ADR-0013_folder_documentation_model.md)`
  * `[2026-06-10_qidna_implementation_reconciliation.md](file:///C:/QiLabs/_QiOS_DNA/Reconciliation/2026-06-10_qidna_implementation_reconciliation.md)`

### File: `20_glossary.md`
- **Current Path**: `00_QiEOS/50_knowledge/20_glossary.md`
- **Proposed Move**: `00_QiEOS/20_glossary.md`
- **Referenced in**:
  * `[_index.md](file:///C:/QiLabs/_QiOS_DNA/00_QiEOS/50_knowledge/_index.md)`

### File: `30_migration_notes.md`
- **Current Path**: `00_QiEOS/50_knowledge/30_migration_notes.md`
- **Proposed Move**: `Reconciliation/30_migration_notes.md`
- **Referenced in**:
  * `[_index.md](file:///C:/QiLabs/_QiOS_DNA/00_QiEOS/50_knowledge/_index.md)`

### File: `40_legacy_csv_migration_plan.md`
- **Current Path**: `00_QiEOS/50_knowledge/40_legacy_csv_migration_plan.md`
- **Proposed Move**: `Reconciliation/40_legacy_csv_migration_plan.md`
- **Referenced in**:
  * `[_index.md](file:///C:/QiLabs/_QiOS_DNA/00_QiEOS/50_knowledge/_index.md)`

### File: `50_legacy_salvage.md`
- **Current Path**: `00_QiEOS/50_knowledge/50_legacy_salvage.md`
- **Proposed Move**: `90_archive/50_legacy_salvage.md`
- **Referenced in**:
  * `[_index.md](file:///C:/QiLabs/_QiOS_DNA/00_QiEOS/50_knowledge/_index.md)`

### File: `60_qiaccess_start_legacy_quarantine.md`
- **Current Path**: `00_QiEOS/50_knowledge/60_qiaccess_start_legacy_quarantine.md`
- **Proposed Move**: `90_archive/60_qiaccess_start_legacy_quarantine.md`
- **Referenced in**:
  * `[_index.md](file:///C:/QiLabs/_QiOS_DNA/00_QiEOS/50_knowledge/_index.md)`

### File: `70_repo_sync_status_20260516.md`
- **Current Path**: `00_QiEOS/50_knowledge/70_repo_sync_status_20260516.md`
- **Proposed Move**: `Reconciliation/70_repo_sync_status_20260516.md`
- **Referenced in**:
  * `[_index.md](file:///C:/QiLabs/_QiOS_DNA/00_QiEOS/50_knowledge/_index.md)`

### File: `QiAccess_Start_Blueprint.md`
- **Current Path**: `00_QiEOS/50_knowledge/90_superseded_sources/QiAccess_Start_Blueprint.md`
- **Proposed Move**: `90_archive/QiAccess_Start_Blueprint.md`
- **Referenced in**:
  * `[blueprint_map.md](file:///C:/QiLabs/_QiOS_DNA/00_QiEOS/60_assets/diagrams/blueprint_map.md)`

### File: `README.md`
- **Current Path**: `00_QiEOS/50_knowledge/90_superseded_sources/README.md`
- **Proposed Move**: `90_archive/README.md`
- **Referenced in**:
  * `[build.js](file:///C:/QiLabs/_QiOS_DNA/build.js)`
  * `[file-index.json](file:///C:/QiLabs/_QiOS_DNA/00_QiEOS/file-index.json)`
  * `[codex.md](file:///C:/QiLabs/_QiOS_DNA/codex.md)`
  * `[QiAccess_Start_Blueprint.md](file:///C:/QiLabs/_QiOS_DNA/00_QiEOS/QiAccess_Start_Blueprint.md)`
  * `[60_directory_tree.md](file:///C:/QiLabs/_QiOS_DNA/00_QiEOS/10_governance/60_registry/60_directory_tree.md)`
  * `[qinote_salvage_extract.md](file:///C:/QiLabs/_QiOS_DNA/00_QiEOS/30_service_map/120_applications/qinote/qinote_salvage_extract.md)`
  * `[operator_tools.md](file:///C:/QiLabs/_QiOS_DNA/00_QiEOS/30_service_map/80_tools/operator_tools.md)`
  * `[2026-05-16_dev_session_directory_markmind_mapper.md](file:///C:/QiLabs/_QiOS_DNA/00_QiEOS/40_operations/30_dev_history/2026-05-16_dev_session_directory_markmind_mapper.md)`
  * `[2026-05-17_open_loop_reset_paperless_ingestion_runbook.md](file:///C:/QiLabs/_QiOS_DNA/00_QiEOS/40_operations/30_dev_history/2026-05-17_open_loop_reset_paperless_ingestion_runbook.md)`
  * `[2026-05-17_momcare_app_qa_checklist.md](file:///C:/QiLabs/_QiOS_DNA/00_QiEOS/40_operations/40_dev_testing/momscare/2026-05-17_momcare_app_qa_checklist.md)`
  * `[2026-05-17_qiaccess_start_qa_checklist.md](file:///C:/QiLabs/_QiOS_DNA/00_QiEOS/40_operations/40_dev_testing/qiaccessstart/2026-05-17_qiaccess_start_qa_checklist.md)`
  * `[blueprint_map.md](file:///C:/QiLabs/_QiOS_DNA/00_QiEOS/60_assets/diagrams/blueprint_map.md)`
  * `[2026-05-24_qiaccess_homepage_conversion_report.md](file:///C:/QiLabs/_QiOS_DNA/00_QiEOS/90_receipts/_audit/2026-05-24_qiaccess_homepage_conversion_report.md)`
  * `[2026-05-24_qiaccess_homepage_local_validation_report.md](file:///C:/QiLabs/_QiOS_DNA/00_QiEOS/90_receipts/_audit/2026-05-24_qiaccess_homepage_local_validation_report.md)`
  * `[2026-06-09_codex_reconciliation_brief.md](file:///C:/QiLabs/_QiOS_DNA/00_QiEOS/reconciliation/2026-06-09_codex_reconciliation_brief.md)`
  * `[2026-06-10_blueprint_readiness_and_decision_gate.md](file:///C:/QiLabs/_QiOS_DNA/Reconciliation/2026-06-10_blueprint_readiness_and_decision_gate.md)`

### File: `qi_os_home_blueprint.md`
- **Current Path**: `00_QiEOS/50_knowledge/90_superseded_sources/qi_os_home_blueprint.md`
- **Proposed Move**: `90_archive/qi_os_home_blueprint.md`
- **Referenced in**:
  * `[blueprint_map.md](file:///C:/QiLabs/_QiOS_DNA/00_QiEOS/60_assets/diagrams/blueprint_map.md)`

### File: `tech_stack_markmind.md`
- **Current Path**: `00_QiEOS/50_knowledge/90_superseded_sources/tech_stack_markmind.md`
- **Proposed Move**: `90_archive/tech_stack_markmind.md`
- **Referenced in**:
  * `[blueprint_map.md](file:///C:/QiLabs/_QiOS_DNA/00_QiEOS/60_assets/diagrams/blueprint_map.md)`

### File: `_index.md`
- **Current Path**: `00_QiEOS/50_knowledge/_index.md`
- **Proposed Move**: `00_QiEOS/_index.md`
- **Referenced in**:
  * `[_index.md](file:///C:/QiLabs/_QiOS_DNA/00_QiEOS/_index.md)`
  * `[_index.md](file:///C:/QiLabs/_QiOS_DNA/00_QiEOS/10_governance/_index.md)`
  * `[blueprint_map.md](file:///C:/QiLabs/_QiOS_DNA/00_QiEOS/60_assets/diagrams/blueprint_map.md)`
  * `[qilabs_structure_check.md](file:///C:/QiLabs/_QiOS_DNA/00_QiEOS/90_receipts/50_generated_reports/qilabs_structure_check.md)`
  * `[wiki_publish_plan.md](file:///C:/QiLabs/_QiOS_DNA/60_QiApps/qiaccess_start/wiki_publish_plan.md)`
  * `[QiIngest_Pipeline.md](file:///C:/QiLabs/_QiOS_DNA/70_QiConnect/06_workflows/QiIngest_Pipeline.md)`
  * `[ADR-0013_folder_documentation_model.md](file:///C:/QiLabs/_QiOS_DNA/decisions/ADR-0013_folder_documentation_model.md)`
  * `[2026-06-10_qidna_implementation_reconciliation.md](file:///C:/QiLabs/_QiOS_DNA/Reconciliation/2026-06-10_qidna_implementation_reconciliation.md)`

### File: `assets.md`
- **Current Path**: `00_QiEOS/60_assets/assets.md`
- **Proposed Move**: `assets/assets.md`
- **Referenced in**:
  * `[file-index.json](file:///C:/QiLabs/_QiOS_DNA/00_QiEOS/file-index.json)`
  * `[blueprint_map.md](file:///C:/QiLabs/_QiOS_DNA/00_QiEOS/60_assets/diagrams/blueprint_map.md)`

### File: `diagrams.md`
- **Current Path**: `00_QiEOS/60_assets/diagrams/diagrams.md`
- **Proposed Move**: `assets/diagrams.md`
- **Referenced in**:
  * `[file-index.json](file:///C:/QiLabs/_QiOS_DNA/00_QiEOS/file-index.json)`
  * `[blueprint_map.md](file:///C:/QiLabs/_QiOS_DNA/00_QiEOS/60_assets/diagrams/blueprint_map.md)`

### File: `markmind-data.json`
- **Current Path**: `00_QiEOS/60_assets/diagrams/markmind-data.json`
- **Proposed Move**: `assets/markmind-data.json`
- **Referenced in**:
  * `[file-index.json](file:///C:/QiLabs/_QiOS_DNA/00_QiEOS/file-index.json)`
  * `[blueprint_map.md](file:///C:/QiLabs/_QiOS_DNA/00_QiEOS/60_assets/diagrams/blueprint_map.md)`

### File: `markmind.html`
- **Current Path**: `00_QiEOS/60_assets/diagrams/markmind.html`
- **Proposed Move**: `assets/markmind.html`
- **Referenced in**:
  * `[file-index.json](file:///C:/QiLabs/_QiOS_DNA/00_QiEOS/file-index.json)`

### File: `_QiOS_Master_Document.jpg`
- **Current Path**: `00_QiEOS/60_assets/images/_QiOS_Master_Document.jpg`
- **Proposed Move**: `assets/_QiOS_Master_Document.jpg`
- **Referenced in**:
  * `[file-index.json](file:///C:/QiLabs/_QiOS_DNA/00_QiEOS/file-index.json)`

### File: `README.md`
- **Current Path**: `00_QiEOS/60_assets/templates/README.md`
- **Proposed Move**: `assets/README.md`
- **Referenced in**:
  * `[build.js](file:///C:/QiLabs/_QiOS_DNA/build.js)`
  * `[file-index.json](file:///C:/QiLabs/_QiOS_DNA/00_QiEOS/file-index.json)`
  * `[codex.md](file:///C:/QiLabs/_QiOS_DNA/codex.md)`
  * `[QiAccess_Start_Blueprint.md](file:///C:/QiLabs/_QiOS_DNA/00_QiEOS/QiAccess_Start_Blueprint.md)`
  * `[60_directory_tree.md](file:///C:/QiLabs/_QiOS_DNA/00_QiEOS/10_governance/60_registry/60_directory_tree.md)`
  * `[qinote_salvage_extract.md](file:///C:/QiLabs/_QiOS_DNA/00_QiEOS/30_service_map/120_applications/qinote/qinote_salvage_extract.md)`
  * `[operator_tools.md](file:///C:/QiLabs/_QiOS_DNA/00_QiEOS/30_service_map/80_tools/operator_tools.md)`
  * `[2026-05-16_dev_session_directory_markmind_mapper.md](file:///C:/QiLabs/_QiOS_DNA/00_QiEOS/40_operations/30_dev_history/2026-05-16_dev_session_directory_markmind_mapper.md)`
  * `[2026-05-17_open_loop_reset_paperless_ingestion_runbook.md](file:///C:/QiLabs/_QiOS_DNA/00_QiEOS/40_operations/30_dev_history/2026-05-17_open_loop_reset_paperless_ingestion_runbook.md)`
  * `[2026-05-17_momcare_app_qa_checklist.md](file:///C:/QiLabs/_QiOS_DNA/00_QiEOS/40_operations/40_dev_testing/momscare/2026-05-17_momcare_app_qa_checklist.md)`
  * `[2026-05-17_qiaccess_start_qa_checklist.md](file:///C:/QiLabs/_QiOS_DNA/00_QiEOS/40_operations/40_dev_testing/qiaccessstart/2026-05-17_qiaccess_start_qa_checklist.md)`
  * `[blueprint_map.md](file:///C:/QiLabs/_QiOS_DNA/00_QiEOS/60_assets/diagrams/blueprint_map.md)`
  * `[2026-05-24_qiaccess_homepage_conversion_report.md](file:///C:/QiLabs/_QiOS_DNA/00_QiEOS/90_receipts/_audit/2026-05-24_qiaccess_homepage_conversion_report.md)`
  * `[2026-05-24_qiaccess_homepage_local_validation_report.md](file:///C:/QiLabs/_QiOS_DNA/00_QiEOS/90_receipts/_audit/2026-05-24_qiaccess_homepage_local_validation_report.md)`
  * `[2026-06-09_codex_reconciliation_brief.md](file:///C:/QiLabs/_QiOS_DNA/00_QiEOS/reconciliation/2026-06-09_codex_reconciliation_brief.md)`
  * `[2026-06-10_blueprint_readiness_and_decision_gate.md](file:///C:/QiLabs/_QiOS_DNA/Reconciliation/2026-06-10_blueprint_readiness_and_decision_gate.md)`

### File: `_index.md`
- **Current Path**: `00_QiEOS/60_assets/templates/_index.md`
- **Proposed Move**: `assets/_index.md`
- **Referenced in**:
  * `[_index.md](file:///C:/QiLabs/_QiOS_DNA/00_QiEOS/_index.md)`
  * `[_index.md](file:///C:/QiLabs/_QiOS_DNA/00_QiEOS/10_governance/_index.md)`
  * `[blueprint_map.md](file:///C:/QiLabs/_QiOS_DNA/00_QiEOS/60_assets/diagrams/blueprint_map.md)`
  * `[qilabs_structure_check.md](file:///C:/QiLabs/_QiOS_DNA/00_QiEOS/90_receipts/50_generated_reports/qilabs_structure_check.md)`
  * `[wiki_publish_plan.md](file:///C:/QiLabs/_QiOS_DNA/60_QiApps/qiaccess_start/wiki_publish_plan.md)`
  * `[QiIngest_Pipeline.md](file:///C:/QiLabs/_QiOS_DNA/70_QiConnect/06_workflows/QiIngest_Pipeline.md)`
  * `[ADR-0013_folder_documentation_model.md](file:///C:/QiLabs/_QiOS_DNA/decisions/ADR-0013_folder_documentation_model.md)`
  * `[2026-06-10_qidna_implementation_reconciliation.md](file:///C:/QiLabs/_QiOS_DNA/Reconciliation/2026-06-10_qidna_implementation_reconciliation.md)`

### File: `adr_template.md`
- **Current Path**: `00_QiEOS/60_assets/templates/adr_template.md`
- **Proposed Move**: `00_QiEOS/adr_template.md`
- **Referenced in**:
  * `[file-index.json](file:///C:/QiLabs/_QiOS_DNA/00_QiEOS/file-index.json)`
  * `[ADR-0007_unified_front_matter_and_progressive_doc_topology.md](file:///C:/QiLabs/_QiOS_DNA/00_QiEOS/10_governance/50_decisions/ADR-0007_unified_front_matter_and_progressive_doc_topology.md)`
  * `[blueprint_map.md](file:///C:/QiLabs/_QiOS_DNA/00_QiEOS/60_assets/diagrams/blueprint_map.md)`
  * `[README.md](file:///C:/QiLabs/_QiOS_DNA/00_QiEOS/60_assets/templates/README.md)`

### File: `appendix_template.md`
- **Current Path**: `00_QiEOS/60_assets/templates/appendix_template.md`
- **Proposed Move**: `assets/appendix_template.md`
- **Referenced in**:
  * `[file-index.json](file:///C:/QiLabs/_QiOS_DNA/00_QiEOS/file-index.json)`
  * `[blueprint_map.md](file:///C:/QiLabs/_QiOS_DNA/00_QiEOS/60_assets/diagrams/blueprint_map.md)`

### File: `artifact_template.md`
- **Current Path**: `00_QiEOS/60_assets/templates/artifact_template.md`
- **Proposed Move**: `assets/artifact_template.md`
- **Referenced in**:
  * `[file-index.json](file:///C:/QiLabs/_QiOS_DNA/00_QiEOS/file-index.json)`
  * `[ADR-0007_unified_front_matter_and_progressive_doc_topology.md](file:///C:/QiLabs/_QiOS_DNA/00_QiEOS/10_governance/50_decisions/ADR-0007_unified_front_matter_and_progressive_doc_topology.md)`
  * `[blueprint_map.md](file:///C:/QiLabs/_QiOS_DNA/00_QiEOS/60_assets/diagrams/blueprint_map.md)`
  * `[README.md](file:///C:/QiLabs/_QiOS_DNA/00_QiEOS/60_assets/templates/README.md)`

### File: `note_template.md`
- **Current Path**: `00_QiEOS/60_assets/templates/note_template.md`
- **Proposed Move**: `assets/note_template.md`
- **Referenced in**:
  * `[file-index.json](file:///C:/QiLabs/_QiOS_DNA/00_QiEOS/file-index.json)`
  * `[blueprint_map.md](file:///C:/QiLabs/_QiOS_DNA/00_QiEOS/60_assets/diagrams/blueprint_map.md)`
  * `[README.md](file:///C:/QiLabs/_QiOS_DNA/00_QiEOS/60_assets/templates/README.md)`

### File: `operational_template.md`
- **Current Path**: `00_QiEOS/60_assets/templates/operational_template.md`
- **Proposed Move**: `assets/operational_template.md`
- **Referenced in**:
  * `[file-index.json](file:///C:/QiLabs/_QiOS_DNA/00_QiEOS/file-index.json)`
  * `[blueprint_map.md](file:///C:/QiLabs/_QiOS_DNA/00_QiEOS/60_assets/diagrams/blueprint_map.md)`

### File: `page_template.md`
- **Current Path**: `00_QiEOS/60_assets/templates/page_template.md`
- **Proposed Move**: `assets/page_template.md`
- **Referenced in**:
  * `[file-index.json](file:///C:/QiLabs/_QiOS_DNA/00_QiEOS/file-index.json)`
  * `[ADR-0007_unified_front_matter_and_progressive_doc_topology.md](file:///C:/QiLabs/_QiOS_DNA/00_QiEOS/10_governance/50_decisions/ADR-0007_unified_front_matter_and_progressive_doc_topology.md)`
  * `[blueprint_map.md](file:///C:/QiLabs/_QiOS_DNA/00_QiEOS/60_assets/diagrams/blueprint_map.md)`

### File: `registry_reference_template.md`
- **Current Path**: `00_QiEOS/60_assets/templates/registry_reference_template.md`
- **Proposed Move**: `00_QiEOS/registry_reference_template.md`
- **Referenced in**:
  * `[file-index.json](file:///C:/QiLabs/_QiOS_DNA/00_QiEOS/file-index.json)`
  * `[blueprint_map.md](file:///C:/QiLabs/_QiOS_DNA/00_QiEOS/60_assets/diagrams/blueprint_map.md)`

### File: `section_index_template.md`
- **Current Path**: `00_QiEOS/60_assets/templates/section_index_template.md`
- **Proposed Move**: `00_QiEOS/section_index_template.md`
- **Referenced in**:
  * `[file-index.json](file:///C:/QiLabs/_QiOS_DNA/00_QiEOS/file-index.json)`
  * `[blueprint_map.md](file:///C:/QiLabs/_QiOS_DNA/00_QiEOS/60_assets/diagrams/blueprint_map.md)`

### File: `standard_template.md`
- **Current Path**: `00_QiEOS/60_assets/templates/standard_template.md`
- **Proposed Move**: `00_QiEOS/standard_template.md`
- **Referenced in**:
  * `[file-index.json](file:///C:/QiLabs/_QiOS_DNA/00_QiEOS/file-index.json)`
  * `[blueprint_map.md](file:///C:/QiLabs/_QiOS_DNA/00_QiEOS/60_assets/diagrams/blueprint_map.md)`

### File: `templates.md`
- **Current Path**: `00_QiEOS/60_assets/templates/templates.md`
- **Proposed Move**: `assets/templates.md`
- **Referenced in**:
  * `[file-index.json](file:///C:/QiLabs/_QiOS_DNA/00_QiEOS/file-index.json)`
  * `[blueprint_map.md](file:///C:/QiLabs/_QiOS_DNA/00_QiEOS/60_assets/diagrams/blueprint_map.md)`

### File: `10_changelog.md`
- **Current Path**: `00_QiEOS/90_receipts/10_changelog.md`
- **Proposed Move**: `90_receipts/10_changelog.md`
- **Referenced in**:
  * `[_index.md](file:///C:/QiLabs/_QiOS_DNA/00_QiEOS/50_knowledge/_index.md)`

### File: `_index.md`
- **Current Path**: `00_QiEOS/90_receipts/10_logs/_index.md`
- **Proposed Move**: `90_receipts/_index.md`
- **Referenced in**:
  * `[_index.md](file:///C:/QiLabs/_QiOS_DNA/00_QiEOS/_index.md)`
  * `[_index.md](file:///C:/QiLabs/_QiOS_DNA/00_QiEOS/10_governance/_index.md)`
  * `[blueprint_map.md](file:///C:/QiLabs/_QiOS_DNA/00_QiEOS/60_assets/diagrams/blueprint_map.md)`
  * `[qilabs_structure_check.md](file:///C:/QiLabs/_QiOS_DNA/00_QiEOS/90_receipts/50_generated_reports/qilabs_structure_check.md)`
  * `[wiki_publish_plan.md](file:///C:/QiLabs/_QiOS_DNA/60_QiApps/qiaccess_start/wiki_publish_plan.md)`
  * `[QiIngest_Pipeline.md](file:///C:/QiLabs/_QiOS_DNA/70_QiConnect/06_workflows/QiIngest_Pipeline.md)`
  * `[ADR-0013_folder_documentation_model.md](file:///C:/QiLabs/_QiOS_DNA/decisions/ADR-0013_folder_documentation_model.md)`
  * `[2026-06-10_qidna_implementation_reconciliation.md](file:///C:/QiLabs/_QiOS_DNA/Reconciliation/2026-06-10_qidna_implementation_reconciliation.md)`

### File: `_index.md`
- **Current Path**: `00_QiEOS/90_receipts/20_audits/_index.md`
- **Proposed Move**: `90_receipts/_index.md`
- **Referenced in**:
  * `[_index.md](file:///C:/QiLabs/_QiOS_DNA/00_QiEOS/_index.md)`
  * `[_index.md](file:///C:/QiLabs/_QiOS_DNA/00_QiEOS/10_governance/_index.md)`
  * `[blueprint_map.md](file:///C:/QiLabs/_QiOS_DNA/00_QiEOS/60_assets/diagrams/blueprint_map.md)`
  * `[qilabs_structure_check.md](file:///C:/QiLabs/_QiOS_DNA/00_QiEOS/90_receipts/50_generated_reports/qilabs_structure_check.md)`
  * `[wiki_publish_plan.md](file:///C:/QiLabs/_QiOS_DNA/60_QiApps/qiaccess_start/wiki_publish_plan.md)`
  * `[QiIngest_Pipeline.md](file:///C:/QiLabs/_QiOS_DNA/70_QiConnect/06_workflows/QiIngest_Pipeline.md)`
  * `[ADR-0013_folder_documentation_model.md](file:///C:/QiLabs/_QiOS_DNA/decisions/ADR-0013_folder_documentation_model.md)`
  * `[2026-06-10_qidna_implementation_reconciliation.md](file:///C:/QiLabs/_QiOS_DNA/Reconciliation/2026-06-10_qidna_implementation_reconciliation.md)`

### File: `_index.md`
- **Current Path**: `00_QiEOS/90_receipts/30_backups/_index.md`
- **Proposed Move**: `90_receipts/_index.md`
- **Referenced in**:
  * `[_index.md](file:///C:/QiLabs/_QiOS_DNA/00_QiEOS/_index.md)`
  * `[_index.md](file:///C:/QiLabs/_QiOS_DNA/00_QiEOS/10_governance/_index.md)`
  * `[blueprint_map.md](file:///C:/QiLabs/_QiOS_DNA/00_QiEOS/60_assets/diagrams/blueprint_map.md)`
  * `[qilabs_structure_check.md](file:///C:/QiLabs/_QiOS_DNA/00_QiEOS/90_receipts/50_generated_reports/qilabs_structure_check.md)`
  * `[wiki_publish_plan.md](file:///C:/QiLabs/_QiOS_DNA/60_QiApps/qiaccess_start/wiki_publish_plan.md)`
  * `[QiIngest_Pipeline.md](file:///C:/QiLabs/_QiOS_DNA/70_QiConnect/06_workflows/QiIngest_Pipeline.md)`
  * `[ADR-0013_folder_documentation_model.md](file:///C:/QiLabs/_QiOS_DNA/decisions/ADR-0013_folder_documentation_model.md)`
  * `[2026-06-10_qidna_implementation_reconciliation.md](file:///C:/QiLabs/_QiOS_DNA/Reconciliation/2026-06-10_qidna_implementation_reconciliation.md)`

### File: `_index.md`
- **Current Path**: `00_QiEOS/90_receipts/40_health_checks/_index.md`
- **Proposed Move**: `90_receipts/_index.md`
- **Referenced in**:
  * `[_index.md](file:///C:/QiLabs/_QiOS_DNA/00_QiEOS/_index.md)`
  * `[_index.md](file:///C:/QiLabs/_QiOS_DNA/00_QiEOS/10_governance/_index.md)`
  * `[blueprint_map.md](file:///C:/QiLabs/_QiOS_DNA/00_QiEOS/60_assets/diagrams/blueprint_map.md)`
  * `[qilabs_structure_check.md](file:///C:/QiLabs/_QiOS_DNA/00_QiEOS/90_receipts/50_generated_reports/qilabs_structure_check.md)`
  * `[wiki_publish_plan.md](file:///C:/QiLabs/_QiOS_DNA/60_QiApps/qiaccess_start/wiki_publish_plan.md)`
  * `[QiIngest_Pipeline.md](file:///C:/QiLabs/_QiOS_DNA/70_QiConnect/06_workflows/QiIngest_Pipeline.md)`
  * `[ADR-0013_folder_documentation_model.md](file:///C:/QiLabs/_QiOS_DNA/decisions/ADR-0013_folder_documentation_model.md)`
  * `[2026-06-10_qidna_implementation_reconciliation.md](file:///C:/QiLabs/_QiOS_DNA/Reconciliation/2026-06-10_qidna_implementation_reconciliation.md)`

### File: `_index.md`
- **Current Path**: `00_QiEOS/90_receipts/50_generated_reports/_index.md`
- **Proposed Move**: `90_receipts/_index.md`
- **Referenced in**:
  * `[_index.md](file:///C:/QiLabs/_QiOS_DNA/00_QiEOS/_index.md)`
  * `[_index.md](file:///C:/QiLabs/_QiOS_DNA/00_QiEOS/10_governance/_index.md)`
  * `[blueprint_map.md](file:///C:/QiLabs/_QiOS_DNA/00_QiEOS/60_assets/diagrams/blueprint_map.md)`
  * `[qilabs_structure_check.md](file:///C:/QiLabs/_QiOS_DNA/00_QiEOS/90_receipts/50_generated_reports/qilabs_structure_check.md)`
  * `[wiki_publish_plan.md](file:///C:/QiLabs/_QiOS_DNA/60_QiApps/qiaccess_start/wiki_publish_plan.md)`
  * `[QiIngest_Pipeline.md](file:///C:/QiLabs/_QiOS_DNA/70_QiConnect/06_workflows/QiIngest_Pipeline.md)`
  * `[ADR-0013_folder_documentation_model.md](file:///C:/QiLabs/_QiOS_DNA/decisions/ADR-0013_folder_documentation_model.md)`
  * `[2026-06-10_qidna_implementation_reconciliation.md](file:///C:/QiLabs/_QiOS_DNA/Reconciliation/2026-06-10_qidna_implementation_reconciliation.md)`

### File: `_index.md`
- **Current Path**: `00_QiEOS/90_receipts/60_generated_indexes/_index.md`
- **Proposed Move**: `90_receipts/_index.md`
- **Referenced in**:
  * `[_index.md](file:///C:/QiLabs/_QiOS_DNA/00_QiEOS/_index.md)`
  * `[_index.md](file:///C:/QiLabs/_QiOS_DNA/00_QiEOS/10_governance/_index.md)`
  * `[blueprint_map.md](file:///C:/QiLabs/_QiOS_DNA/00_QiEOS/60_assets/diagrams/blueprint_map.md)`
  * `[qilabs_structure_check.md](file:///C:/QiLabs/_QiOS_DNA/00_QiEOS/90_receipts/50_generated_reports/qilabs_structure_check.md)`
  * `[wiki_publish_plan.md](file:///C:/QiLabs/_QiOS_DNA/60_QiApps/qiaccess_start/wiki_publish_plan.md)`
  * `[QiIngest_Pipeline.md](file:///C:/QiLabs/_QiOS_DNA/70_QiConnect/06_workflows/QiIngest_Pipeline.md)`
  * `[ADR-0013_folder_documentation_model.md](file:///C:/QiLabs/_QiOS_DNA/decisions/ADR-0013_folder_documentation_model.md)`
  * `[2026-06-10_qidna_implementation_reconciliation.md](file:///C:/QiLabs/_QiOS_DNA/Reconciliation/2026-06-10_qidna_implementation_reconciliation.md)`

### File: `_index.md`
- **Current Path**: `00_QiEOS/90_receipts/70_maintenance/_index.md`
- **Proposed Move**: `90_receipts/_index.md`
- **Referenced in**:
  * `[_index.md](file:///C:/QiLabs/_QiOS_DNA/00_QiEOS/_index.md)`
  * `[_index.md](file:///C:/QiLabs/_QiOS_DNA/00_QiEOS/10_governance/_index.md)`
  * `[blueprint_map.md](file:///C:/QiLabs/_QiOS_DNA/00_QiEOS/60_assets/diagrams/blueprint_map.md)`
  * `[qilabs_structure_check.md](file:///C:/QiLabs/_QiOS_DNA/00_QiEOS/90_receipts/50_generated_reports/qilabs_structure_check.md)`
  * `[wiki_publish_plan.md](file:///C:/QiLabs/_QiOS_DNA/60_QiApps/qiaccess_start/wiki_publish_plan.md)`
  * `[QiIngest_Pipeline.md](file:///C:/QiLabs/_QiOS_DNA/70_QiConnect/06_workflows/QiIngest_Pipeline.md)`
  * `[ADR-0013_folder_documentation_model.md](file:///C:/QiLabs/_QiOS_DNA/decisions/ADR-0013_folder_documentation_model.md)`
  * `[2026-06-10_qidna_implementation_reconciliation.md](file:///C:/QiLabs/_QiOS_DNA/Reconciliation/2026-06-10_qidna_implementation_reconciliation.md)`

### File: `Current_Project_State.md`
- **Current Path**: `00_QiEOS/90_receipts/Current_Project_State.md`
- **Proposed Move**: `90_receipts/Current_Project_State.md`
- **Referenced in**:
  * `[current_project_state.md](file:///C:/QiLabs/_QiOS_DNA/00_QiEOS/90_receipts/50_generated_reports/current_project_state.md)`

### File: `2026-05-24_qiaccess_homepage_conversion_report.md`
- **Current Path**: `00_QiEOS/90_receipts/_audit/2026-05-24_qiaccess_homepage_conversion_report.md`
- **Proposed Move**: `90_receipts/2026-05-24_qiaccess_homepage_conversion_report.md`
- **Referenced in**:
  * `[2026-05-24_qiaccess_homepage_local_validation_report.md](file:///C:/QiLabs/_QiOS_DNA/00_QiEOS/90_receipts/_audit/2026-05-24_qiaccess_homepage_local_validation_report.md)`

### File: `2026-05-24_qiaccess_homepage_local_validation_report.md`
- **Current Path**: `00_QiEOS/90_receipts/_audit/2026-05-24_qiaccess_homepage_local_validation_report.md`
- **Proposed Move**: `90_receipts/2026-05-24_qiaccess_homepage_local_validation_report.md`
- **Referenced in**:
  * `[QiAccess_Start_Blueprint.md](file:///C:/QiLabs/_QiOS_DNA/00_QiEOS/QiAccess_Start_Blueprint.md)`

### File: `qiaccess_map.md`
- **Current Path**: `00_QiEOS/90_receipts/_audit/qiaccess_map.md`
- **Proposed Move**: `90_receipts/qiaccess_map.md`
- **Referenced in**:
  * `[qilinks_bookmark_admin_plan.md](file:///C:/QiLabs/_QiOS_DNA/qilinks_bookmark_admin_plan.md)`
  * `[2026-05-24_qilinks_admin_and_visual_map_plan.md](file:///C:/QiLabs/_QiOS_DNA/00_QiEOS/90_receipts/_audit/2026-05-24_qilinks_admin_and_visual_map_plan.md)`

### File: `qiaccess_map.mmd`
- **Current Path**: `00_QiEOS/90_receipts/_audit/qiaccess_map.mmd`
- **Proposed Move**: `90_receipts/qiaccess_map.mmd`
- **Referenced in**:
  * `[qilinks_bookmark_admin_plan.md](file:///C:/QiLabs/_QiOS_DNA/qilinks_bookmark_admin_plan.md)`
  * `[2026-05-24_qilinks_admin_and_visual_map_plan.md](file:///C:/QiLabs/_QiOS_DNA/00_QiEOS/90_receipts/_audit/2026-05-24_qilinks_admin_and_visual_map_plan.md)`

### File: `QiAccess_Start_Blueprint.md`
- **Current Path**: `00_QiEOS/QiAccess_Start_Blueprint.md`
- **Proposed Move**: `10_QiAccess/QiAccess_Start_Blueprint.md`
- **Referenced in**:
  * `[blueprint_map.md](file:///C:/QiLabs/_QiOS_DNA/00_QiEOS/60_assets/diagrams/blueprint_map.md)`

### File: `README.md`
- **Current Path**: `00_QiEOS/README.md`
- **Proposed Move**: `00_QiEOS/README.md`
- **Referenced in**:
  * `[build.js](file:///C:/QiLabs/_QiOS_DNA/build.js)`
  * `[file-index.json](file:///C:/QiLabs/_QiOS_DNA/00_QiEOS/file-index.json)`
  * `[codex.md](file:///C:/QiLabs/_QiOS_DNA/codex.md)`
  * `[QiAccess_Start_Blueprint.md](file:///C:/QiLabs/_QiOS_DNA/00_QiEOS/QiAccess_Start_Blueprint.md)`
  * `[60_directory_tree.md](file:///C:/QiLabs/_QiOS_DNA/00_QiEOS/10_governance/60_registry/60_directory_tree.md)`
  * `[qinote_salvage_extract.md](file:///C:/QiLabs/_QiOS_DNA/00_QiEOS/30_service_map/120_applications/qinote/qinote_salvage_extract.md)`
  * `[operator_tools.md](file:///C:/QiLabs/_QiOS_DNA/00_QiEOS/30_service_map/80_tools/operator_tools.md)`
  * `[2026-05-16_dev_session_directory_markmind_mapper.md](file:///C:/QiLabs/_QiOS_DNA/00_QiEOS/40_operations/30_dev_history/2026-05-16_dev_session_directory_markmind_mapper.md)`
  * `[2026-05-17_open_loop_reset_paperless_ingestion_runbook.md](file:///C:/QiLabs/_QiOS_DNA/00_QiEOS/40_operations/30_dev_history/2026-05-17_open_loop_reset_paperless_ingestion_runbook.md)`
  * `[2026-05-17_momcare_app_qa_checklist.md](file:///C:/QiLabs/_QiOS_DNA/00_QiEOS/40_operations/40_dev_testing/momscare/2026-05-17_momcare_app_qa_checklist.md)`
  * `[2026-05-17_qiaccess_start_qa_checklist.md](file:///C:/QiLabs/_QiOS_DNA/00_QiEOS/40_operations/40_dev_testing/qiaccessstart/2026-05-17_qiaccess_start_qa_checklist.md)`
  * `[blueprint_map.md](file:///C:/QiLabs/_QiOS_DNA/00_QiEOS/60_assets/diagrams/blueprint_map.md)`
  * `[2026-05-24_qiaccess_homepage_conversion_report.md](file:///C:/QiLabs/_QiOS_DNA/00_QiEOS/90_receipts/_audit/2026-05-24_qiaccess_homepage_conversion_report.md)`
  * `[2026-05-24_qiaccess_homepage_local_validation_report.md](file:///C:/QiLabs/_QiOS_DNA/00_QiEOS/90_receipts/_audit/2026-05-24_qiaccess_homepage_local_validation_report.md)`
  * `[2026-06-09_codex_reconciliation_brief.md](file:///C:/QiLabs/_QiOS_DNA/00_QiEOS/reconciliation/2026-06-09_codex_reconciliation_brief.md)`
  * `[2026-06-10_blueprint_readiness_and_decision_gate.md](file:///C:/QiLabs/_QiOS_DNA/Reconciliation/2026-06-10_blueprint_readiness_and_decision_gate.md)`

### File: `_QiEOS.md`
- **Current Path**: `00_QiEOS/_QiEOS.md`
- **Proposed Move**: `00_QiEOS/_QiEOS.md`
- **Referenced in**:
  * `[_01_QiDNA.md](file:///C:/QiLabs/_QiOS_DNA/_01_QiDNA.md)`
  * `[2026-06-10_blueprint_readiness_and_decision_gate.md](file:///C:/QiLabs/_QiOS_DNA/Reconciliation/2026-06-10_blueprint_readiness_and_decision_gate.md)`

### File: `_index.md`
- **Current Path**: `00_QiEOS/_index.md`
- **Proposed Move**: `00_QiEOS/_index.md`
- **Referenced in**:
  * `[_index.md](file:///C:/QiLabs/_QiOS_DNA/00_QiEOS/10_governance/_index.md)`
  * `[blueprint_map.md](file:///C:/QiLabs/_QiOS_DNA/00_QiEOS/60_assets/diagrams/blueprint_map.md)`
  * `[qilabs_structure_check.md](file:///C:/QiLabs/_QiOS_DNA/00_QiEOS/90_receipts/50_generated_reports/qilabs_structure_check.md)`
  * `[wiki_publish_plan.md](file:///C:/QiLabs/_QiOS_DNA/60_QiApps/qiaccess_start/wiki_publish_plan.md)`
  * `[QiIngest_Pipeline.md](file:///C:/QiLabs/_QiOS_DNA/70_QiConnect/06_workflows/QiIngest_Pipeline.md)`
  * `[ADR-0013_folder_documentation_model.md](file:///C:/QiLabs/_QiOS_DNA/decisions/ADR-0013_folder_documentation_model.md)`
  * `[2026-06-10_qidna_implementation_reconciliation.md](file:///C:/QiLabs/_QiOS_DNA/Reconciliation/2026-06-10_qidna_implementation_reconciliation.md)`

### File: `QiOS_Core_Doctrine.mdx`
- **Current Path**: `00_QiEOS/doctrine/QiOS_Core_Doctrine.mdx`
- **Proposed Move**: `00_QiEOS/QiOS_Core_Doctrine.mdx`
- **Referenced in**:
  * `[2026-06-10_blueprint_readiness_and_decision_gate.md](file:///C:/QiLabs/_QiOS_DNA/Reconciliation/2026-06-10_blueprint_readiness_and_decision_gate.md)`

### File: `QiOS_DNA_Chronicle.md`
- **Current Path**: `00_QiEOS/exports/QiOS_DNA_Chronicle.md`
- **Proposed Move**: `90_receipts/QiOS_DNA_Chronicle.md`
- **Referenced in**:
  * `[2026-06-09_codex_reconciliation_brief.md](file:///C:/QiLabs/_QiOS_DNA/00_QiEOS/reconciliation/2026-06-09_codex_reconciliation_brief.md)`
  * `[QiOS_DNA_File_Manifest.mdx](file:///C:/QiLabs/_QiOS_DNA/20_QiSystem/manifests/QiOS_DNA_File_Manifest.mdx)`

### File: `file-index.json`
- **Current Path**: `00_QiEOS/file-index.json`
- **Proposed Move**: `90_receipts/file-index.json`
- **Referenced in**:
  * `[blueprint_map.md](file:///C:/QiLabs/_QiOS_DNA/00_QiEOS/60_assets/diagrams/blueprint_map.md)`

### File: `rebuild.bat`
- **Current Path**: `00_QiEOS/rebuild.bat`
- **Proposed Move**: `00_QiEOS/rebuild.bat`
- **Referenced in**:
  * `[README.md](file:///C:/QiLabs/_QiOS_DNA/00_QiEOS/README.md)`
  * `[tech_stack_markmind.md](file:///C:/QiLabs/_QiOS_DNA/00_QiEOS/50_knowledge/90_superseded_sources/tech_stack_markmind.md)`
  * `[wiki_publish_plan.md](file:///C:/QiLabs/_QiOS_DNA/60_QiApps/qiaccess_start/wiki_publish_plan.md)`
  * `[Core_Workflows.md](file:///C:/QiLabs/_QiOS_DNA/70_QiConnect/06_workflows/Core_Workflows.md)`

### File: `QiOS_Master_Map.mdx`
- **Current Path**: `00_QiEOS/system_map/QiOS_Master_Map.mdx`
- **Proposed Move**: `00_QiEOS/QiOS_Master_Map.mdx`
- **Referenced in**:
  * `[2026-06-10_blueprint_readiness_and_decision_gate.md](file:///C:/QiLabs/_QiOS_DNA/Reconciliation/2026-06-10_blueprint_readiness_and_decision_gate.md)`

### File: `vizvibe.mmd`
- **Current Path**: `00_QiEOS/vizvibe.mmd`
- **Proposed Move**: `00_QiEOS/vizvibe.mmd`
- **Referenced in**:
  * `[70_repo_sync_status_20260516.md](file:///C:/QiLabs/_QiOS_DNA/00_QiEOS/50_knowledge/70_repo_sync_status_20260516.md)`
  * `[blueprint_map.md](file:///C:/QiLabs/_QiOS_DNA/00_QiEOS/60_assets/diagrams/blueprint_map.md)`

## 2. Potential Name Collisions
The following files have duplicate basenames (e.g. `_index.md`) that will exist across domains. Ensure they are nested under appropriate directories in the destination repositories to avoid overwriting:

### Collision Group: `current_project_state.md`
- `00_QiEOS/90_receipts/Current_Project_State.md` (Proposed Action: `move` to `90_receipts`)
- `00_QiEOS/90_receipts/50_generated_reports/current_project_state.md` (Proposed Action: `move` to `90_receipts`)

### Collision Group: `qiaccess_start_blueprint.md`
- `00_QiEOS/QiAccess_Start_Blueprint.md` (Proposed Action: `move` to `10_QiAccess`)
- `00_QiEOS/50_knowledge/90_superseded_sources/QiAccess_Start_Blueprint.md` (Proposed Action: `archive` to `90_archive`)

