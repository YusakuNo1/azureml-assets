# Copyright (c) Microsoft Corporation.
# Licensed under the MIT License.

"""This file contains unit tests for prompt redaction modifier."""

import pytest

from src.batch_score_oss.common.request_modification.modifiers.prompt_redaction_modifier import (
    PromptRedactionModifier,
)

messages = [
    {
        "role": "system",
        "content": "You are a helpful assistant.",
    },
    {
        "role": "user",
        "content": "Hello!",
    }
]
test_cases = [
    [
        {"prompt": "Hello world"},
        {"prompt": "REDACTED"},
    ],
    [
        {"messages": messages},
        {"messages": "REDACTED"},
    ],
    [
        {
            "prompt": "Hello world",
            "messages": messages,
        },
        {
            "prompt": "REDACTED",
            "messages": "REDACTED",
        },
    ],
    [
        {
            "prompt": "Hello world",
            "messages": messages,
            "max_tokens": 50,
        },
        {
            "prompt": "REDACTED",
            "messages": "REDACTED",
            "max_tokens": 50,
        },
    ],
]


@pytest.mark.parametrize(
    "mock_get_logger, request_obj, redacted_request_obj",
    [['mock_get_logger', *test] for test in test_cases],
    indirect=['mock_get_logger'],
)
def test_modify(mock_get_logger, request_obj, redacted_request_obj):
    """Test modify."""
    prompt_redaction_modifier: PromptRedactionModifier = PromptRedactionModifier()
    modified_request_obj = prompt_redaction_modifier.modify(request_obj=request_obj)

    assert modified_request_obj == redacted_request_obj
