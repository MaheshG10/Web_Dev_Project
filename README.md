# Django CRUD Application

## Features
- Add, view, edit, and delete items.

- ## Models

| **Field Name**  | **Type**       | **Description**          |
|------------------|----------------|--------------------------|
| `name`          | `CharField`    | Name of the item         |
| `description`   | `TextField`    | Description of the item  |
| `created_at`    | `DateTimeField` | Auto-generated timestamp |
| `updated_at`    | `DateTimeField` | Auto-updated timestamp   |

- ## Views

| **View Name**       | **Type**       | **URL Pattern**       | **Template**                 | **Description**                       |
|----------------------|----------------|-----------------------|------------------------------|---------------------------------------|
| `ItemListView`       | `ListView`     | `/`                   | `item_list.html`             | Displays a list of all items          |
| `ItemCreateView`     | `CreateView`   | `/add/`               | `item_form.html`             | Allows users to create a new item     |
| `ItemUpdateView`     | `UpdateView`   | `/<int:pk>/edit/`     | `item_form.html`             | Allows users to edit an existing item |
| `ItemDeleteView`     | `DeleteView`   | `/<int:pk>/delete/`   | `item_confirm_delete.html`   | Confirms and deletes an item          |


## Setup
1. Clone the repository.
2. Install dependencies: `pip install django`.
3. Run migrations: `python manage.py migrate`.
4. Start the server: `python manage.py runserver`.

## Usage
- Visit the homepage to manage items.
