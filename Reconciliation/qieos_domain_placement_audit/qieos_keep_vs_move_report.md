# QiEOS Domain Placement Audit: Keep vs Move Report

**Total Files Scanned under `00_QiEOS`:** 194

## 1. Proposed Final Meaning of `00_QiEOS`
> 00_QiEOS is the constitutional layer of QiOS DNA. It defines the system-wide doctrine, governance, registries, naming rules, lifecycle rules, and architectural decisions that other domains must follow. It does not own app docs, server runbooks, service implementation details, generated reports, or legacy project debris.

## 2. Executive Summary
| Action Group | Count | Description |
| --- | --- | --- |
| **Keep in QiEOS** | 86 | Constitutional doctrine, registries, ADRs, principles, policies |
| **Move to Domains** | 94 | Operational, application, and domain-specific markdown files |
| **Archive** | 8 | Superseded, historical, and legacy files |
| **Needs Human Review** | 6 | Ambiguous files requiring manual domain definition |

## 3. Files to Keep in `00_QiEOS`
The following files are system-wide, constitutional, and define the core conventions of the ecosystem:

- `00_QiEOS/10_governance/10_principles/_index.md` (Confidence: `high`)
  *Reason: Constitutional governance, principles, rules, standards, or structural metadata.*
- `00_QiEOS/10_governance/20_rules/_index.md` (Confidence: `high`)
  *Reason: Constitutional governance, principles, rules, standards, or structural metadata.*
- `00_QiEOS/10_governance/30_standards/_index.md` (Confidence: `high`)
  *Reason: Constitutional governance, principles, rules, standards, or structural metadata.*
- `00_QiEOS/10_governance/30_standards/content_metadata_profile.yaml` (Confidence: `high`)
  *Reason: Constitutional governance, principles, rules, standards, or structural metadata.*
- `00_QiEOS/10_governance/30_standards/metadata_rules.yaml` (Confidence: `high`)
  *Reason: Constitutional governance, principles, rules, standards, or structural metadata.*
- `00_QiEOS/10_governance/30_standards/naming_rules.yaml` (Confidence: `high`)
  *Reason: Constitutional governance, principles, rules, standards, or structural metadata.*
- `00_QiEOS/10_governance/30_standards/pdf_standards.yaml` (Confidence: `high`)
  *Reason: Constitutional governance, principles, rules, standards, or structural metadata.*
- `00_QiEOS/10_governance/30_standards/repo_rules.yaml` (Confidence: `high`)
  *Reason: Constitutional governance, principles, rules, standards, or structural metadata.*
- `00_QiEOS/10_governance/40_policies/_index.md` (Confidence: `high`)
  *Reason: Constitutional governance, principles, rules, standards, or structural metadata.*
- `00_QiEOS/10_governance/40_policies/agents/agent_governance_policy.md` (Confidence: `high`)
  *Reason: Constitutional governance, principles, rules, standards, or structural metadata.*
- `00_QiEOS/10_governance/40_policies/architecture/active_runtime_policy.md` (Confidence: `high`)
  *Reason: Constitutional governance, principles, rules, standards, or structural metadata.*
- `00_QiEOS/10_governance/40_policies/architecture/placement_policy.md` (Confidence: `high`)
  *Reason: Constitutional governance, principles, rules, standards, or structural metadata.*
- `00_QiEOS/10_governance/40_policies/architecture/registry_policy.md` (Confidence: `high`)
  *Reason: Canonical system-wide registry / classification.*
- `00_QiEOS/10_governance/40_policies/architecture/root_navigation_policy.md` (Confidence: `high`)
  *Reason: Constitutional governance, principles, rules, standards, or structural metadata.*
- `00_QiEOS/10_governance/40_policies/development/bootstrap_policy.md` (Confidence: `high`)
  *Reason: Constitutional governance, principles, rules, standards, or structural metadata.*
- `00_QiEOS/10_governance/40_policies/development/contribution_policy.md` (Confidence: `high`)
  *Reason: Constitutional governance, principles, rules, standards, or structural metadata.*
- `00_QiEOS/10_governance/40_policies/development/merge_policy.md` (Confidence: `high`)
  *Reason: Constitutional governance, principles, rules, standards, or structural metadata.*
- `00_QiEOS/10_governance/40_policies/operations/legacy_quarantine_policy.md` (Confidence: `high`)
  *Reason: Constitutional governance, principles, rules, standards, or structural metadata.*
- `00_QiEOS/10_governance/40_policies/operations/lifecycle_policy.md` (Confidence: `high`)
  *Reason: Constitutional governance, principles, rules, standards, or structural metadata.*
- `00_QiEOS/10_governance/40_policies/operations/qinexus_freeze_policy.md` (Confidence: `high`)
  *Reason: Constitutional governance, principles, rules, standards, or structural metadata.*
- `00_QiEOS/10_governance/40_policies/security/security_data_access_policy.md` (Confidence: `high`)
  *Reason: Constitutional governance, principles, rules, standards, or structural metadata.*
- `00_QiEOS/10_governance/50_decisions/ADR-0000_template.md` (Confidence: `high`)
  *Reason: Governance ADR template.*
- `00_QiEOS/10_governance/50_decisions/ADR-0001_QiOS_DNA_As_Master_Doctrine_Repo.mdx` (Confidence: `high`)
  *Reason: Architectural Decision Record (System-wide).*
- `00_QiEOS/10_governance/50_decisions/ADR-0001_blueprint_scope.md` (Confidence: `high`)
  *Reason: Architectural Decision Record (System-wide).*
- `00_QiEOS/10_governance/50_decisions/ADR-0002_single_domain_rule.md` (Confidence: `high`)
  *Reason: Architectural Decision Record (System-wide).*
- `00_QiEOS/10_governance/50_decisions/ADR-0003_band_model.md` (Confidence: `high`)
  *Reason: Architectural Decision Record (System-wide).*
- `00_QiEOS/10_governance/50_decisions/ADR-0004_single_account_modular_mode.md` (Confidence: `high`)
  *Reason: Architectural Decision Record (System-wide).*
- `00_QiEOS/10_governance/50_decisions/ADR-0005_fleet_orchestration.md` (Confidence: `high`)
  *Reason: Architectural Decision Record (System-wide).*
- `00_QiEOS/10_governance/50_decisions/ADR-0006_narrative_and_knowledge_consolidation.md` (Confidence: `high`)
  *Reason: Architectural Decision Record (System-wide).*
- `00_QiEOS/10_governance/50_decisions/ADR-0007_unified_front_matter_and_progressive_doc_topology.md` (Confidence: `high`)
  *Reason: Architectural Decision Record (System-wide).*
- `00_QiEOS/10_governance/50_decisions/ADR-0008_qilabs_root.md` (Confidence: `high`)
  *Reason: Architectural Decision Record (System-wide).*
- `00_QiEOS/10_governance/50_decisions/ADR-0009_backup_server_control_plane_and_public_edge_pattern.md` (Confidence: `high`)
  *Reason: Architectural Decision Record (System-wide).*
- `00_QiEOS/10_governance/50_decisions/ADR-0010_qios_namespace_as_routing_metadata_layer.md` (Confidence: `high`)
  *Reason: Architectural Decision Record (System-wide).*
- `00_QiEOS/10_governance/50_decisions/_index.md` (Confidence: `high`)
  *Reason: Constitutional governance, principles, rules, standards, or structural metadata.*
- `00_QiEOS/10_governance/60_registry/100_metadata.md` (Confidence: `high`)
  *Reason: Constitutional governance, principles, rules, standards, or structural metadata.*
- `00_QiEOS/10_governance/60_registry/10_infrastructure_layout.md` (Confidence: `high`)
  *Reason: Constitutional governance, principles, rules, standards, or structural metadata.*
- `00_QiEOS/10_governance/60_registry/110_front_matter.md` (Confidence: `high`)
  *Reason: Constitutional governance, principles, rules, standards, or structural metadata.*
- `00_QiEOS/10_governance/60_registry/120_storage.md` (Confidence: `high`)
  *Reason: Constitutional governance, principles, rules, standards, or structural metadata.*
- `00_QiEOS/10_governance/60_registry/130_placement_rules.md` (Confidence: `high`)
  *Reason: Constitutional governance, principles, rules, standards, or structural metadata.*
- `00_QiEOS/10_governance/60_registry/140_exports.md` (Confidence: `high`)
  *Reason: Constitutional governance, principles, rules, standards, or structural metadata.*
- `00_QiEOS/10_governance/60_registry/150_qievidence.md` (Confidence: `high`)
  *Reason: Constitutional governance, principles, rules, standards, or structural metadata.*
- `00_QiEOS/10_governance/60_registry/160_vectorization_pipeline.md` (Confidence: `high`)
  *Reason: Constitutional governance, principles, rules, standards, or structural metadata.*
- `00_QiEOS/10_governance/60_registry/20_bands.md` (Confidence: `high`)
  *Reason: Constitutional governance, principles, rules, standards, or structural metadata.*
- `00_QiEOS/10_governance/60_registry/30_domains.md` (Confidence: `high`)
  *Reason: Constitutional governance, principles, rules, standards, or structural metadata.*
- `00_QiEOS/10_governance/60_registry/40_subdomains.md` (Confidence: `high`)
  *Reason: Constitutional governance, principles, rules, standards, or structural metadata.*
- `00_QiEOS/10_governance/60_registry/60_directory_tree.md` (Confidence: `high`)
  *Reason: Constitutional governance, principles, rules, standards, or structural metadata.*
- `00_QiEOS/10_governance/60_registry/70_object_model.md` (Confidence: `high`)
  *Reason: Constitutional governance, principles, rules, standards, or structural metadata.*
- `00_QiEOS/10_governance/60_registry/80_objects.md` (Confidence: `high`)
  *Reason: Constitutional governance, principles, rules, standards, or structural metadata.*
- `00_QiEOS/10_governance/60_registry/90_schema.md` (Confidence: `high`)
  *Reason: Constitutional governance, principles, rules, standards, or structural metadata.*
- `00_QiEOS/10_governance/60_registry/_index.md` (Confidence: `high`)
  *Reason: Constitutional governance, principles, rules, standards, or structural metadata.*
- `00_QiEOS/10_governance/60_registry/band_registry.yaml` (Confidence: `high`)
  *Reason: Canonical system-wide registry / classification.*
- `00_QiEOS/10_governance/60_registry/band_registry_v2.yaml` (Confidence: `high`)
  *Reason: Canonical system-wide registry / classification.*
- `00_QiEOS/10_governance/60_registry/deprecation_registry.yaml` (Confidence: `high`)
  *Reason: Canonical system-wide registry / classification.*
- `00_QiEOS/10_governance/60_registry/domain_registry.yaml` (Confidence: `high`)
  *Reason: Canonical system-wide registry / classification.*
- `00_QiEOS/10_governance/60_registry/folder_registry.yaml` (Confidence: `high`)
  *Reason: Canonical system-wide registry / classification.*
- `00_QiEOS/10_governance/60_registry/infrastructure_registry.yaml` (Confidence: `high`)
  *Reason: Canonical system-wide registry / classification.*
- `00_QiEOS/10_governance/60_registry/namespace_registry/2026-05-18_qios_namespace_registry_merged_v2.md` (Confidence: `high`)
  *Reason: Canonical system-wide registry / classification.*
- `00_QiEOS/10_governance/60_registry/namespace_registry/_index.md` (Confidence: `high`)
  *Reason: Constitutional governance, principles, rules, standards, or structural metadata.*
- `00_QiEOS/10_governance/60_registry/realms_registry.yaml` (Confidence: `high`)
  *Reason: Canonical system-wide registry / classification.*
- `00_QiEOS/10_governance/60_registry/schemas/band_registry.schema.json` (Confidence: `high`)
  *Reason: Canonical system-wide registry / classification.*
- `00_QiEOS/10_governance/60_registry/sensitivity_classification.yaml` (Confidence: `high`)
  *Reason: Canonical system-wide registry / classification.*
- `00_QiEOS/10_governance/60_registry/subdomain_registry.yaml` (Confidence: `high`)
  *Reason: Canonical system-wide registry / classification.*
- `00_QiEOS/10_governance/60_registry/workspace_realms.yaml` (Confidence: `high`)
  *Reason: Canonical system-wide registry / classification.*
- `00_QiEOS/10_governance/_index.md` (Confidence: `high`)
  *Reason: Constitutional governance, principles, rules, standards, or structural metadata.*
- `00_QiEOS/20_structure/10_identity.md` (Confidence: `high`)
  *Reason: Constitutional governance, principles, rules, standards, or structural metadata.*
- `00_QiEOS/20_structure/20_system_model.md` (Confidence: `high`)
  *Reason: Constitutional governance, principles, rules, standards, or structural metadata.*
- `00_QiEOS/20_structure/30_component_map.md` (Confidence: `high`)
  *Reason: Constitutional governance, principles, rules, standards, or structural metadata.*
- `00_QiEOS/20_structure/40_service_boundaries.md` (Confidence: `high`)
  *Reason: Constitutional governance, principles, rules, standards, or structural metadata.*
- `00_QiEOS/20_structure/50_data_flow.md` (Confidence: `high`)
  *Reason: Constitutional governance, principles, rules, standards, or structural metadata.*
- `00_QiEOS/20_structure/60_device_model.md` (Confidence: `high`)
  *Reason: Constitutional governance, principles, rules, standards, or structural metadata.*
- `00_QiEOS/20_structure/70_runtime_zones.md` (Confidence: `high`)
  *Reason: Constitutional governance, principles, rules, standards, or structural metadata.*
- `00_QiEOS/20_structure/_index.md` (Confidence: `high`)
  *Reason: Constitutional governance, principles, rules, standards, or structural metadata.*
- `00_QiEOS/40_operations/40_dev_testing/Access_And_Exposure_Rules.md` (Confidence: `medium`)
  *Reason: Governance rule defining exposure level rules.*
- `00_QiEOS/50_knowledge/20_glossary.md` (Confidence: `high`)
  *Reason: System-wide glossary.*
- `00_QiEOS/50_knowledge/_index.md` (Confidence: `medium`)
  *Reason: System-wide knowledge index.*
- `00_QiEOS/60_assets/templates/adr_template.md` (Confidence: `high`)
  *Reason: Core metadata templates for governance.*
- `00_QiEOS/60_assets/templates/registry_reference_template.md` (Confidence: `high`)
  *Reason: Core metadata templates for governance.*
- `00_QiEOS/60_assets/templates/section_index_template.md` (Confidence: `high`)
  *Reason: Core metadata templates for governance.*
- `00_QiEOS/60_assets/templates/standard_template.md` (Confidence: `high`)
  *Reason: Core metadata templates for governance.*
- `00_QiEOS/README.md` (Confidence: `high`)
  *Reason: Core constitutional system-wide structure file.*
- `00_QiEOS/_QiEOS.md` (Confidence: `high`)
  *Reason: Core constitutional system-wide structure file.*
- `00_QiEOS/_index.md` (Confidence: `high`)
  *Reason: Core constitutional system-wide structure file.*
- `00_QiEOS/doctrine/QiOS_Core_Doctrine.mdx` (Confidence: `high`)
  *Reason: Constitutional governance, principles, rules, standards, or structural metadata.*
- `00_QiEOS/rebuild.bat` (Confidence: `medium`)
  *Reason: Build script for the QiEOS surface docs generator.*
- `00_QiEOS/system_map/QiOS_Master_Map.mdx` (Confidence: `high`)
  *Reason: Constitutional governance, principles, rules, standards, or structural metadata.*
- `00_QiEOS/vizvibe.mmd` (Confidence: `high`)
  *Reason: Core constitutional system-wide structure file.*

## 4. Files to Move out of `00_QiEOS` by Target Domain

### Destination: `10_QiAccess`
- `00_QiEOS/40_operations/40_dev_testing/qiaccessstart/2026-05-17_qiaccess_start_qa_checklist.md` -> `10_QiAccess/2026-05-17_qiaccess_start_qa_checklist.md` (Confidence: `high`)
  *Reason: QiAccess application QA testing checklist.*
- `00_QiEOS/QiAccess_Start_Blueprint.md` -> `10_QiAccess/QiAccess_Start_Blueprint.md` (Confidence: `high`)
  *Reason: Operational blueprint of the QiAccess Start module.*

### Destination: `20_QiSystem`
- `00_QiEOS/30_service_map/60_workers/_index.md` -> `20_QiSystem/_index.md` (Confidence: `medium`)
  *Reason: Background workers code/implementation specifications.*
- `00_QiEOS/30_service_map/60_workers/system_workers.md` -> `20_QiSystem/system_workers.md` (Confidence: `medium`)
  *Reason: Background workers code/implementation specifications.*
- `00_QiEOS/30_service_map/70_pipelines/data_pipelines.md` -> `20_QiSystem/data_pipelines.md` (Confidence: `medium`)
  *Reason: Core data pipelines implementation specifications.*
- `00_QiEOS/30_service_map/80_tools/_index.md` -> `20_QiSystem/_index.md` (Confidence: `medium`)
  *Reason: Development and operator utilities specifications.*
- `00_QiEOS/30_service_map/80_tools/operator_tools.md` -> `20_QiSystem/operator_tools.md` (Confidence: `medium`)
  *Reason: Development and operator utilities specifications.*

### Destination: `30_QiServer`
- `00_QiEOS/30_service_map/10_infrastructure/_index.md` -> `30_QiServer/_index.md` (Confidence: `high`)
  *Reason: Infrastructure configuration and server runtime docs.*
- `00_QiEOS/30_service_map/10_infrastructure/cloudflare.md` -> `30_QiServer/cloudflare.md` (Confidence: `high`)
  *Reason: Infrastructure configuration and server runtime docs.*
- `00_QiEOS/30_service_map/10_infrastructure/cockpit/_index.md` -> `30_QiServer/_index.md` (Confidence: `high`)
  *Reason: Infrastructure configuration and server runtime docs.*
- `00_QiEOS/30_service_map/10_infrastructure/cockpit/cockpit_command_menu.md` -> `30_QiServer/cockpit_command_menu.md` (Confidence: `high`)
  *Reason: Infrastructure configuration and server runtime docs.*
- `00_QiEOS/30_service_map/10_infrastructure/docker_compose.md` -> `30_QiServer/docker_compose.md` (Confidence: `high`)
  *Reason: Infrastructure configuration and server runtime docs.*
- `00_QiEOS/30_service_map/10_infrastructure/gethomepage.md` -> `30_QiServer/gethomepage.md` (Confidence: `high`)
  *Reason: Infrastructure configuration and server runtime docs.*
- `00_QiEOS/30_service_map/10_infrastructure/portainer.md` -> `30_QiServer/portainer.md` (Confidence: `high`)
  *Reason: Infrastructure configuration and server runtime docs.*
- `00_QiEOS/30_service_map/10_infrastructure/tailscale.md` -> `30_QiServer/tailscale.md` (Confidence: `high`)
  *Reason: Infrastructure configuration and server runtime docs.*
- `00_QiEOS/30_service_map/10_infrastructure/uptime_kuma.md` -> `30_QiServer/uptime_kuma.md` (Confidence: `high`)
  *Reason: Infrastructure configuration and server runtime docs.*
- `00_QiEOS/30_service_map/110_qiserver/Service_Map.md` -> `30_QiServer/Service_Map.md` (Confidence: `high`)
  *Reason: Infrastructure configuration and server runtime docs.*
- `00_QiEOS/30_service_map/110_qiserver/_index.md` -> `30_QiServer/_index.md` (Confidence: `high`)
  *Reason: Infrastructure configuration and server runtime docs.*
- `00_QiEOS/30_service_map/110_qiserver/runtime.md` -> `30_QiServer/runtime.md` (Confidence: `high`)
  *Reason: Infrastructure configuration and server runtime docs.*
- `00_QiEOS/30_service_map/110_qiserver/runtime_profile.md` -> `30_QiServer/runtime_profile.md` (Confidence: `high`)
  *Reason: Infrastructure configuration and server runtime docs.*
- `00_QiEOS/30_service_map/20_ai_compute/_index.md` -> `30_QiServer/_index.md` (Confidence: `medium`)
  *Reason: Describes AI compute server runtime and configuration.*
- `00_QiEOS/30_service_map/20_ai_compute/aider.md` -> `30_QiServer/aider.md` (Confidence: `medium`)
  *Reason: Describes AI compute server runtime and configuration.*
- `00_QiEOS/30_service_map/20_ai_compute/neo4j.md` -> `30_QiServer/neo4j.md` (Confidence: `medium`)
  *Reason: Describes AI compute server runtime and configuration.*
- `00_QiEOS/30_service_map/20_ai_compute/ollama.md` -> `30_QiServer/ollama.md` (Confidence: `medium`)
  *Reason: Describes AI compute server runtime and configuration.*
- `00_QiEOS/30_service_map/20_ai_compute/open_webui.md` -> `30_QiServer/open_webui.md` (Confidence: `medium`)
  *Reason: Describes AI compute server runtime and configuration.*
- `00_QiEOS/30_service_map/20_ai_compute/qdrant.md` -> `30_QiServer/qdrant.md` (Confidence: `medium`)
  *Reason: Describes AI compute server runtime and configuration.*
- `00_QiEOS/40_operations/20_qiserver/QiAccess_Server_Runbook.md` -> `30_QiServer/QiAccess_Server_Runbook.md` (Confidence: `high`)
  *Reason: Runtime operations and server runbook.*
- `00_QiEOS/40_operations/30_dev_history/2026-05-17_open_loop_reset_paperless_ingestion_runbook.md` -> `30_QiServer/2026-05-17_open_loop_reset_paperless_ingestion_runbook.md` (Confidence: `medium`)
  *Reason: Runbook for services operations.*

### Destination: `40_QiCapture`
- `00_QiEOS/30_service_map/30_capture/_index.md` -> `40_QiCapture/_index.md` (Confidence: `high`)
  *Reason: Capture services implementation and tool documentation.*
- `00_QiEOS/30_service_map/30_capture/nocodb.md` -> `40_QiCapture/nocodb.md` (Confidence: `high`)
  *Reason: Capture services implementation and tool documentation.*
- `00_QiEOS/30_service_map/30_capture/obsidian_qidocs.md` -> `40_QiCapture/obsidian_qidocs.md` (Confidence: `high`)
  *Reason: Capture services implementation and tool documentation.*
- `00_QiEOS/30_service_map/30_capture/paperless/_index.md` -> `40_QiCapture/_index.md` (Confidence: `high`)
  *Reason: Capture services implementation and tool documentation.*
- `00_QiEOS/30_service_map/30_capture/wikijs.md` -> `40_QiCapture/wikijs.md` (Confidence: `high`)
  *Reason: Capture services implementation and tool documentation.*
- `00_QiEOS/30_service_map/70_pipelines/_index.md` -> `40_QiCapture/_index.md` (Confidence: `medium`)
  *Reason: Ingestion and capture pipeline specifications.*

### Destination: `60_QiApps`
- `00_QiEOS/30_service_map/120_applications/CareLite/_index.md` -> `60_QiApps/_index.md` (Confidence: `high`)
  *Reason: Describes end-user applications and components.*
- `00_QiEOS/30_service_map/120_applications/_index.md` -> `60_QiApps/_index.md` (Confidence: `high`)
  *Reason: Describes end-user applications and components.*
- `00_QiEOS/30_service_map/120_applications/admin.md` -> `60_QiApps/admin.md` (Confidence: `high`)
  *Reason: Describes end-user applications and components.*
- `00_QiEOS/30_service_map/120_applications/carelite.md` -> `60_QiApps/carelite.md` (Confidence: `high`)
  *Reason: CareLite application documentation.*
- `00_QiEOS/30_service_map/120_applications/firefly.md` -> `60_QiApps/firefly.md` (Confidence: `high`)
  *Reason: Describes end-user applications and components.*
- `00_QiEOS/30_service_map/120_applications/portal.md` -> `60_QiApps/portal.md` (Confidence: `high`)
  *Reason: Describes end-user applications and components.*
- `00_QiEOS/30_service_map/120_applications/qinote/qinote_salvage_extract.md` -> `60_QiApps/qinote_salvage_extract.md` (Confidence: `high`)
  *Reason: Describes end-user applications and components.*
- `00_QiEOS/30_service_map/120_applications/roadmap.md` -> `60_QiApps/roadmap.md` (Confidence: `high`)
  *Reason: Describes end-user applications and components.*
- `00_QiEOS/30_service_map/130_GINA/_index.md` -> `60_QiApps/_index.md` (Confidence: `medium`)
  *Reason: GINA assistant/personality application documentation.*
- `00_QiEOS/30_service_map/40_productivity/_index.md` -> `60_QiApps/_index.md` (Confidence: `medium`)
  *Reason: Describes user productivity applications and workflow tools.*
- `00_QiEOS/30_service_map/40_productivity/activitywatch.md` -> `60_QiApps/activitywatch.md` (Confidence: `medium`)
  *Reason: Describes user productivity applications and workflow tools.*
- `00_QiEOS/30_service_map/40_productivity/qiledger.md` -> `60_QiApps/qiledger.md` (Confidence: `medium`)
  *Reason: Describes user productivity applications and workflow tools.*
- `00_QiEOS/30_service_map/40_productivity/solidtime.md` -> `60_QiApps/solidtime.md` (Confidence: `medium`)
  *Reason: Describes user productivity applications and workflow tools.*
- `00_QiEOS/40_operations/40_dev_testing/momscare/2026-05-17_momcare_app_qa_checklist.md` -> `60_QiApps/2026-05-17_momcare_app_qa_checklist.md` (Confidence: `high`)
  *Reason: Application QA testing checklist.*

### Destination: `70_QiConnect`
- `00_QiEOS/30_service_map/40_productivity/n8n.md` -> `70_QiConnect/n8n.md` (Confidence: `high`)
  *Reason: n8n is an external integration system, belongs in QiConnect.*
- `00_QiEOS/30_service_map/50_apis/_index.md` -> `70_QiConnect/_index.md` (Confidence: `medium`)
  *Reason: API services and integrations specifications.*
- `00_QiEOS/30_service_map/50_apis/portal_api.md` -> `70_QiConnect/portal_api.md` (Confidence: `medium`)
  *Reason: API services and integrations specifications.*
- `00_QiEOS/30_service_map/90_interfaces/_index.md` -> `70_QiConnect/_index.md` (Confidence: `medium`)
  *Reason: API and gateway interfaces specifications.*
- `00_QiEOS/30_service_map/90_interfaces/public_interfaces.md` -> `70_QiConnect/public_interfaces.md` (Confidence: `medium`)
  *Reason: API and gateway interfaces specifications.*

### Destination: `90_archive`
- `00_QiEOS/50_knowledge/50_legacy_salvage.md` -> `90_archive/50_legacy_salvage.md` [ARCHIVE] (Confidence: `high`)
  *Reason: Obsolete or superseded documentation files.*
- `00_QiEOS/50_knowledge/60_qiaccess_start_legacy_quarantine.md` -> `90_archive/60_qiaccess_start_legacy_quarantine.md` [ARCHIVE] (Confidence: `high`)
  *Reason: Obsolete or superseded documentation files.*
- `00_QiEOS/50_knowledge/90_superseded_sources/2025-11-18_qicodex_protocol_batch_overview.md` -> `90_archive/2025-11-18_qicodex_protocol_batch_overview.md` [ARCHIVE] (Confidence: `high`)
  *Reason: Obsolete or superseded documentation files.*
- `00_QiEOS/50_knowledge/90_superseded_sources/QiAccess_Start_Blueprint.md` -> `90_archive/QiAccess_Start_Blueprint.md` [ARCHIVE] (Confidence: `high`)
  *Reason: Obsolete or superseded documentation files.*
- `00_QiEOS/50_knowledge/90_superseded_sources/README.md` -> `90_archive/README.md` [ARCHIVE] (Confidence: `high`)
  *Reason: Obsolete or superseded documentation files.*
- `00_QiEOS/50_knowledge/90_superseded_sources/qi_os_home_blueprint.md` -> `90_archive/qi_os_home_blueprint.md` [ARCHIVE] (Confidence: `high`)
  *Reason: Obsolete or superseded documentation files.*
- `00_QiEOS/50_knowledge/90_superseded_sources/tech_stack_markmind.md` -> `90_archive/tech_stack_markmind.md` [ARCHIVE] (Confidence: `high`)
  *Reason: Obsolete or superseded documentation files.*

### Destination: `90_receipts`
- `00_QiEOS/40_operations/30_dev_history/2026-05-16_dev_session_directory_markmind_mapper.md` -> `90_receipts/2026-05-16_dev_session_directory_markmind_mapper.md` [ARCHIVE] (Confidence: `high`)
  *Reason: Historical development log, belongs in receipts/archives.*
- `00_QiEOS/90_receipts/10_changelog.md` -> `90_receipts/10_changelog.md` (Confidence: `high`)
  *Reason: Generated reports, checks, and logs.*
- `00_QiEOS/90_receipts/10_logs/_index.md` -> `90_receipts/_index.md` (Confidence: `high`)
  *Reason: Generated reports, checks, and logs.*
- `00_QiEOS/90_receipts/20_audits/_index.md` -> `90_receipts/_index.md` (Confidence: `high`)
  *Reason: Generated reports, checks, and logs.*
- `00_QiEOS/90_receipts/30_backups/_index.md` -> `90_receipts/_index.md` (Confidence: `high`)
  *Reason: Generated reports, checks, and logs.*
- `00_QiEOS/90_receipts/40_health_checks/_index.md` -> `90_receipts/_index.md` (Confidence: `high`)
  *Reason: Generated reports, checks, and logs.*
- `00_QiEOS/90_receipts/50_generated_reports/_index.md` -> `90_receipts/_index.md` (Confidence: `high`)
  *Reason: Generated reports, checks, and logs.*
- `00_QiEOS/90_receipts/50_generated_reports/current_project_state.md` -> `90_receipts/current_project_state.md` (Confidence: `high`)
  *Reason: Generated reports, checks, and logs.*
- `00_QiEOS/90_receipts/50_generated_reports/qilabs_structure_check.csv` -> `90_receipts/qilabs_structure_check.csv` (Confidence: `high`)
  *Reason: Generated reports, checks, and logs.*
- `00_QiEOS/90_receipts/50_generated_reports/qilabs_structure_check.json` -> `90_receipts/qilabs_structure_check.json` (Confidence: `high`)
  *Reason: Generated reports, checks, and logs.*
- `00_QiEOS/90_receipts/50_generated_reports/qilabs_structure_check.md` -> `90_receipts/qilabs_structure_check.md` (Confidence: `high`)
  *Reason: Generated reports, checks, and logs.*
- `00_QiEOS/90_receipts/60_generated_indexes/_index.md` -> `90_receipts/_index.md` (Confidence: `high`)
  *Reason: Generated reports, checks, and logs.*
- `00_QiEOS/90_receipts/70_maintenance/_index.md` -> `90_receipts/_index.md` (Confidence: `high`)
  *Reason: Generated reports, checks, and logs.*
- `00_QiEOS/90_receipts/Current_Project_State.md` -> `90_receipts/Current_Project_State.md` (Confidence: `high`)
  *Reason: Generated reports, checks, and logs.*
- `00_QiEOS/90_receipts/_audit/2026-05-24_qiaccess_homepage_conversion_report.md` -> `90_receipts/2026-05-24_qiaccess_homepage_conversion_report.md` (Confidence: `high`)
  *Reason: Generated reports, checks, and logs.*
- `00_QiEOS/90_receipts/_audit/2026-05-24_qiaccess_homepage_local_validation_report.md` -> `90_receipts/2026-05-24_qiaccess_homepage_local_validation_report.md` (Confidence: `high`)
  *Reason: Generated reports, checks, and logs.*
- `00_QiEOS/90_receipts/_audit/2026-05-24_qilinks_admin_and_visual_map_plan.md` -> `90_receipts/2026-05-24_qilinks_admin_and_visual_map_plan.md` (Confidence: `high`)
  *Reason: Generated reports, checks, and logs.*
- `00_QiEOS/90_receipts/_audit/qiaccess_map.md` -> `90_receipts/qiaccess_map.md` (Confidence: `high`)
  *Reason: Generated reports, checks, and logs.*
- `00_QiEOS/90_receipts/_audit/qiaccess_map.mmd` -> `90_receipts/qiaccess_map.mmd` (Confidence: `high`)
  *Reason: Generated reports, checks, and logs.*
- `00_QiEOS/exports/QiOS_DNA_Chronicle.md` -> `90_receipts/QiOS_DNA_Chronicle.md` (Confidence: `medium`)
  *Reason: Generated export artifacts.*
- `00_QiEOS/file-index.json` -> `90_receipts/file-index.json` (Confidence: `medium`)
  *Reason: Automatically generated index of files, belongs in receipts.*

### Destination: `Reconciliation`
- `00_QiEOS/50_knowledge/30_migration_notes.md` -> `Reconciliation/30_migration_notes.md` (Confidence: `high`)
  *Reason: Migration and sync reconciliation plans.*
- `00_QiEOS/50_knowledge/40_legacy_csv_migration_plan.md` -> `Reconciliation/40_legacy_csv_migration_plan.md` (Confidence: `high`)
  *Reason: Migration and sync reconciliation plans.*
- `00_QiEOS/50_knowledge/70_repo_sync_status_20260516.md` -> `Reconciliation/70_repo_sync_status_20260516.md` (Confidence: `high`)
  *Reason: Migration and sync reconciliation plans.*
- `00_QiEOS/reconciliation/2026-06-09_codex_reconciliation_brief.md` -> `Reconciliation/2026-06-09_codex_reconciliation_brief.md` (Confidence: `high`)
  *Reason: Active reconciliation audits and plans.*
- `00_QiEOS/reconciliation/2026-06-09_initial_reconciliation.mdx` -> `Reconciliation/2026-06-09_initial_reconciliation.mdx` (Confidence: `high`)
  *Reason: Active reconciliation audits and plans.*

### Destination: `assets`
- `00_QiEOS/60_assets/assets.md` -> `assets/assets.md` (Confidence: `high`)
  *Reason: Static assets, diagrams, images, and visual mapping documents.*
- `00_QiEOS/60_assets/diagrams/2026-05-17_supabase_markmind.md` -> `assets/2026-05-17_supabase_markmind.md` (Confidence: `high`)
  *Reason: Static assets, diagrams, images, and visual mapping documents.*
- `00_QiEOS/60_assets/diagrams/blueprint_map.md` -> `assets/blueprint_map.md` (Confidence: `high`)
  *Reason: Static assets, diagrams, images, and visual mapping documents.*
- `00_QiEOS/60_assets/diagrams/diagrams.md` -> `assets/diagrams.md` (Confidence: `high`)
  *Reason: Static assets, diagrams, images, and visual mapping documents.*
- `00_QiEOS/60_assets/diagrams/markmind-data.json` -> `assets/markmind-data.json` (Confidence: `high`)
  *Reason: Static assets, diagrams, images, and visual mapping documents.*
- `00_QiEOS/60_assets/diagrams/markmind.html` -> `assets/markmind.html` (Confidence: `high`)
  *Reason: Static assets, diagrams, images, and visual mapping documents.*
- `00_QiEOS/60_assets/images/_QiOS_Master_Document.jpg` -> `assets/_QiOS_Master_Document.jpg` (Confidence: `high`)
  *Reason: Static assets, diagrams, images, and visual mapping documents.*
- `00_QiEOS/60_assets/templates/2026-05-16_dev_session_template.md` -> `assets/2026-05-16_dev_session_template.md` (Confidence: `medium`)
  *Reason: General markdown or document templates.*
- `00_QiEOS/60_assets/templates/README.md` -> `assets/README.md` (Confidence: `high`)
  *Reason: Static assets, diagrams, images, and visual mapping documents.*
- `00_QiEOS/60_assets/templates/_index.md` -> `assets/_index.md` (Confidence: `high`)
  *Reason: Static assets, diagrams, images, and visual mapping documents.*
- `00_QiEOS/60_assets/templates/appendix_template.md` -> `assets/appendix_template.md` (Confidence: `medium`)
  *Reason: General markdown or document templates.*
- `00_QiEOS/60_assets/templates/artifact_template.md` -> `assets/artifact_template.md` (Confidence: `medium`)
  *Reason: General markdown or document templates.*
- `00_QiEOS/60_assets/templates/note_template.md` -> `assets/note_template.md` (Confidence: `medium`)
  *Reason: General markdown or document templates.*
- `00_QiEOS/60_assets/templates/operational_template.md` -> `assets/operational_template.md` (Confidence: `medium`)
  *Reason: General markdown or document templates.*
- `00_QiEOS/60_assets/templates/page_template.md` -> `assets/page_template.md` (Confidence: `medium`)
  *Reason: General markdown or document templates.*
- `00_QiEOS/60_assets/templates/templates.md` -> `assets/templates.md` (Confidence: `medium`)
  *Reason: General markdown or document templates.*

## 5. Ambiguous or Dual-Domain Files
- `00_QiEOS/30_service_map/100_integrations/_index.md` (Proposed: `00_QiEOS`)
  *Reason: Unclassified file.*
- `00_QiEOS/30_service_map/100_integrations/external_integrations.md` (Proposed: `00_QiEOS`)
  *Reason: Unclassified file.*
- `00_QiEOS/30_service_map/_index.md` (Proposed: `00_QiEOS`)
  *Reason: Unclassified file.*
- `00_QiEOS/40_operations/10_cases/_index.md` (Proposed: `20_QiSystem`)
  *Reason: Operational document requiring review.*
- `00_QiEOS/40_operations/20_qiserver/_index.md` (Proposed: `20_QiSystem`)
  *Reason: Operational document requiring review.*
- `00_QiEOS/40_operations/_index.md` (Proposed: `20_QiSystem`)
  *Reason: Operational document requiring review.*
