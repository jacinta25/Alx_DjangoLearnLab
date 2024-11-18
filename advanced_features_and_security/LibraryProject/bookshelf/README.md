# Django Permissions and Groups Implementation

## Overview
This Django application demonstrates how to implement permissions and groups to restrict access to specific parts of the application.

### Custom Permissions
The `Book` model has the following custom permissions:
- `can_view`: Allows users to view books.
- `can_create`: Allows users to create new books.
- `can_edit`: Allows users to edit existing books.
- `can_delete`: Allows users to delete books.

### Groups and Permissions
The following groups are defined:
- **Viewers**: Can only view books (`can_view`).
- **Editors**: Can view and create books (`can_view`, `can_create`).
- **Admins**: Can view, create, edit, and delete books (`can_view`, `can_create`, `can_edit`, `can_delete`).

### Testing
- **Test Users**: Create test users and assign them to the appropriate groups.
- **Access Control**: Each view enforces the appropriate permissions using `@permission_required`.
