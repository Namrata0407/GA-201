import { Component } from '@angular/core';

@Component({
  selector: 'app-counter',
  templateUrl: './counter.component.html',
  styleUrls: ['./counter.component.css'],
})
export class CounterComponent {
  count: number = 0;

  increment() {
    this.count++;
  }

  decrement() {
    if (this.count === 0) {
      alert("Count can't go below zero!");
    } else {
      this.count--;
    }
    this.checkCount();
  }
  
  checkCount() {
    if (this.count === 0) {
      const decrementButton = document.getElementById(
        'decrementButton'
      ) as HTMLButtonElement;
      decrementButton.disabled = true;
    } else {
      const decrementButton = document.getElementById(
        'decrementButton'
      ) as HTMLButtonElement;
      decrementButton.disabled = false;
    }
  }
  
}
