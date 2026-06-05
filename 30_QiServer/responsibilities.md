# QiServer Responsibilities

QiServer is responsible for:

- Hosting protected runtime services.
- Keeping runtime stack paths and service facts clear.
- Separating public restricted access from private-only access.
- Running Docker Compose stacks and systemd services.
- Supporting QiAccess Start, Wiki.js, Paperless, Open WebUI, Ollama, NocoDB, Qdrant, Neo4j, Uptime Kuma, SolidTime, n8n, BookStack, QI TTS, and related services.
- Verifying local, tailnet, and public routes after changes.

QiServer is not responsible for:

- Defining QiLife product behavior.
- Owning QiNexus folder taxonomy.
- Holding doctrine.
- Replacing source repositories.
