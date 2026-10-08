# county-mcp
<!-- mcp-name: io.github.gabrielmahia/county-mcp -->

## Why This Exists

Kenya's 2010 Constitution devolved substantial budget and service delivery to 47 counties, but county-level demographics, budgets, ward structures and contacts are published inconsistently across 47 different sites. Devolution only works if citizens can actually see what their county controls.

## Install

```bash
pip install county-mcp
```

## Tools (6)

- **`county_information`** —   
  <sub>args: county, region</sub>
- **`county_budget_guide`** — Return budget allocation, development fund, and financial accountability data for a Kenya county.  
  <sub>args: county</sub>
- **`county_services_guide`** — List and describe devolved government services available at county level in Kenya.  
  <sub>args: service</sub>
- **`cdf_guide`** —   
  <sub>args: no arguments</sub>
- **`ward_information`** — Return ward and constituency breakdown for a Kenya county.  
  <sub>args: county</sub>
- **`county_contact_directory`** — Return official contact information for Kenya county government offices.  
  <sub>args: county</sub>

## Example

```python
from county_mcp.server import county_information

result = county_information(county='Kiambu')
# demographics, budget allocation, services, contacts
```

## Claude Desktop Integration

Add to `claude_desktop_config.json`:

```json
{
  "mcpServers": {
    "county-mcp": {
      "command": "python",
      "args": ["-m", "county_mcp.server"]
    }
  }
}
```

## Data & Disclaimers

County figures are reference data compiled from public sources. Budgets change each fiscal year — verify against the Controller of Budget (cob.go.ke) and the county's own publications.

Every tool response carries a `source` field. Responses labelled `DEMO` are
illustrative reference data, not a live feed — verify against the authority
named in the response before acting on it.

## Part of the East Africa Coordination Stack

This MCP server is part of the Kenya coordination infrastructure.
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

<!-- interconnect:v1 -->
## Part of the East Africa coordination stack

- **Install & run:** `pip install reli-cli && reli list` — the MCP servers on the [official MCP Registry](https://registry.modelcontextprotocol.io) under `io.github.gabrielmahia`
- **Evaluate any model on Swahili agent tasks:** [kipimo](https://github.com/gabrielmahia/kipimo) · [dataset](https://huggingface.co/datasets/gmahia/kipimo) · [leaderboard](https://huggingface.co/spaces/gmahia/kipimo-leaderboard)
- **Coordinate across servers:** [africa-coord-bus](https://pypi.org/project/africa-coord-bus/) — offline-first event bus with a built-in Kenya routing table
- **Datasets:** [huggingface.co/gmahia](https://huggingface.co/gmahia) · **Docs hub:** [nairobi-stack](https://github.com/gabrielmahia/nairobi-stack)

Model-agnostic by design: closed APIs, open-weight models, and small distilled models are all first-class citizens.
<!-- /interconnect:v1 -->
