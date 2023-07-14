import { Component } from '@angular/core';

interface Todo {
  text: string;
  status: 'Pending' | 'Completed';
}

@Component({
  selector: 'app-todo',
  templateUrl: './todo.component.html',
  styleUrls: ['./todo.component.css']
})
export class TodoComponent {
  todos: Todo[] = [];
  newTodo: string = '';

  addTodo() {
    if (this.newTodo.trim() !== '') {
      this.todos.push({ text: this.newTodo, status: 'Pending' });
      this.newTodo = '';
    }
  }

  deleteTodo(index: number) {
    this.todos.splice(index, 1);
  }

  toggleStatus(index: number) {
    if (this.todos[index].status === 'Pending') {
      this.todos[index].status = 'Completed';
    } else {
      this.todos[index].status = 'Pending';
    }
  }
}
