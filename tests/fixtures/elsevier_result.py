"""Fixtures for Elsevier search results."""

from urllib.request import Request

from modules.journal_downloader.query_elsevier import QueryElsevierResult

SEARCH_RESULTS = [QueryElsevierResult(
    f"doi{i}", f"title{i}", f"creator{i}", f"coverDisplayDate{i}")
    for i in range(1, 11)]

def assert_requests_are_equal(request1: Request, request2: Request) -> None:
    """Assert that two requests are equal."""
    assert request1.full_url == request2.full_url
    assert request1.headers == request2.headers