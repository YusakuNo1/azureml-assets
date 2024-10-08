# Copyright (c) Microsoft Corporation.
# Licensed under the MIT License.

"""This file contains the definition for the batch score input row completed event."""

from dataclasses import dataclass, field
from .batch_score_event import BatchScoreEvent

from .. import logging_utils as lu


# TODO: Add comments to describe each field
@dataclass
class BatchScoreInputRowCompletedEvent(BatchScoreEvent):
    """Defines the batch score input row completed event."""

    @property
    def name(self):
        """Get the name of the event."""
        return "BatchScore.InputRow.Completed"

    minibatch_id: str = field(init=True, default_factory=lu.get_mini_batch_id)
    input_row_id: str = field(init=True, default=None)
    node_id: str = field(init=True, default=None)
    process_id: str = field(init=True, default=None)
    worker_id: str = field(init=True, default_factory=lu.get_worker_id)
    scoring_url: str = field(init=True, default=None)
    is_successful: bool = field(init=True, default=None)
    response_code: int = field(init=True, default=None)
    prompt_tokens: int = field(init=True, default=None)
    completion_tokens: int = field(init=True, default=None)
    retry_count: int = field(init=True, default=None)
    duration_ms: float = field(init=True, default=None)
    segment_count: int = field(init=True, default=-1)

    """Input type classification for the request."""
    input_type: str = field(init=True, default=None)
