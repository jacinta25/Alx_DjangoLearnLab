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


# Django Security Best Practices Implementation

## Security Settings
- `DEBUG = False`: Disables debugging in production.
- Browser security headers are set for XSS and clickjacking protection.
- Cookies are set to secure (sent only over HTTPS).
- HSTS is enabled for 1 year to prevent downgrade attacks.

## CSRF Protection
- All forms include `{% csrf_token %}` to protect against CSRF attacks.

## SQL Injection Prevention
- All user input is handled through Django's ORM to prevent SQL injection.
- User inputs are validated using Django forms.

## CSP Implementation
- CSP headers are set to limit the sources from which content can be loaded, reducing the risk of XSS attacks.

### Testing Approach:
- Test the application by attempting to inject malicious code or bypass security features (e.g., submitting forms without CSRF tokens).
- Ensure that input fields sanitize and validate user input correctly.

