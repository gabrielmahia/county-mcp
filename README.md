# county-mcp
<!-- mcp-name: io.github.gabrielmahia/county-mcp -->

[![county-mcp Glama score](https://glama.ai/mcp/servers/gabrielmahia/county-mcp/badges/score.svg)](https://glama.ai/mcp/servers/gabrielmahia/county-mcp)
[![smithery badge](https://smithery.ai/badge/@gabrielmahia/county-mcp)](https://smithery.ai/server/@gabrielmahia/county-mcp)


---
**Compatible with `claude-sonnet-5`** (released 2026-06-30) — Anthropic's most agentic
Sonnet yet. Runs multi-step tool chains end-to-end without stopping short.
Install: `pip install county-mcp` · Use with any MCP client.

---


> Kenya 47-county local government data via MCP.

[![PyPI](https://img.shields.io/badge/PyPI-v0.1.0-blue?logo=pypi)](https://pypi.org/project/county-mcp/)
[![Thesis Layer](https://img.shields.io/badge/Thesis_Layer-L9_Civic_Infrastructure-orange)](https://gabrielmahia.github.io/nairobi-stack)

## Install
```bash
pip install county-mcp
```

## Tools (6) — All 47 counties covered
| Tool | Description |
|------|-------------|
| `county_information` | Demographics, area, wards, constituencies for all 47 counties |
| `county_budget_guide` | Devolution funding, equitable share, own-source revenue |
| `county_services_guide` | What services are provided at county vs national level |
| `cdf_guide` | Constituency Development Fund — bursaries, project proposals |
| `ward_information` | MCA role, ward development fund, how to petition county assembly |
| `county_contact_directory` | County government websites, governor offices, assembly contacts |

→ [The Nairobi Stack](https://gabrielmahia.github.io/nairobi-stack)

## License
MIT © Gabriel Mahia | contact@aikungfu.dev

## Part of the East Africa Coordination Stack

This MCP server is one of 32 tools in the Kenya coordination infrastructure.
It connects to [`africa-coord-bus`](https://github.com/gabrielmahia/africa-coord-bus) — the coordination
event bus that routes signals between domains automatically.

When this server detects a threshold condition, the bus notifies:
- `bima-mcp` — parametric insurance evaluation
- `kilimo-mcp` — agricultural advisory
- `afya-mcp` — health surveillance activation
- `county-mcp` — county office alert

```python
pip install africa-coord-bus
```

All servers: [pypi.org/user/gmahia](https://pypi.org/user/gmahia/)

## IP & Collaboration

MIT licensed. Feedback via GitHub Issues only — pull requests are not accepted. Demo data is labeled DEMO and is not suitable for operational decisions. Full policy: [docs/architecture/IP_POLICY.md](docs/architecture/IP_POLICY.md). Security reports: see [SECURITY.md](SECURITY.md).
