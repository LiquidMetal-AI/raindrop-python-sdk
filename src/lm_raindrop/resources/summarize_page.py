# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from ..types import summarize_page_create_params
from .._types import NOT_GIVEN, Body, Query, Headers, NotGiven
from .._utils import (
    maybe_transform,
    async_maybe_transform,
)
from .._compat import cached_property
from .._resource import SyncAPIResource, AsyncAPIResource
from .._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from .._base_client import make_request_options
from ..types.summarize_page_create_response import SummarizePageCreateResponse

__all__ = ["SummarizePageResource", "AsyncSummarizePageResource"]


class SummarizePageResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> SummarizePageResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/LiquidMetal-AI/raindrop-python-sdk#accessing-raw-response-data-eg-headers
        """
        return SummarizePageResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> SummarizePageResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/LiquidMetal-AI/raindrop-python-sdk#with_streaming_response
        """
        return SummarizePageResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        request_id: str,
        page: int | NotGiven = NOT_GIVEN,
        page_size: int | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> SummarizePageCreateResponse:
        """
        Generates intelligent summaries of search result pages, helping users quickly
        understand large result sets without reading through every document. The system
        analyzes the content of all results on a given page and generates a detailed
        overview.

        The summary system:

        - Identifies key themes and topics
        - Extracts important findings
        - Highlights document relationships
        - Provides content type distribution

        Args:
          request_id: Client-provided search session identifier from the original search

          page: Target page number (1-based)

          page_size: Results per page. Affects how many documents are included in the summary

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/v1/summarize_page",
            body=maybe_transform(
                {
                    "request_id": request_id,
                    "page": page,
                    "page_size": page_size,
                },
                summarize_page_create_params.SummarizePageCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=SummarizePageCreateResponse,
        )


class AsyncSummarizePageResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncSummarizePageResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/LiquidMetal-AI/raindrop-python-sdk#accessing-raw-response-data-eg-headers
        """
        return AsyncSummarizePageResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncSummarizePageResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/LiquidMetal-AI/raindrop-python-sdk#with_streaming_response
        """
        return AsyncSummarizePageResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        request_id: str,
        page: int | NotGiven = NOT_GIVEN,
        page_size: int | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> SummarizePageCreateResponse:
        """
        Generates intelligent summaries of search result pages, helping users quickly
        understand large result sets without reading through every document. The system
        analyzes the content of all results on a given page and generates a detailed
        overview.

        The summary system:

        - Identifies key themes and topics
        - Extracts important findings
        - Highlights document relationships
        - Provides content type distribution

        Args:
          request_id: Client-provided search session identifier from the original search

          page: Target page number (1-based)

          page_size: Results per page. Affects how many documents are included in the summary

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/v1/summarize_page",
            body=await async_maybe_transform(
                {
                    "request_id": request_id,
                    "page": page,
                    "page_size": page_size,
                },
                summarize_page_create_params.SummarizePageCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=SummarizePageCreateResponse,
        )


class SummarizePageResourceWithRawResponse:
    def __init__(self, summarize_page: SummarizePageResource) -> None:
        self._summarize_page = summarize_page

        self.create = to_raw_response_wrapper(
            summarize_page.create,
        )


class AsyncSummarizePageResourceWithRawResponse:
    def __init__(self, summarize_page: AsyncSummarizePageResource) -> None:
        self._summarize_page = summarize_page

        self.create = async_to_raw_response_wrapper(
            summarize_page.create,
        )


class SummarizePageResourceWithStreamingResponse:
    def __init__(self, summarize_page: SummarizePageResource) -> None:
        self._summarize_page = summarize_page

        self.create = to_streamed_response_wrapper(
            summarize_page.create,
        )


class AsyncSummarizePageResourceWithStreamingResponse:
    def __init__(self, summarize_page: AsyncSummarizePageResource) -> None:
        self._summarize_page = summarize_page

        self.create = async_to_streamed_response_wrapper(
            summarize_page.create,
        )
