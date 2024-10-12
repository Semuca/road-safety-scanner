"""Header class for the results table."""

from typing import Callable, Self

from PySide6.QtCore import QRect, Qt
from PySide6.QtGui import QMouseEvent, QPainter
from PySide6.QtWidgets import (
    QHeaderView,
    QWidget,
)


class ResultsTableHeader(QHeaderView):
    """Custom header class for the results table."""

    def __init__(self: Self, orientation: Qt.Orientation, parent: QWidget,
                 on_clicked:Callable[[int], None] = lambda: None) -> None:
        """Initialize the custom header."""
        super().__init__(orientation, parent)
        self.setSectionsClickable(True)

        self.on_clicked = on_clicked

    def paintSection(self: Self, painter: QPainter, rect: QRect, # noqa: N802
                     logical_index: int) -> None: 
        """Paint the section of the header."""
        super().paintSection(painter, rect, logical_index)

    def mouseReleaseEvent(self: Self, event: QMouseEvent) -> None: # noqa: N802
        """Handle the mouse release event."""
        super().mouseReleaseEvent(event)
        self.on_clicked(self.logicalIndexAt(event.position().toPoint()))