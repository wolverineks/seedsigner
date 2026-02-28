from typing import Any, Generic, TypeVar


RouteT = TypeVar("RouteT", bound=str)


class LoopyRouter(Generic[RouteT]):
    def __init__(
        self,
        routes: tuple[RouteT, ...],
        initial_route: RouteT,
    ):
        self.routes = routes
        self.stack = [initial_route]
        self.dirty = True
        self.mounted: list[RouteT] = []
        self.unmounted: list[RouteT] = []
        self.focused: list[RouteT] = []
        self.blurred: list[RouteT] = []

    @property
    def changes(self):
        changes = (
            self.mounted,
            self.unmounted,
            self.focused,
            self.blurred,
        )
        self.dirty = False
        self.mounted = []
        self.unmounted = []
        self.focused = []
        self.blurred = []
        return changes

    def has_changed(self):
        return self.dirty

    def hasnt_changed(self):
        return not self.has_changed()

    def navigate_to(self, route: RouteT, *params: Any):
        self.dirty = True
        self.blurred.append(self.stack[-1])
        if route in self.routes:
            self.mounted.append(route)
            self.focused.append(route)
            self.stack.append(route)
        else:
            self.mounted.append("not_found")  # type: ignore
            self.focused.append("not_found")  # type: ignore
            self.stack.append("not_found")  # type: ignore
            print(f"Route {route} not found")

    def go_back(self):
        if len(self.stack) > 1:
            self.dirty = True
            self.blurred.append(self.stack[-1])
            self.unmounted.append(self.stack[-1])
            self.focused.append(self.stack[-2])
            self.stack.pop()
        else:
            print("Cannot pop the last screen")

    @property
    def current_route(self):
        return self.stack[-1]
