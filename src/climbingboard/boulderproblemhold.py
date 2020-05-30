from climbingboard.hold import Hold
from climbingboard.holdkind import HoldKind
from climbingboard.position import Position


class BoulderProblemHold(Hold):
    kind: HoldKind

    def __init__(self, name: str, position: Position, kind: HoldKind):
        super().__init__(name, position)
        self.kind = kind

    def __repr__(self):
        return f" {self.name} ({self.position.x},{self.position.y}) {self.kind}"

    @property
    def _cmpkey(self) -> int:
        return super()._cmpkey + self.kind.value
