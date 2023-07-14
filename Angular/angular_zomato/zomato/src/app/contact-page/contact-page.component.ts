import { Component, OnInit } from '@angular/core';
import { DataService } from '../data.service';

@Component({
  selector: 'app-contact-page',
  templateUrl: './contact-page.component.html',
  styleUrls: ['./contact-page.component.css']
})
export class ContactPageComponent {
  data: any[] = [];

  constructor(private dataService: DataService) { }

  ngOnInit(): void {
    this.fetchOrderData();
  }

  fetchOrderData(): void {
    this.dataService.getOrers().subscribe(response => {
      this.data = response;
    });
  }
}