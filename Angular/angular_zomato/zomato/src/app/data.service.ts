import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Observable } from 'rxjs';

@Injectable({
  providedIn: 'root'
})
export class DataService {
  private apiUrl = 'http://localhost:5000/data';
  private apiOrdersUrl = 'http://localhost:5000/order';

  constructor(private http: HttpClient) { }

  getData(): Observable<any> {
    return this.http.get<any>(this.apiUrl);
  }

  getOrers(): Observable<any> {
    return this.http.get<any>(this.apiOrdersUrl);
  }

  deleteItem(id: string): Observable<any> {
    const url = `${this.apiUrl}/${id}`;
    return this.http.delete<any>(url);
  }

  updateItem(id: string, payload: any): Observable<any> {
    const url = `${this.apiUrl}/${id}`;
    return this.http.put<any>(url, payload);
  }

  addItem(newItem: any) {
    return this.http.post<any>(this.apiUrl, newItem);
  }

  placeOrder(newItem: any){
    return this.http.post<any>(this.apiOrdersUrl, newItem);
  }
}