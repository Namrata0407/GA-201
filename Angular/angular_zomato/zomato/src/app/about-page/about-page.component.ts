import { Component, OnInit } from '@angular/core';
import { DataService } from '../data.service';

@Component({
  selector: 'app-about-page',
  templateUrl: './about-page.component.html',
  styleUrls: ['./about-page.component.css']
})
export class AboutPageComponent implements OnInit {
  data: any[] = [];
  selectedItem: any = null; // Holds the selected item for update
  orderselectedItem: any = null; // Holds the selected item for update
  showNewModal: boolean = false; // Controls the visibility of the new item modal

  showPlaceOrderModal: boolean = false; // Controls the visibility of the place order modal
  newItem: any = {
    dish_name: '',
    price: 0,
    availability: ''
  }; // Holds the new item data
  orderUsername: string = ''; // Holds the username for the place order modal

  constructor(private dataService: DataService) { }

  ngOnInit(): void {
    this.fetchData();
  }

  fetchData(): void {
    this.dataService.getData().subscribe(response => {
      this.data = response;
    });
  }

  openModal(item: any): void {
    this.selectedItem = { ...item }; // Make a copy of the selected item
    this.showPlaceOrderModal = false; // Close the place order modal
  }

  closeModal(): void {
    this.selectedItem = null;
  }

  submitUpdate(): void {
    this.dataService.updateItem(this.selectedItem.id, this.selectedItem).subscribe(response => {
      // Update the item in the data array
      const index = this.data.findIndex(item => item.id === this.selectedItem.id);
      if (index !== -1) {
        this.data[index] = response;
      }
      this.closeModal();
    });
  }

  deleteItem(id: string): void {
    this.dataService.deleteItem(id).subscribe(() => {
      // Remove the deleted item from the data array
      this.data = this.data.filter(item => item.id !== id);
    });
  }

  openNewModal(): void {
    this.showNewModal = true;
  }

  closeNewModal(): void {
    this.showNewModal = false;
    this.resetNewItem();
  }

  submitNewItem(): void {
    this.dataService.addItem(this.newItem).subscribe(response => {
      this.data.push(response);
      this.closeNewModal();
    });
  }

  resetNewItem(): void {
    this.newItem = {
      dish_name: '',
      price: 0,
      availability: ''
    };
  }

  openPlaceOrderModal(item: any): void {
    this.orderselectedItem = { ...item }; // Make a copy of the selected item
    this.showPlaceOrderModal = true;
  }

  closePlaceOrderModal(): void {
    this.orderselectedItem = null;
    this.showPlaceOrderModal = false;
  }

  submitOrder(): void {
    const orderData = {
      dish_name: this.orderselectedItem.dish_name,
      price: this.orderselectedItem.price,
      username: this.orderUsername
    };

    this.dataService.placeOrder(orderData).subscribe(response => {
      // Handle the success response
      // You can perform any additional actions here, such as displaying a success message
      this.closePlaceOrderModal();
    });
  }
}