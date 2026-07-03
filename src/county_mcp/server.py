"""CountyMCP — Kenya 47 Counties Local Government Data (6 tools). All data DEMO."""
from __future__ import annotations
from typing import Annotated, Optional
from fastmcp import FastMCP
mcp = FastMCP(name="county-mcp", instructions="Kenya 47 counties local government data. DEMO.")

COUNTIES = {
    "Nairobi": {"code": 47, "pop": 4397073, "area_km2": 695.1, "region": "Nairobi", "wards": 85, "constituencies": 17},
    "Mombasa": {"code": 1, "pop": 1208333, "area_km2": 229.9, "region": "Coast", "wards": 30, "constituencies": 6},
    "Kwale": {"code": 2, "pop": 866820, "area_km2": 8270.3, "region": "Coast", "wards": 20, "constituencies": 4},
    "Kilifi": {"code": 3, "pop": 1453787, "area_km2": 12245.9, "region": "Coast", "wards": 35, "constituencies": 7},
    "Tana River": {"code": 4, "pop": 315943, "area_km2": 35375.8, "region": "Coast", "wards": 15, "constituencies": 3},
    "Lamu": {"code": 5, "pop": 143920, "area_km2": 6497.7, "region": "Coast", "wards": 10, "constituencies": 2},
    "Taita-Taveta": {"code": 6, "pop": 340671, "area_km2": 17083.9, "region": "Coast", "wards": 20, "constituencies": 4},
    "Garissa": {"code": 7, "pop": 841353, "area_km2": 44175.9, "region": "North Eastern", "wards": 20, "constituencies": 6},
    "Wajir": {"code": 8, "pop": 661941, "area_km2": 56685.8, "region": "North Eastern", "wards": 25, "constituencies": 6},
    "Mandera": {"code": 9, "pop": 867457, "area_km2": 25797.3, "region": "North Eastern", "wards": 30, "constituencies": 6},
    "Marsabit": {"code": 10, "pop": 459785, "area_km2": 70961.2, "region": "Eastern", "wards": 20, "constituencies": 4},
    "Isiolo": {"code": 11, "pop": 268002, "area_km2": 25336.1, "region": "Eastern", "wards": 9, "constituencies": 2},
    "Meru": {"code": 12, "pop": 1545714, "area_km2": 6936.2, "region": "Eastern", "wards": 45, "constituencies": 9},
    "Tharaka-Nithi": {"code": 13, "pop": 393177, "area_km2": 2609.4, "region": "Eastern", "wards": 15, "constituencies": 3},
    "Embu": {"code": 14, "pop": 608599, "area_km2": 2818.2, "region": "Eastern", "wards": 25, "constituencies": 4},
    "Kitui": {"code": 15, "pop": 1136187, "area_km2": 24385.1, "region": "Eastern", "wards": 40, "constituencies": 8},
    "Machakos": {"code": 16, "pop": 1421932, "area_km2": 6208.2, "region": "Eastern", "wards": 40, "constituencies": 8},
    "Makueni": {"code": 17, "pop": 987653, "area_km2": 8008.9, "region": "Eastern", "wards": 30, "constituencies": 6},
    "Nyandarua": {"code": 18, "pop": 638289, "area_km2": 3304.7, "region": "Central", "wards": 25, "constituencies": 5},
    "Nyeri": {"code": 19, "pop": 759164, "area_km2": 3337.1, "region": "Central", "wards": 35, "constituencies": 7},
    "Kirinyaga": {"code": 20, "pop": 610411, "area_km2": 1478.1, "region": "Central", "wards": 20, "constituencies": 5},
    "Muranga": {"code": 21, "pop": 1056640, "area_km2": 2558.8, "region": "Central", "wards": 30, "constituencies": 7},
    "Kiambu": {"code": 22, "pop": 2417735, "area_km2": 2543.5, "region": "Central", "wards": 60, "constituencies": 12},
    "Turkana": {"code": 23, "pop": 926976, "area_km2": 77000.0, "region": "Rift Valley", "wards": 45, "constituencies": 6},
    "West Pokot": {"code": 24, "pop": 512690, "area_km2": 9169.4, "region": "Rift Valley", "wards": 20, "constituencies": 4},
    "Samburu": {"code": 25, "pop": 310327, "area_km2": 20182.5, "region": "Rift Valley", "wards": 15, "constituencies": 3},
    "Trans Nzoia": {"code": 26, "pop": 990341, "area_km2": 2495.5, "region": "Rift Valley", "wards": 25, "constituencies": 5},
    "Uasin Gishu": {"code": 27, "pop": 1163186, "area_km2": 3345.2, "region": "Rift Valley", "wards": 30, "constituencies": 6},
    "Elgeyo-Marakwet": {"code": 28, "pop": 454480, "area_km2": 3030.4, "region": "Rift Valley", "wards": 20, "constituencies": 4},
    "Nandi": {"code": 29, "pop": 885711, "area_km2": 2884.5, "region": "Rift Valley", "wards": 25, "constituencies": 6},
    "Baringo": {"code": 30, "pop": 666763, "area_km2": 11075.3, "region": "Rift Valley", "wards": 30, "constituencies": 6},
    "Laikipia": {"code": 31, "pop": 518560, "area_km2": 9462.5, "region": "Rift Valley", "wards": 25, "constituencies": 3},
    "Nakuru": {"code": 32, "pop": 2162202, "area_km2": 7495.1, "region": "Rift Valley", "wards": 55, "constituencies": 11},
    "Narok": {"code": 33, "pop": 1157873, "area_km2": 17933.1, "region": "Rift Valley", "wards": 30, "constituencies": 6},
    "Kajiado": {"code": 34, "pop": 1117840, "area_km2": 21901.1, "region": "Rift Valley", "wards": 25, "constituencies": 5},
    "Kericho": {"code": 35, "pop": 901777, "area_km2": 2454.5, "region": "Rift Valley", "wards": 30, "constituencies": 6},
    "Bomet": {"code": 36, "pop": 857823, "area_km2": 1997.1, "region": "Rift Valley", "wards": 25, "constituencies": 5},
    "Kakamega": {"code": 37, "pop": 1867579, "area_km2": 3033.8, "region": "Western", "wards": 60, "constituencies": 12},
    "Vihiga": {"code": 38, "pop": 590013, "area_km2": 563.3, "region": "Western", "wards": 25, "constituencies": 5},
    "Bungoma": {"code": 39, "pop": 1670570, "area_km2": 3032.2, "region": "Western", "wards": 45, "constituencies": 9},
    "Busia": {"code": 40, "pop": 893681, "area_km2": 1695.4, "region": "Western", "wards": 35, "constituencies": 7},
    "Siaya": {"code": 41, "pop": 993183, "area_km2": 2530.5, "region": "Nyanza", "wards": 30, "constituencies": 6},
    "Kisumu": {"code": 42, "pop": 1155574, "area_km2": 2085.9, "region": "Nyanza", "wards": 35, "constituencies": 7},
    "Homa Bay": {"code": 43, "pop": 1131950, "area_km2": 3154.7, "region": "Nyanza", "wards": 40, "constituencies": 8},
    "Migori": {"code": 44, "pop": 1116436, "area_km2": 2586.4, "region": "Nyanza", "wards": 35, "constituencies": 8},
    "Kisii": {"code": 45, "pop": 1266860, "area_km2": 1317.6, "region": "Nyanza", "wards": 45, "constituencies": 9},
    "Nyamira": {"code": 46, "pop": 605576, "area_km2": 899.3, "region": "Nyanza", "wards": 25, "constituencies": 4},
}

@mcp.tool(name="county_information", description="Kenya county demographics and basic statistics. DEMO.", annotations={"readOnlyHint": True, "openWorldHint": False})
def county_information(county: Annotated[Optional[str], "Name of a Kenya county e.g."] = None, region: Annotated[Optional[str], "Region filter:"] = None) -> dict:
    if county:
        c = county.title()
        info = COUNTIES.get(c)
        if info:
            return {"source": "DEMO — KNBS 2019 Census", "county": c, **info,
                    "county_code": info["code"],
                    "government": f"county.go.ke (each county has a website at [county].go.ke)"}
        return {"error": f"County '{county}' not found", "available": list(COUNTIES.keys())}
    if region:
        counties = {k: v for k, v in COUNTIES.items() if v["region"].lower() == region.lower()}
        return {"source": "DEMO", "region": region, "counties": counties, "count": len(counties)}
    return {"source": "DEMO — KNBS 2019 Census", "all_counties": {k: {"code": v["code"], "pop": v["pop"], "region": v["region"]} for k, v in COUNTIES.items()},
            "total": 47, "regions": list(set(v["region"] for v in COUNTIES.values()))}

@mcp.tool(name="county_budget_guide", description="Kenya county devolution and budget information. DEMO.", annotations={"readOnlyHint": True, "openWorldHint": False})
def county_budget_guide(county: Annotated[Optional[str], "Kenya county name e.g."] = None) -> dict:
    """Return budget allocation, development fund, and financial accountability data for a Kenya county."""
    # Rough equitable share allocations (DEMO - based on 2024/25 estimates)
    BUDGETS = {
        "Nairobi": 17800, "Nakuru": 8200, "Kiambu": 8100, "Kakamega": 7900, "Meru": 7100,
        "Turkana": 9800, "Marsabit": 8500, "Garissa": 8100, "Wajir": 7900, "Mandera": 8600,
    }
    if county:
        c = county.title()
        budget = BUDGETS.get(c, 5000)  # default estimate
        return {"source": "DEMO — Controller of Budget Kenya", "county": c,
                "equitable_share_kes_million": budget,
                "own_source_revenue": "Counties collect property rates, business permits, market fees, etc.",
                "devolved_functions": ["Health services", "Pre-primary education", "County roads", "Agriculture", "Trade"],
                "budget_documents": "Each county publishes Annual Development Plan and Budget at county.go.ke",
                "controller_of_budget": "cob.go.ke — oversees all county budgets",
                "disclaimer": "DEMO figures. Actual allocations from National Treasury vary annually."}
    return {"source": "DEMO — Controller of Budget Kenya",
            "how_counties_funded": {
                "equitable_share": "At least 15% of national revenue shared by formula (population, land area, poverty, fiscal responsibility)",
                "own_source": "Counties collect local revenue (permits, rates, fees)",
                "conditional_grants": "National government grants for specific programs",
            },
            "oversight": "Controller of Budget (cob.go.ke) + County Assembly",
            "total_devolution_budget_2025": "~KES 400 billion across 47 counties",
            "cdf": "CDF (Constituency Development Fund) is separate from county — managed by MPs. cdf.go.ke"}

@mcp.tool(name="county_services_guide", description="Services available at Kenya county government level. DEMO.", annotations={"readOnlyHint": True, "openWorldHint": False})
def county_services_guide(service: Annotated[Optional[str], "Service category e.g."] = None) -> dict:
    """List and describe devolved government services available at county level in Kenya."""
    SERVICES = {
        "health": "Primary health facilities (dispensaries, health centres), referral system to national hospitals",
        "water": "Rural water supply, borehole maintenance (county and national shared mandate)",
        "roads": "County roads maintenance (national roads by Kenya Roads Authority)",
        "markets": "Market infrastructure, market fees collection",
        "permits": "Business permits, building permits, health certificates",
        "agriculture": "Agricultural extension services, county demonstration farms",
        "education": "Pre-primary (ECDE) schools and ECD teachers",
        "environment": "Solid waste management, local environmental regulations",
        "trade": "County trade facilitation, hawker licensing",
        "id_services": "National ID is a national government function. Physical address can be done at sub-county offices.",
    }
    if service:
        s = service.lower()
        matched = {k: v for k, v in SERVICES.items() if k in s or s in k or s in v.lower()}
        return {"source": "DEMO — County Governments Act 2012", "service": service, "info": matched or SERVICES}
    return {"source": "DEMO — County Governments Act 2012", "devolved_services": SERVICES,
            "national_services": "National ID, passport, KRA, land titles — national government",
            "contact": "Visit your sub-county office. Directory at county.go.ke"}

@mcp.tool(name="cdf_guide", description="Kenya Constituency Development Fund (CDF) guide. DEMO.", annotations={"readOnlyHint": True, "openWorldHint": False})
def cdf_guide() -> dict:
    return {"source": "DEMO — CDF Act 2013 (Kenya)", "what_is_cdf":
            "Constituency Development Fund allocates 2.5% of national revenue to 290 constituencies for development projects.",
            "how_it_works": {
                "amount": "Each constituency gets KES 100-200M+ annually (varies by allocation formula)",
                "managed_by": "Constituency Development Fund Committee, chaired by area MP",
                "funded_projects": ["Bursaries (primary education focus)", "Classroom construction", "Health centres", "Water projects", "Roads", "Sports facilities"],
                "bursary": "CDF bursaries for needy students. Apply at constituency office during school term. Usually KES 5,000–20,000 per student.",
            },
            "how_to_access": {
                "bursary": "Collect form from MP's office or constituency office. Provide: admission letter, fee statement, ID (guardian). Apply before deadlines.",
                "project_proposal": "Submit community project proposals to CDF committee in your constituency",
                "contact": "cdf.go.ke | Your area MP's office",
            },
            "accountability": "CDF accounts must be audited. Misuse is a criminal offence under the CDF Act.",
            "portal": "cdf.go.ke"}

@mcp.tool(name="ward_information", description="Kenya ward-level civic information and ward representative role. DEMO.", annotations={"readOnlyHint": True, "openWorldHint": False})
def ward_information(county: Annotated[Optional[str], "Kenya county name e.g."] = None) -> dict:
    """Return ward and constituency breakdown for a Kenya county."""
    return {"source": "DEMO — IEBC Kenya", "what_is_ward":
            "Kenya is divided into 1,450 wards (sub-units of constituencies). Each ward elects a Member of County Assembly (MCA).",
            "mca_role": {
                "legislative": "Passes county legislation. Approves county budget.",
                "oversight": "Oversees county governor and executive.",
                "ward_development": "Ward Development Fund — small development budget for projects in the ward.",
                "bursary": "Some MCAs have ward bursary funds similar to CDF. Inquire at ward office.",
            },
            "ward_development_fund": "Each MCA ward gets KES 5-10M annually for development projects.",
            "how_to_reach_mca": "Visit your ward office. MCA contact via county assembly website or IEBC portal.",
            "county_assembly": f"County assembly for {county or 'any county'} handles legislation and petitions. Visit county.go.ke",
            "petition_mca": "Citizens can petition the county assembly on any matter affecting their county.",
            "iebc": "iebc.or.ke — find your ward, constituency, and county representatives"}

@mcp.tool(name="county_contact_directory", description="Kenya county government contact directory. DEMO.", annotations={"readOnlyHint": True, "openWorldHint": False})
def county_contact_directory(county: Annotated[Optional[str], "Kenya county name e.g."] = None) -> dict:
    """Return official contact information for Kenya county government offices."""
    CONTACTS = {
        "Nairobi": {"website": "nairobi.go.ke", "governor_office": "0800720007", "county_assembly": "nairobica.go.ke"},
        "Mombasa": {"website": "mombasa.go.ke", "governor_office": "041-2492022", "county_assembly": "mombasacountyassembly.go.ke"},
        "Kisumu": {"website": "kisumu.go.ke", "governor_office": "057-2022000", "county_assembly": "kisumucountyassembly.go.ke"},
        "Nakuru": {"website": "nakuru.go.ke", "governor_office": "051-2212888", "county_assembly": "nakuruca.go.ke"},
        "Kiambu": {"website": "kiambu.go.ke", "governor_office": "0725-000100", "county_assembly": "kiambu.go.ke/county-assembly"},
    }
    if county:
        c = county.title()
        info = CONTACTS.get(c, {"website": f"{c.lower().replace(' ','')}.go.ke", "note": "All 47 counties have websites at [countyname].go.ke"})
        return {"source": "DEMO", "county": c, "contact": info}
    return {"source": "DEMO", "contacts": CONTACTS,
            "general_pattern": "All counties: [countyname].go.ke (e.g. nakuru.go.ke, kisumu.go.ke)",
            "county_assembly_pattern": "[countyname]ca.go.ke or [countyname].go.ke/county-assembly",
            "all_contacts": "kenya.go.ke/counties | 47counties.go.ke"}
