# Copyright (c) Microsoft Corporation.
# Licensed under the MIT License.

"""This file contains the unit tests for scoring client factory."""

import pytest

from src.batch_score_oss.aoai.scoring.aoai_scoring_client import AoaiScoringClient
from src.batch_score_oss.common.configuration.configuration_parser import ConfigurationParser
from src.batch_score_oss.common.scoring.scoring_client_factory import ScoringClientFactory


@pytest.mark.parametrize('scoring_url, expected_scoring_client_type', [
    ('serverless.models.ai.azure.com', AoaiScoringClient),
])
def test_create_success(mocker, make_metadata, scoring_url, expected_scoring_client_type):
    """Test create success."""
    # Arrange
    configuration = ConfigurationParser().parse_configuration([
        '--scoring_url', scoring_url
    ])

    # Act
    scoring_client = ScoringClientFactory().setup_scoring_client(
        configuration=configuration,
        metadata=make_metadata,
        token_provider=mocker.MagicMock())

    # Assert
    assert isinstance(scoring_client, expected_scoring_client_type)
