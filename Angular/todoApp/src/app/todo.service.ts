import { Injectable } from '@angular/core';
import { Todo } from './todo.interface';

@Injectable({
  providedIn: 'root'
})
export class TodoService {
  todos: Todo[] = [];

  constructor() {
    this.create({ id: 1, title: 'Sample Todo 1', description: 'This is the first todo.', completed: false });
    this.create({ id: 2, title: 'Sample Todo 2', description: 'This is the second todo.', completed: true });
   }

  create(todo: Todo): void {
    todo.id = this.generateId();
    this.todos.push(todo);
  }

  read(): Todo[] {
    return this.todos;
  }

  update(updatedTodo: Todo): void {
    const index = this.todos.findIndex(todo => todo.id === updatedTodo.id);
    if (index !== -1) {
      this.todos[index] = updatedTodo;
    }
  }

  delete(todo: Todo): void {
    const index = this.todos.findIndex(t => t.id === todo.id);
    if (index !== -1) {
      this.todos.splice(index, 1);
    }
  }

  private generateId(): number {
    // Generate a unique ID here (e.g., using a library or custom logic)
    // For simplicity, we'll just use a random number generator
    return Math.floor(Math.random() * 1000000);
  }
}
