# Todo-Flask-App

## User

### Signup
```
.com/user/signup -> post
i/p - name, email
o/p -> user_is, msg
```

### Delete
```
.com/user/delete -> post
i/p - user_id
o/p -> msg
```

## Todo

### Add
```
.com/todo/add -> post
i/p -> user_id, content, due_date, is_completed
o/p -> todo_id, msg
```

### List
```
.com/todo/list -> post
i/p -> user_id
o/p -> json list of todo created by user_id
```

### Single todo
```
.com/todo/<todo_id> -> get
i/p -> none
o/p -> user_id, todo_content, due_date, is_completed
```

### Update todo
```
.com/todo/<todo_id>/update -> post
i/p -> user_id, todo_content, due_date, is_completed
o/p -> todo_id, msg
```

### Delete todo
```
.com/todo/<todo_id>/delete -> post
i/p -> none
o/p -> msg
```