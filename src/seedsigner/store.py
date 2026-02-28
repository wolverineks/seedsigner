class Store:
    def __init__(self):
        self.state = {}
        self.dirty = False

    def set_state(self, new_state):
        self.state.update(new_state)
        self.dirty = True

    def has_changed(self):
        dirty = self.dirty
        self.dirty = False
        return dirty

    def hasnt_changed(self):
        return not self.has_changed()


store = Store()
# def connect(screen_class):
#     def wrapper(store, dispatch, router):
#         return screen_class(
#             props={
#                 "foo": store.state.get("foo"),
#                 "on_delete": lambda: dispatch({"type": "DELETE_FOO"}),
#             },
#             router=router,
#         )

#     return wrapper
