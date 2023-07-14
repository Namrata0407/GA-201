import { Component, Input } from '@angular/core';
import { TodoService } from '../todo.service';
import { Todo } from '../todo.interface';

@Component({
  selector: 'app-todo-item',
  templateUrl: './todo-item.component.html',
  styleUrls: ['./todo-item.component.css']
})
export class TodoItemComponent {
  @Input() todo!: Todo;

  constructor(private todoService: TodoService) { }

  markAsCompleted(): void {
    const updatedTodo: Todo = { ...this.todo, completed: true };
    this.todoService.update(updatedTodo);
  }

  deleteTodo(): void {
    this.todoService.delete(this.todo);
  }
}
