# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from lm_raindrop import Raindrop, AsyncRaindrop
from tests.utils import assert_matches_type
from lm_raindrop.types import SummarizePageCreateResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestSummarizePage:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip()
    @parametrize
    def test_method_create(self, client: Raindrop) -> None:
        summarize_page = client.summarize_page.create(
            request_id="request_id",
        )
        assert_matches_type(SummarizePageCreateResponse, summarize_page, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_method_create_with_all_params(self, client: Raindrop) -> None:
        summarize_page = client.summarize_page.create(
            request_id="request_id",
            page=0,
            page_size=0,
        )
        assert_matches_type(SummarizePageCreateResponse, summarize_page, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_create(self, client: Raindrop) -> None:
        response = client.summarize_page.with_raw_response.create(
            request_id="request_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        summarize_page = response.parse()
        assert_matches_type(SummarizePageCreateResponse, summarize_page, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_create(self, client: Raindrop) -> None:
        with client.summarize_page.with_streaming_response.create(
            request_id="request_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            summarize_page = response.parse()
            assert_matches_type(SummarizePageCreateResponse, summarize_page, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncSummarizePage:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_create(self, async_client: AsyncRaindrop) -> None:
        summarize_page = await async_client.summarize_page.create(
            request_id="request_id",
        )
        assert_matches_type(SummarizePageCreateResponse, summarize_page, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncRaindrop) -> None:
        summarize_page = await async_client.summarize_page.create(
            request_id="request_id",
            page=0,
            page_size=0,
        )
        assert_matches_type(SummarizePageCreateResponse, summarize_page, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_create(self, async_client: AsyncRaindrop) -> None:
        response = await async_client.summarize_page.with_raw_response.create(
            request_id="request_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        summarize_page = await response.parse()
        assert_matches_type(SummarizePageCreateResponse, summarize_page, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncRaindrop) -> None:
        async with async_client.summarize_page.with_streaming_response.create(
            request_id="request_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            summarize_page = await response.parse()
            assert_matches_type(SummarizePageCreateResponse, summarize_page, path=["response"])

        assert cast(Any, response.is_closed) is True
