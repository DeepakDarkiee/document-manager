from bridger.menus import ItemPermission, Menu, MenuItem, default_registry

default_app_config = "documents.apps.DocumentsConfig"

default_registry.alphabetical_sorted = True
default_registry.register(
    Menu(
        label="Views",
        items=[
            Menu(
                label="Sub Views",
                items=[
                    MenuItem(
                        label="Documents",
                        endpoint="documents-list",
                        add=MenuItem(label="Add Documents", endpoint="documents-list"),
                    ),
                ],
            ),
            MenuItem(
                label="DocumentType",
                endpoint="type-list",
                add=MenuItem(label="Add DocumentType", endpoint="type-list"),
            ),
        ],
        index=1,
    ),
)


# default_registry.register(
#     Menu(
#         label="Menu1",
#         items=[
#             MenuItem(label="ToDo", endpoint="todo-list"),
#             MenuItem(label="Category", endpoint="category-list"),
#         ],
#     )
# )

# default_registry.register(
#     Menu(
#         label="Menu2",
#         items=[
#             MenuItem(
#                 label="MenuItem3",
#                 endpoint="app:endpoint3",
#                 permission=ItemPermission(method=lambda request: request.user.is_active),
#             ),
#             MenuItem(
#                 label="MenuItem4",
#                 endpoint="app:endpoint4",
#                 add=MenuItem(label="Add MenuItem4", endpoint="app:endpoint4"),
#             ),
#         ],
#     )
# )
