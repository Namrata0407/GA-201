import { Component } from '@angular/core';
import { TodoService } from '../todo.service';
import { Todo } from '../todo.interface';

@Component({
  selector: 'app-create-todo',
  templateUrl: './create-todo.component.html',
  styleUrls: ['./create-todo.component.css']
})
export class CreateTodoComponent {
  newTodo: Todo = {
    id: 0,
    title: '',
    description: '',
    completed: false
  };

  constructor(private todoService: TodoService) { }

  createTodo(): void {
    this.todoService.create(this.newTodo);
    this.newTodo = { id: 0, title: '', description: '', completed: false };
  }
}
