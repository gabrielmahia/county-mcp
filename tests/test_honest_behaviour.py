from county_mcp import server

_fn = lambda name: (getattr(server, name).fn if hasattr(getattr(server, name), "fn") else getattr(server, name))


def test_an_unknown_county_gets_no_invented_budget_figure():
    r = _fn("county_budget_guide")("Atlantis")
    assert r["equitable_share_kes_million"] is None and r["equitable_share_basis"] == "no data for this county"
    assert _fn("county_budget_guide")("Nairobi")["equitable_share_basis"] == "sample table"


def test_an_unknown_county_contact_is_marked_unverified_not_presented_as_real():
    r = _fn("county_contact_directory")("Atlantis")["contact"]
    assert r["verified"] is False and "guess" in r["note"]
