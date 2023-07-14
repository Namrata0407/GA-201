import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';
import { CreateTodoComponent } from './create-todo/create-todo.component';
import { TodoListComponent } from './todo-list/todo-list.component';


const routes: Routes = [
    { path: 'todos', component: TodoListComponent },
    { path: 'create', component: CreateTodoComponent },
    { path: '', redirectTo: '/todos', pathMatch: 'full' },
  ];
  

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule { }
