"""
Example: Custom Snapshot Name
"""
import pytest

from syrupy.extensions.amber import AmberSnapshotExtension
from syrupy.types import SnapshotIndex


class CanadianNameExtension(AmberSnapshotExtension):
    def get_snapshot_name(self, *, index: "SnapshotIndex") -> str:
        original_name = super(CanadianNameExtension, self).get_snapshot_name(
            index=index
        )
        return f"{original_name}🇨🇦"


@pytest.fixture
def snapshot(snapshot):
    return snapshot.use_extension(CanadianNameExtension)


def test_canadian_name(snapshot):
    assert "Name should be test_canadian_name🇨🇦." == snapshot
